import dewiki.parser
import requests
import json
import sys
import dewiki

def get_first_result(arg):
    params = {
        'action': 'opensearch',
        'search': arg,
        'limit': 2
    }
    response = requests.get("https://en.wikipedia.org/w/api.php", params=params)

    if response.status_code == 200:
        # print(response.json())
        data = response.json()

        if len(data[1]) > 0:
            return data[1][0]
        return None
    
def get_page_content(title):
    # params = {
    #     'action': 'query',
    #     'prop': 'revisions',
    #     'titles': title,
    #     'rvslots': '*',
    #     'rvprop': 'content',
    #     'formatversion': '2',
    #     'format': 'json'
    # }

    params = {
        'action': 'parse',
        'page': title,
        'prop': 'wikitext',
        'formatversion': '2',
        'format': 'json'
    }

    response = requests.get("https://en.wikipedia.org/w/api.php", params=params)
    
    if response.status_code == 200:
        # print(response.json())
        data = response.json()
        # content = data.get('query').get('pages')[0].get('revisions')[0].get('slots').get('main').get('content')
        content = data.get('parse').get('wikitext')
        # print(content)
        return content
    else:
        return None

def get_wiki(arg):
    first_result = get_first_result(arg)

    if not first_result:
        print('No page found for this term')
        exit()
    # print(f'searching for {first_result}')

    content = get_page_content(first_result)
    
    if not content:
        print(f'Failed to retrieve page content for {first_result}')
        exit()

    clean_content = dewiki.from_string(content)
    # print(clean_content)

    # write in file
    filename = first_result.replace(' ', '_') + '.wiki'

    try:
        with open(filename, 'w') as file:
            file.write(clean_content)
    except:
        print('Failed to create .wiki file')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_wiki(sys.argv[1])
    else:
        print('One argument expected')