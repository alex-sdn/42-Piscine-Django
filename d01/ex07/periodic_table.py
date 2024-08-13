import sys

# Returns dict with key=element and value=(position, number, small, molar, electron)
# Sorted by number
def get_elements():
    try:
        with open('periodic_table.txt', 'r') as file:
            lines = file.readlines()
            elements = {}

            for line in lines:
                elem       = line.split('=')[0].strip()
                attributes = line.split('=')[1].strip().split(',')
                attributes_clean = []
                
                # Keep values only
                for attribute in attributes:
                    attributes_clean.append(attribute.split(':')[1].strip())
                # Cast position and number as int
                attributes_clean[0] = int(attributes_clean[0])
                attributes_clean[1] = int(attributes_clean[1])
                attributes_clean.append(elem)
                
                elements[attributes_clean[1]] = tuple(attributes_clean)
            
            # Sort dict by number
            sorted_elements = dict(sorted(elements.items(), key=lambda x: x[1][1]))
            
            return sorted_elements
    except:
        print('failed to open .txt')
        exit()

# Returns row of element (0 - 8)
def get_row(elements, num):
    pos = elements[num][0]

    pos_count = 0
    num_pos = 0

    for key,value in elements.items():
        if value[0] == pos:
            pos_count += 1
            if key == num:
                num_pos = pos_count

    # col 3 - 16 have 2 extra rows
    # if pos > 2 and pos < 17:
    #     return 9 - pos_count + num_pos - 1
    # else:
        return 7 - pos_count + num_pos - 1

def periodic_table():
    elements = get_elements()

    # for key,value in elements.items():
    #     print(key, ':', value)

    # Print out symbols (temp test)
    num = 1

    for row in range(9):
        for col in range(18):
            if elements[num][0] == col and get_row(elements, num) == row:
                print(elements[num][2].ljust(4), end='')
                num += 1
            else:
                print('    ', end='')
        print()



if __name__ == '__main__':
    periodic_table()