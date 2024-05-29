class fuelPump:
    def __init__(self, fuel_kind, value_liter, fuel_quantity) -> None:
        self.fuel_kind = fuel_kind
        self.value_liter = value_liter
        self.fuel_quantity = fuel_quantity


    def supply_per_value(self, value):
        print(f'O valor a ser abastecido é R$ {value:.2f}')
        calculate_liter = value / self.value_liter
        self.fuel_quantity = round((self.fuel_quantity - calculate_liter), 2)
        print(f'Foi abastecido {calculate_liter:.2f} litros')


    def supply_per_liter(self, value):
        print(f'Será abastecido {value} litros.')
        calculate_value = value * self.value_liter
        self.fuel_quantity = round((self.fuel_quantity - value), 2)
        print(f'O valor a ser pago é de R$ {calculate_value:.2f}')


    def change_value_fuel(self, new_value):
        self.value_liter = float(new_value)
        print(f'O combustível passará a custar R$ {self.value_liter:.2f} o litro')

    
    def change_combustible_kind(self, new_value):
        self.fuel_kind = str(new_value)


    def change_fuel_pump_quantity(self, new_value):
        self.fuel_quantity = float(new_value)
        print(f'A bomba possui {self.fuel_quantity:.2f} litros')



fuelpump1 = fuelPump(fuel_kind='Adtivada', value_liter=5.77, fuel_quantity=60000)


