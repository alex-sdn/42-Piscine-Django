import sys

def get_capital(state):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    try:
        capital = capital_cities[states[state]]
        print(capital)
    except KeyError:
        print('Unknown state')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_capital(sys.argv[1])