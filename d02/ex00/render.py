import sys

def get_dict():
    try:
        with open('settings.py', 'r') as file:
            content = file.read()

            settings = {}
            exec(content, {}, settings)

            return settings
    except:
        print('An error occured when opening settings.py')
        exit()

def format_template(template, settings):
    try:
        with open(template, 'r') as file:
            content = file.read()
            replaced_content = content.format(**settings)

            return replaced_content
    except:
        print('An error occured when opening the template')
        exit()

def create_html(template):
    settings = get_dict()
    replaced_content = format_template(template, settings)
    filename = template.replace('.template', '.html')

    try:
        with open(filename, 'w') as file:
            file.write(replaced_content)
    except:
        print('An error occured when creating the file')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].endswith('.template'):
        create_html(sys.argv[1])
    else:
        print('single .template file expected as argument')
