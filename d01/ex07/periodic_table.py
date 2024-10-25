import sys


class Element():
    def __init__(self, name, position, number, small, molar, electron):
        self.name = name
        self.position = position
        self.number = number
        self.small = small
        self.molar = molar
        self.electron = electron

    def table_print(self):
        """Returns elem data for table data cell"""
        return ('    ' * 5 + f'<h4>{self.name}</h4>\n'
                + '    ' * 5 + '<ul>\n'
                + '    ' * 6 + f'<li>No {self.number}</li>\n'
                + '    ' * 6 + f'<li>{self.small}</li>\n'
                + '    ' * 6 + f'<li>{self.molar}</li>\n'
                + '    ' * 6 + f'<li>{self.electron}</li>\n'
                + '    ' * 5 + '</ul>\n')


def get_elements() -> list[Element]:
    """
    Returns a list of Element from periodic_table.txt
    Note: assumes numbers are in order (add sort?)
    """
    try:
        with open('periodic_table.txt', 'r') as file:
            elements = []
            
            for line in file:
                name = line.split('=')[0].strip()
                attributes = line.split('=')[1].strip().split(',')

                for attribute in attributes:
                    key = attribute.split(':')[0].strip()
                    value = attribute.split(':')[1].strip()

                    if key == 'position':
                        position = int(value)
                    elif key == 'number':
                        number = value
                    elif key == 'small':
                        small = value
                    elif key == 'molar':
                        molar = value
                    elif key == 'electron':
                        electron = value

                elem = Element(name, position, number, small, molar, electron)
                elements.append(elem)

            return elements
    except Exception as e:
        print(str(e))
        exit()


def get_elem_rows(elements) -> list[list[Element]]:
    """
    Returns a list of lists of Element sorted by rows
    """
    elem_rows = []
    row = []
    row.append(elements[0])

    for i in range(1, len(elements)):
        if elements[i].position > elements[i - 1].position:
            row.append(elements[i])
        else:
            elem_rows.append(row.copy())
            row.clear()
            row.append(elements[i])

    elem_rows.append(row)
    return elem_rows


def html_table(elem_rows):
    """
    Creates .html file and writes in periodic table from elem_rows
    """
    try:
        with open('periodic_table.html', 'w') as file:
            file.write('<!DOCTYPE html>\n<html lang="en">\n')
            file.write('    <head>\n        <title>Periodic table</title>\n    </head>\n')
            file.write('    <body>\n        <table>\n')

            for row in elem_rows:
                file.write('            <tr>\n')
                pos = 0
                for elem in row:
                    while elem.position > pos:
                        file.write('    ' * 4 + '<td></td>\n')
                        pos += 1
                    if elem.position == pos:
                        file.write('    ' * 4 + '<td style="border: 1px solid black; padding:10px">\n')
                        file.write(elem.table_print())
                        file.write('    ' * 4 + '</td>\n')
                    pos += 1
                file.write('            </tr>\n')

            file.write('        </table>\n    </body>\n</html>')
    except Exception as e:
        print(e)

def periodic_table():
    elements = get_elements()
    elem_rows = get_elem_rows(elements)
    html_table(elem_rows)


if __name__ == '__main__':
    periodic_table()