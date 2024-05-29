class virtualAnimal:
    def __init__(self, name, hungry=100, health=100, age=0):
        self.name = name
        self.hungry = hungry
        self.health = health
        self.age = age


    def change_name(self, new_name):
        self.name = new_name
        return self.name

    
    def change_hungry(self, new_hungry):
        self.hungry = new_hungry
        return self.hungry

    
    def change_health(self, new_health):
        self.health = new_health
        return self.health


    def change_age(self, new_age):
        self.age = new_age
        return self.age


    def show_humor(self):
        if int(self.health) + int(self.hungry) / 2 < 50:
            return f'O tamagushi está triste'
        else:
            return f'O tamagushi está contente.'
        

tamagushi = virtualAnimal(name='AX', age=12)

print(tamagushi.health)
print(tamagushi.hungry)
print(tamagushi.show_humor())
tamagushi.change_health(25)
tamagushi.change_hungry(25)
print(tamagushi.health)
print(tamagushi.hungry)
print(tamagushi.show_humor())