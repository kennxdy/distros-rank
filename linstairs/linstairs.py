from urllib.request import urlopen

from bs4 import BeautifulSoup

banner = r"""
 __                            __
/\ \       __                 /\ \__           __
\ \ \     /\_\    ___     ____\ \ ,_\    __   /\_\  _ __   ____
 \ \ \  __\/\ \ /' _ `\  /',__\\ \ \/  /'__`\ \/\ \/\`'__\/',__\
  \ \ \L\ \\ \ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_\ \ \ \ \//\__, `\
   \ \____/ \ \_\ \_\ \_\/\____/ \ \__\ \__/.\_\\ \_\ \_\\/\____/
    \/___/   \/_/\/_/\/_/\/___/   \/__/\/__/\/_/ \/_/\/_/ \/___/


"""


def search_rank(position_number):
    url = 'https://distrowatch.com/'
    with urlopen(url) as response:
        html = response.read()
        page = BeautifulSoup(html, 'html.parser')
        distributions = page.find_all('td', class_='phr2')
        rank = {}
        for number in range(position_number):
            rank.update({(number + 1): distributions[number].text})
        return rank


def main():
    print(banner)
    try:
        number = int(input('Number of positions: '))
        print('Please wait while we fetch the data for you...\n')
        rank = search_rank(number)
        for position in rank:
            print('|{}| {}'.format(position, rank[position]))
    except ValueError:
        print('Enter a number of positions you would like to see!')


if __name__ == '__main__':
    main()
