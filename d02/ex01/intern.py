class Intern:
    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self.Name = name

    def __str__(self):
        return self.Name
    
    class Coffee:
        def __str__(self):
            return 'This is the worst coffee you ever tasted'
    
    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    nameless = Intern()
    mark = Intern('Mark')
    
    print(str(nameless))  # REPLACE EVERYWHERE
    print(str(mark))

    coffee = mark.make_coffee()
    print(str(coffee))

    try:
        nameless.work()
    except Exception as e:
        print(e)