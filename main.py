from asyncio import wait
import random
from parents import Parent
import sys
import time

class Parent:
    def __init__(self, name, wealth_bracket, children, love_for_child,  ):
        self.name = name
        self.wealth_bracket = wealth_bracket
        self.children = children
        self.love_for_child = love_for_child

    def add_child(self, child):
        self.children+= 1

    def get_children(self):
        return self.children
    def get_wealth_bracket(self):
        return self.wealth_bracket
    def get_love_for_child(self):
        return self.love_for_child
    def set_love_for_child(self, love_for_child):
        love_for_child = random.randint(0, 100)
        self.love_for_child = love_for_child
        return self.love_for_child
    def set_wealth_bracket(self, wealth_bracket):
        wealth_brackets = ["homeless", "low", "low-mid", "mid_low", "mid", "middle_high", "high", "very_high", "elon_musk"]
        number = random.randint(0, 1000)
        if number < 200:
            self.wealth_bracket = wealth_brackets[0]  # homeless
        elif number < 400:
            self.wealth_bracket = wealth_brackets[1]  # low
        elif number < 600:
            self.wealth_bracket = wealth_brackets[2]  # low-mid
        elif number < 700:
            self.wealth_bracket = wealth_brackets[3]  # mid_low
        elif number < 800:
            self.wealth_bracket = wealth_brackets[4]  # mid
        elif number < 900:
            self.wealth_bracket = wealth_brackets[5]  # middle_high
        elif number < 970:
            self.wealth_bracket = wealth_brackets[6]  # high
        elif number < 990:
            self.wealth_bracket = wealth_brackets[7]  # very_high
        else:
            self.wealth_bracket = wealth_brackets[8]  # elon_musk

    def __str__(self):
        return f"Parent: {self.name}, Children: {[child.name for child in self.children]}"

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
        print("You stayed home and did nothing.")
        self.money -= 100  
        if self.money < 0:
            self.die()
    def par_death(self):
        self.Parents = None
        print("Your parents have died.")
        self.nepotism = 0  # Losing nepotism after parents die
    def gamble(self):
        bet = int(input("Enter your bet: "))
        self.money -= bet
        if random.random() < 0.3:
            self.money += bet * 2
            print(f"You won {bet * 2} in the gamble.")
        else:
            print(f"You lost {bet} in the gamble.")
        if self.money < 0:
            self.die()
    def play_games(self,):
        if random.randint(1, 100) < 5:
            print("You got addicted to gaming and lost all your money.")
            self.money = 0
        else:
            print("You played games and had fun.")
            self.money -= 50
        if self.money < 0:
            self.die()
    def __str__(self):
        return f"Player(name={self.name}, age={self.age}, height={self.height}, health={self.health}, looks={self.looks}, sex={self.sex}, money={self.money}, income={self.income}, hair_type={self.hair_type}, race={self.race}, nepotism={self.nepotism}, hair_texture={self.hair_texture})"
    
    def workout(self):
        print("You worked out and improved your health.")
        if self.health < 100:
            self.health += 10
        self.money -= 50
        if self.money < 0:
            self.die()
    def cry_sadly(self):
        print("You cried sadly.")
        self.health += 5
        if self.health > 100:
            self.health = 100
        self.money -= 50
        if self.money < 0:
            self.die()
    def feel_happy(self):
        print("You feel happy.")
        self.health += 5
        if self.health > 100:
            self.health = 100
        self.money -= 50
        if self.money < 0:
            self.die()

    def make_choice(self):
        print("What would you like to do?")
        print("1. Stay home")
        print("2. Work a job")
        print("3. Gamble")
        print("4. Check your status")
        print("5. Play games")
        print("6. Workout")
        print("7. Cry sadly")
        print("8. Feel happy")
        choice = input("Enter your choice: ").strip().lower()
        wait(1)
        if choice == "1":
            self.stay_home()
            wait(1)
            self.make_choice()
        elif choice == "2":
            self.work_job()
            wait(1)
            self.make_choice()
        elif choice == "3":
            self.gamble()
            wait(1)
            self.make_choice()
        elif choice == "4":
            print(self)
            wait(1)
            self.make_choice()
        elif choice == "5":
            self.play_games()
            wait(1)
            self.make_choice()
        elif choice == "6":
            self.workout()
            wait(1)
            self.make_choice()
        elif choice == "7":
            self.cry_sadly()
            wait(1)
            self.make_choice()
        elif choice == "8":
            self.feel_happy()
            wait(1)
            self.make_choice()
        else:
            print("Invalid choice. Please try again.")
        
        



def main():
    Player = player(name=None, age=None, height=None, health=None, looks=None, sex=None, money=None, income=None, hair_type=None, race=None, nepotism=None, hair_texture=None)
    player_name = Player.set_name(player_name)
    player_age = Player.set_age(player_age)
    player_height = Player.set_height(player_height)
    player_health = Player.set_health(player_health)
    player_looks = Player.set_looks(player_looks)
    player_sex = Player.set_sex(player_sex)
    player_money = Player.set_money(player_money)
    player_income = Player.set_income(player_income)
    player_hair_type, player_hair_texture = Player.set_hair_type(player_hair_type)
    player_race = Player.set_race(player_race)
    player_nepotism = Player.set_nepotism(player_nepotism)
    print("Player characteristics:")
    print("-" * 30)
    print(Player)

    while Player.is_alive():
        Player.make_choice()
    print("Game Over")
    print(Player)
    print("Thanks for playing!")
    print("wanna play again?")
    play_again = input("Enter 'yes' to play again or 'no' to quit: ").strip().lower()
    if play_again == 'yes':
        main()
    else:
        print("Goodbye!")
        exit()
