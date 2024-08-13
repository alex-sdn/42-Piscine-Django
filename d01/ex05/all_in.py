import sys

def get_capital_or_state(arg):
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

    formatted_arg = arg.lower().title()

    try:
        capital = capital_cities[states[formatted_arg]]
        print(capital, "is the capital of", formatted_arg)
    except KeyError:
        try:
            state = rev_states[rev_capital_cities[formatted_arg]]
            print(formatted_arg, "is the capital of", state)
        except KeyError:
            print(arg, "is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        split_arg = sys.argv[1].split(',')
        
        for arg in split_arg:
            if arg.strip():
                get_capital_or_state(arg.strip())  # just format here?