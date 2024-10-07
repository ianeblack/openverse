import requests
from bs4 import BeautifulSoup
import socket
from colorama import init, Fore, Style
from prettytable import PrettyTable

table = PrettyTable(max_table_width=33)

# Check if connected to the internet and run code accordingly
def is_connected_to_internet():
    """Check if connected to the internet by attempting to connect to Google's DNS server"""
    try:
        # Attempt to connect to Google's DNS server (8.8.8.8) on port 53
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        pass
    return False


def randomVerse():
    """pick a random Bible verse from the dailyverses.net website"""
    version = "KJV"
    # Make a request to the dailyverses.net website
    response = requests.get(f'https://dailyverses.net/random-bible-verse/{version}')

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the Bible verse element
    verse_element = soup.find(class_='v1')

    # Find the Bible book element
    book_element = soup.find(class_='vc')

    # Extract the verse text
    verse_text = verse_element.text.strip()

    # Extract the book text
    book_pick = book_element.text.strip()
    book = book_pick

    table.add_column(f'{Fore.GREEN}{book}{Style.RESET_ALL}', [f"{verse_text}"])
    print(table)


if is_connected_to_internet():
    randomVerse()
else:
    pass
