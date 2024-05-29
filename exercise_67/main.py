class Car:
    def __init__(self, fuel_consume, fuel_quantity=0):
        self.fuel_consume = fuel_consume
        self.fuel_quantity = fuel_quantity

    def show_fuel(self):
        print(f'O carro possui {self.fuel_quantity:.2f} litros de combustível.')

    def to_walk(self, distance):
        if self.fuel_quantity <= 0:
            print('Carro sem combustível.')
        else:
            car_consume = (distance / self.fuel_consume)
            self.fuel_quantity = (self.fuel_quantity - car_consume)
    
    def add_fuel(self, quantity):
        self.fuel_quantity = (self.fuel_quantity + quantity)
        print(f'O veículo foi abastecido com {quantity:.2f} litros.')



meuFusca = Car(fuel_consume=15)
meuFusca.add_fuel(20)

meuFusca.to_walk(100)
meuFusca.show_fuel()