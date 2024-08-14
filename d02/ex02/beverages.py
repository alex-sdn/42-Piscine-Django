class HotBeverage:
    price = 0.30
    name = 'hot beverage'

    def description(self):
        return 'Just some hot water in a cup.'
    
    def __str__(self):
        return (f'name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}\n')
    
class Coffee(HotBeverage):
    name = 'coffee'
    price = 0.40

    def description(self):
        return 'A coffee, to stay awake.'
    
class Tea(HotBeverage):
    name = 'tea'

class Chocolate(HotBeverage):
    name = 'chocolate'
    price = 0.50
    
    def description(self):
       return 'Chocolate, sweet chocolate...'
    
class Cappuccino(HotBeverage):
    name = 'cappuccino'
    price = 0.45

    def description(self):
        return 'Un po’ di Italia nella sua tazza!'

if __name__ == '__main__':
    hotbeverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappucino = Cappuccino()

    print(hotbeverage.__str__())
    print(coffee.__str__())
    print(tea.__str__())
    print(chocolate.__str__())
    print(cappucino.__str__())