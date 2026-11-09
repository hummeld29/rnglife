import random
from parents import Parent


class player:
    def __init__(self, name, age , height, health, looks, sex, money, income, hair_type, race,nepotism = False):

        self.name = name
        self.age = age
        self.height = height
        self.health = health
        self.looks = looks
        self.sex = sex
        self.money = money
        self.income = income
        self.hair_type = hair_type
        self.race = race
        self.nepotism = False

    def display_life_characteristics(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Health: {self.health}")
        print(f"Looks: {self.looks}")
        print(f"Sex: {self.sex}")
        print(f"Money: {self.money}")
        print(f"Income: {self.income}")
        print(f"Hair Type: {self.hair_type}")
        print(f"Race: {self.race}")
        print(f"Nepotism: {self.nepotismc}")
    def die(self):
        self.health = 0
        print(f"{self.name} has died.")
    def get_height(self):
        return self.height

    def get_health(self):
        return self.health

    def get_looks(self):
        return self.looks

    def get_sex(self):
        return self.sex

    def get_money(self):
        return self.money

    def get_income(self):
        return self.income

    def get_hair_type(self):
        return self.hair_type

    def get_race(self):
        return self.race

    def get_nepotism(self):
        return self.nepotism
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_height(self, height):
        c = random.randint(57, )
    