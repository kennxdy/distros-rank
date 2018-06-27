from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen


banner = r'''
  _____  _     _                   _____             _    
 |  __ \(_)   | |                 |  __ \           | |   
 | |  | |_ ___| |_ _ __ ___  ___  | |__) |__ _ _ __ | | __
 | |  | | / __| __| '__/ _ \/ __| |  _  // _` | '_ \| |/ /
 | |__| | \__ \ |_| | | (_) \__ \ | | \ \ (_| | | | |   < 
 |_____/|_|___/\__|_|  \___/|___/ |_|  \_\__,_|_| |_|_|\_\
                                                          

'''

def search_rank():
	url = 'https://distrowatch.com/'

	with urlopen(url) as response:
		html = response.read()

		page = Soup(html, 'html.parser')
		distros = page.find_all("td", class_="phr2")
		pos = 1
		print('------------------')

		for i in range(number):
			print("|{}| {}".format(pos, distros[i].text))
			print("------------------")
			pos += 1

			
if __name__ == '__main__':
	print(banner)
	number = int(input("Enter the number of positions: "))
	print("Please wait while we fetch the data for you...")
	print('')
	search_rank()
