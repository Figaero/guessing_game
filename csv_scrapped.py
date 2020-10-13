#guessing game that scrapes quotes from a website and presents them as answers to a user as part of a guessing game.

from random import choice
from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import DictWriter
#To pull html information into readable format

base_url = 'http://quotes.toscrape.com/'

def scrape_quotes():
	all_quotes = []
	url = '/page/1/'
	while url:
		response = requests.get(f'{base_url}{url}')
		print(f'Scraping {base_url}{url}')
		soup = BeautifulSoup(response.text,'html.parser')
		quotes = soup.find_all(class_='quote')

		for quote in quotes:
			all_quotes.append({
				'text': quote.find(class_="text").get_text(),
				'author': quote.find(class_='author').get_text(),
				'link': quote.find('a')['href']
				})
		next_bttn = soup.find(class_='next') 
		url = next_bttn.find('a')['href'] if next_bttn else None
		sleep(2)

	return all_quotes



def write_quotes(quotes)
	with open('quotes.csv', 'w') as file:
		headers = ['text','author','link']
		csv_writer = DictWriter(file, fieldnames=headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)