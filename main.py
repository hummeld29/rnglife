import random
from parents import Parent
import sys


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
        sys.exit()
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
        c = random.randint(57, 96)
        self.height = c
        return self.height

    def set_health(self, health):
        health = max(0, min(100, health))
        self.health = health
        return self.health

    def set_looks(self, looks):
        c = random.randint(0, 10)
        self.looks = c
        return self.looks

    def set_sex(self, sex):
        c = input("Enter sex: ")
        self.sex = c
        return self.sex

    def set_money(self, money):
        wealth_bracket = self.Parent.get_wealth_bracket()
        if wealth_bracket == "homeless":
            c = random.randint(0, 100)
        elif wealth_bracket == "low":
            c = random.randint(100, 500)
        elif wealth_bracket == "low-mid":
            c = random.randint(500, 1000)
        elif wealth_bracket == "mid_low":
            c = random.randint(1000, 2000)
        elif wealth_bracket == "mid":
            c = random.randint(2000, 5000)
        elif wealth_bracket == "middle_high":
            c = random.randint(5000, 10000)
        elif wealth_bracket == "high":
            c = random.randint(10000, 50000)
        elif wealth_bracket == "very_high":
            c = random.randint(50000, 100000)
        else:
            c = random.randint(100000, 1000000)
        self.money = c
        return self.money

    def set_income(self, income):
        c = random.randint(0, 100)
        self.income = c
        return self.income

    def set_hair_type(self, hair_type):
        c = random.choice(["blonde", "brown", "black", "red"])
        self.hair_type = c
        return self.hair_type

    def set_race(self, race):
        c = random.choice(["white", "black", "asian", "hispanic"])
        self.race = c
        return self.race

    def set_nepotism(self, nepotism):
        c = random.choice([True, False])
        self.nepotism = c
        return self.nepotism
    def set_age(self, age):
        c = 18
        self.age = c
        return self.age
    def set_name(self, name):
        c = input("Enter name: ")
        if c.lower() == "sam altman":
            self.die()
            
        self.name = c
        return self.name
    def set_nepotism(self, nepotism):
        if self.Parent.love_for_child > 50:
            self.nepotism = True
        else:
            self.nepotism = False
        return self.nepotism
    def set_parent(self, parent):
        self.Parent = parent
        return self.Parent
    def 



def main():
    pass
    
    