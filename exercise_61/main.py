class Person:
    def __self__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def weight_grow(self, kg):
        self.weight += kg

    def height_grow(self, cm):
        self.height += cm

    def old_grow(self, years):
        self.age += years
        if self.age < 21:
            self.height_grow(0.5 * years)



pessoa = Person()

pessoa.name = 'Alceu'
pessoa.age = 18
pessoa.weight = 60
pessoa.height = 165
pessoa.old_grow(2)
print(pessoa.height)
