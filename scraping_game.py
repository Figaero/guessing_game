#guessing game that scrapes quotes from a website and presents them as answers to a user as part of a guessing game.

from random import choice
from bs4 import BeautifulSoup
import requests
from csv import DictReader

#To pull html information into readable format

base_url = 'http://quotes.toscrape.com/'


def read_quotes(filename):
	with open(filename, 'r') as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

def start_game(quotes):
	quote = choice(quotes)
	num_guesses = 4
	print("Here's a quote")
	print(quote["text"])
	guess = ''
	while guess.lower() != quote['author'].lower() and num_guesses:
		guess = input(f'Who said this quote? Guesses remaining: {num_guesses}\n')
		if guess.lower() == quote['author'].lower():
			print (f"Correct Answer. You get a cookie for guessing: {quote['author']}\n")
			break
		num_guesses -= 1
		if num_guesses == 3:
			res = requests.get(f"{base_url}{quote['link']}")
			soup = BeautifulSoup(res.text,'html.parser')
			birthdate = soup.find(class_="author-born-date").get_text()
			birthplace = soup.find(class_="author-born-location").get_text()
			print (f"Here's a hint: The author was born {birthplace} on {birthdate}")


		elif num_guesses == 2:
			last_initial = quote['author'].split(' ')[1][0]
			print(f"The authors initials are {quote['author'][0]}{last_initial}")

		elif num_guesses == 0:
			print(f"Sorry you ran out of guesses. The correct answers was {quote['author']}\n")
			break


	play_again = ''
	while play_again.lower() not in ('y','yes','no','n'):
		play_again = input("Do you want to play again(Y/N)?: ")
	if play_again.lower() in ('y','yes'):
		print('Okay play again\n')
		return start_game(quotes)
	else:
		print('Okay, goodbye')

quotes = read_quotes("quotes.csv")
start_game(quotes)