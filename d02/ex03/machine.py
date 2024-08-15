from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
    def __init__(self):
        self.served = 0

    class EmptyCup(HotBeverage):
        name = 'empty cup'
        price = 0.90

        def description(self):
            return 'An empty cup?! Gimme my money back!'
        
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired')

    def repair(self):
        self.served = 0

    def serve(self, hotbeverage: HotBeverage):
        if self.served < 10:
            self.served += 1

            if random.random() < 0.5:  # generates number between 0 and 1
                return hotbeverage()
            else:
                return self.EmptyCup()  # count as served ?
        else:
            raise self.BrokenMachineException()

if __name__ == '__main__':
    machine = CoffeeMachine()

    try:
        beverage = machine.serve(HotBeverage)
        print(str(beverage))
        
        beverage = machine.serve(HotBeverage)
        print(str(beverage))

        beverage = machine.serve(Coffee)
        print(str(beverage))

        beverage = machine.serve(Coffee)
        print(str(beverage))
        
        beverage = machine.serve(Tea)
        print(str(beverage))

        beverage = machine.serve(Tea)
        print(str(beverage))

        beverage = machine.serve(Chocolate)
        print(str(beverage))

        beverage = machine.serve(Chocolate)
        print(str(beverage))

        beverage = machine.serve(Cappuccino)
        print(str(beverage))

        beverage = machine.serve(Cappuccino)
        print(str(beverage))

        beverage = machine.serve(HotBeverage)
        print(str(beverage))
    except Exception as e:
        print(e)

    print('\n>REPAIRING<\n')
    machine.repair()

    try:
        beverage = machine.serve(HotBeverage)
        print(str(beverage))
        
        beverage = machine.serve(HotBeverage)
        print(str(beverage))

        beverage = machine.serve(Coffee)
        print(str(beverage))

        beverage = machine.serve(Coffee)
        print(str(beverage))
        
        beverage = machine.serve(Tea)
        print(str(beverage))

        beverage = machine.serve(Tea)
        print(str(beverage))

        beverage = machine.serve(Chocolate)
        print(str(beverage))

        beverage = machine.serve(Chocolate)
        print(str(beverage))

        beverage = machine.serve(Cappuccino)
        print(str(beverage))

        beverage = machine.serve(Cappuccino)
        print(str(beverage))

        beverage = machine.serve(HotBeverage)
        print(str(beverage))
    except Exception as e:
        print(e)