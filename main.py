import random
from parents import Parent
import sys
import time



class player:
    def __init__(self, name, age , height, health, looks, sex, money, income, hair_type, race,nepotism, hair_texture):

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
        self.nepotism = nepotism
        self.hair_texture = hair_texture

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
        print(f"Nepotism: {self.nepotism}")
        print(f"Hair Texture: {self.hair_texture}")
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
        cb = random.choice(["straight", "curly", "wavy", "coily"])
        self.hair_texture = cb
        return self.hair_type, self.hair_texture

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
        if self.Parent.love_for_child > 50 and self.Parent.wealth_bracket.lower() >= "mid_high":
            self.nepotism = 0.2
        if self.Parent.love_for_child <= 50 or self.Parent.wealth_bracket.lower() < "high":
            self.nepotism = 0.5
        if self.Parent.love_for_child > 50 and self.Parent.wealth_bracket.lower() < "very_high":
            self.nepotism = 0.8
        if self.Parent.love_for_child > 50 and self.Parent.wealth_bracket.lower() >= "elon_musk":
            self.nepotism = 1.0
        else:
            self.nepotism = 0

        return self.nepotism
    def set_parent(self, parent):
        self.Parent = parent
        return self.Parent
    def set_hair_type(self, hair_type):
        c = random.choice(["blonde", "brown", "black", "red"])
        self.hair_type = c
        return self.hair_type, self.hair_texture
    def set_hair_texture(self, hair_texture):
        c = random.choice(["straight", "curly", "wavy", "coily"])
        self.hair_texture = c
        return self.hair_texture
    def set_job(self, job, neportism):
        if self.nepotism == 1:
            self.job = random.choice(["owner of big company", "kpop idol"])
        elif self.nepotism == 0.8:
            self.job = random.choice(["CEO", "CFO", "CTO", "COO"])
        elif self.nepotism == 0.5:
            self.job = random.choice(["manager", "supervisor"])
        elif self.nepotism == 0.2:
            self.job = random.choice([
                "Accountant", "Actor", "Architect", "Audiologist", "Baker", "Barber", "Biologist", "Blacksmith", "Bus Driver", "Butcher", "Carpenter", "Cashier", "Chef", "Chemist", "Civil Engineer", "Cleaner", "Cook", "Designer", "Detective", "Electrician", "Editor", "Mechanic", "Farmer", "Fashion Designer", "Firefighter", "Flight Attendant", "Florist", "Gardener", "Graphic Designer", "Hairdresser", "Journalist", "Librarian", "Lifeguard", "Musician", "Nurse", "Photographer", "Plumber", "Police Officer", "Receptionist"
                ])
        else:
            self.job = random.choice(["unemployed", "mcdonlalds fry cook", "coal miner", "human experiment guy","backround actor"])
        return self.job
    def get_money(self):
        return self.money
    def get_job(self):
        return self.job
    def work_job(self):
        if self.job == "unemployed":
            print("You can't work because you're unemployed")
        else:
            if self.nepotism == 1:
                daily_salary = random.randint(10000,200000)  # Example salary for high nepotism
                self.money += daily_salary
            elif self.nepotism == 0.8:
                daily_salary = random.randint(5000,100000)  # Example salary for medium-high nepotism
                self.money += daily_salary
            elif self.nepotism == 0.5:
                daily_salary = random.randint(1000,5000)  # Example salary for medium nepotism
                self.money += daily_salary
            elif self.nepotism == 0.2:
                daily_salary = random.randint(500,1000)  # Example salary for low nepotism
                self.money += daily_salary
            else:
                daily_salary = random.randint(100,400)  # Example salary for very low nepotism
                self.money += daily_salary

    def what_u_wanna_do(self, nepotism):
        if self.money < 1000:
            print("You broke your staying home idc or working a job")
            if self.job != "unemployed":
                self.work_job()
        if self.money >= 1000:
            print("what u wanna do?")

    def stay_home(self):
    


def main():
    pass
    
    