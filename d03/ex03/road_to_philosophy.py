import sys
import requests
from bs4 import BeautifulSoup

def request_failed():
    print('An error occured during the GET request')
    exit()

def check_first_page(article):
    response = requests.get("https://en.wikipedia.org" + article)

    if response.status_code == 200:
        return True
    return False

def check_end_conditions(roads: list):
    # if reached philosophy
    if roads[-1] == 'Philosophy':
        for road in roads:
            print(road)
        print(f'{len(roads)} roads from {roads[0]} to philosophy')
        return True

    # if about to loop
    if len(roads) != len(set(roads)):
        # print(roads)
        print('It leads to an infinite loop!')
        return True
    
    return False


def scrape_title(article):
    wiki_url = "https://en.wikipedia.org"

    response = requests.get(wiki_url + article)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title_tag = soup.find('h1', class_='firstHeading mw-first-heading')

        # if title in italics
        if title_tag.find('i') != None:
            return title_tag.find('i').text
        else:
            return title_tag.find('span', class_='mw-page-title-main').text
    else:
        request_failed()
    
def scrape_article(article):
    wiki_url = "https://en.wikipedia.org"

    response = requests.get(wiki_url + article)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        paragraphs = soup.select('p:not(table p)')

        # iterate until intro paragraph
        for paragraph in paragraphs:
            # Skip if has a class or is in a blockquote
            if paragraph.get('class') != None or paragraph.find_parent('blockquote'):
                continue
            # Skip paragraphs in italics (not main paragraph)
            italic_part = paragraph.find('i')
            if italic_part != None and italic_part.text.strip() == paragraph.text.strip():
                continue

            # get first link to article
            anchors = paragraph.find_all('a')
            for elem in anchors:
                link = elem.get('href')
                if link[:6] == '/wiki/' and not ':' in link:
                         return (link)
            return None
    else:
        request_failed()

def roads_to_philosophy(arg):
    roads = []
    article = '/wiki/' + arg.replace(' ', '_')
    title = None

    if not check_first_page(article):
        print('Argument passed is not an existing page')
        exit()

    title = scrape_title(article)
    roads.append(title)

    while not check_end_conditions(roads):
        article = scrape_article(article)

        if article == None:
            # print(roads)
            print('It leads to a dead end!')
            exit()

        title = scrape_title(article)
        roads.append(title)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        roads_to_philosophy(sys.argv[1])
    else:
        print('One argument expected')