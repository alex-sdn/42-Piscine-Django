import sys

def get_state(capital):
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

    rev_states = {tag: state for state, tag in states.items()}
    rev_capital_cities = {capital: tag for tag, capital in capital_cities.items()}

    try:
        state = rev_states[rev_capital_cities[capital]]
        print(state)
    except KeyError:
        print('Unknown capital city')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_state(sys.argv[1])