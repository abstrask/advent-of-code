import requests
from bs4 import BeautifulSoup
import html2text
import datetime

def aoc_task_getter(day=datetime.datetime.now().day, year=datetime.datetime.now().year):
    # Make a GET request to fetch the raw HTML content
    url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day)
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the body or any other part you're interested in
    body = soup.find('article')
    if body is None:
        return "No body tag found in HTML."

    # Convert HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown = h.handle(str(body))

    #s ave to md file
    with open("day" + str(day) + ".md", "w") as file:
        file.write(markdown)

    return markdown

aoc_task_getter()