import random
import sys
import time

# Keep time.sleep as the delay used throughout the game.


class Parent:
    def __init__(self, name, wealth_bracket, children, love_for_child):
        self.name = name
        self.wealth_bracket = wealth_bracket
        self.children = children
        self.love_for_child = love_for_child

    def add_child(self, amount=1):
        if isinstance(self.children, list):
            self.children.append(amount)
        else:
            self.children += amount

    def get_children(self):
        return self.children

    def get_wealth_bracket(self):
        return self.wealth_bracket

    def get_love_for_child(self):
        return self.love_for_child

    def set_love_for_child(self, love_for_child=None):
        self.love_for_child = random.randint(0, 100)
        return self.love_for_child

    def set_wealth_bracket(self, _wealth_bracket=None):
        wealth_brackets = [
            "homeless",
            "low",
            "low-mid",
            "mid_low",
            "mid",
            "middle_high",
            "high",
            "very_high",
            "elon_musk",
        ]
        number = random.randint(0, 1000)
        if number < 200:
            self.wealth_bracket = wealth_brackets[0]
        elif number < 400:
            self.wealth_bracket = wealth_brackets[1]
        elif number < 600:
            self.wealth_bracket = wealth_brackets[2]
        elif number < 700:
            self.wealth_bracket = wealth_brackets[3]
        elif number < 800:
            self.wealth_bracket = wealth_brackets[4]
        elif number < 900:
            self.wealth_bracket = wealth_brackets[5]
        elif number < 970:
            self.wealth_bracket = wealth_brackets[6]
        elif number < 990:
            self.wealth_bracket = wealth_brackets[7]
        else:
            self.wealth_bracket = wealth_brackets[8]
        return self.wealth_bracket

    def __str__(self):
        if isinstance(self.children, list):
            child_names = [getattr(c, "name", str(c)) for c in self.children]
        else:
            child_names = self.children
        return (
            f"Parent(name={self.name}, wealth={self.wealth_bracket}, "
            f"love={self.love_for_child}, children={child_names})"
        )


class Player:
    def __init__(
        self,
        name,
        age,
        height,
        health,
        looks,
        sex,
        money,
        income,
        hair_type,
        race,
        nepotism,
        hair_texture,
        job="unemployed",
        parent=None,
    ):
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
        self.job = job
        self.parent = parent

    def display_life_characteristics(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
        print(f"Health: {self.health}")
        print(f"Looks: {self.looks}")
        print(f"Sex: {self.sex}")
        print(f"Money: {self.money}")
        print(f"Income: {self.income}")
        print(f"Job: {self.job}")
        print(f"Hair Type: {self.hair_type}")
        print(f"Race: {self.race}")
        print(f"Nepotism: {self.nepotism}")
        print(f"Hair Texture: {self.hair_texture}")

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

    def get_job(self):
        return self.job

    def set_height(self, height=None):
        self.height = random.randint(46, 96)
        return self.height

    def set_health(self, health):
        self.health = max(0, min(100, health))
        return self.health

    def set_looks(self, looks=None):
        self.looks = random.randint(0, 10)
        return self.looks

    def set_sex(self, sex=None):
        self.sex = input("Enter sex: ").strip()
        return self.sex

    def set_money(self, money=None):
        if self.parent is None:
            self.money = random.randint(0, 100)
            return self.money

        wealth_bracket = self.parent.get_wealth_bracket()
        if wealth_bracket == "homeless":
            amount = random.randint(0, 100)
        elif wealth_bracket == "low":
            amount = random.randint(100, 500)
        elif wealth_bracket == "low-mid":
            amount = random.randint(500, 1000)
        elif wealth_bracket == "mid_low":
            amount = random.randint(1000, 2000)
        elif wealth_bracket == "mid":
            amount = random.randint(2000, 5000)
        elif wealth_bracket == "middle_high":
            amount = random.randint(5000, 10000)
        elif wealth_bracket == "high":
            amount = random.randint(10000, 50000)
        elif wealth_bracket == "very_high":
            amount = random.randint(50000, 100000)
        else:
            amount = random.randint(100000, 1000000)

        self.money = amount
        return self.money

    def set_income(self, income=None):
        self.income = random.randint(0, 100)
        return self.income

    def set_hair_type(self, hair_type=None):
        self.hair_type = random.choice(["blonde", "brown", "black", "red"])
        self.hair_texture = random.choice(["straight", "curly", "wavy", "coily"])
        return self.hair_type, self.hair_texture

    def set_hair_texture(self, hair_texture=None):
        self.hair_texture = random.choice(["straight", "curly", "wavy", "coily"])
        return self.hair_texture

    def set_race(self, race=None):
        self.race = random.choice(["white", "black", "asian", "hispanic"])
        return self.race

    def set_nepotism(self, nepotism=None):
        if self.parent is None:
            self.nepotism = 0
            return self.nepotism

        love = self.parent.love_for_child
        wealth = self.parent.wealth_bracket
        if wealth == "elon_musk" and love > 50:
            self.nepotism = 1.0
        elif wealth in ("very_high", "high") and love > 50:
            self.nepotism = 0.8
        elif wealth in ("middle_high", "mid", "mid_low") and love > 50:
            self.nepotism = 0.5
        else:
            self.nepotism = 0.2
        return self.nepotism

    def set_age(self, age=None):
        self.age = 18 if age is None else age
        return self.age

    def set_name(self, name=None):
        entered = input("Enter name: ").strip()
        self.name = entered
        if entered.lower() == "sam altman":
            self.die()
        return self.name

    def set_job(self, job=None, nepotism=None):
        tier = self.nepotism if nepotism is None else nepotism
        if tier == 1:
            self.job = random.choice(["owner of big company", "kpop idol"])
        elif tier == 0.8:
            self.job = random.choice(["CEO", "CFO", "CTO", "COO"])
        elif tier == 0.5:
            self.job = random.choice(["manager", "supervisor"])
        elif tier == 0.2:
            self.job = random.choice([
                "Accountant", "Actor", "Architect", "Audiologist", "Baker",
                "Barber", "Biologist", "Blacksmith", "Bus Driver", "Butcher",
                "Carpenter", "Cashier", "Chef", "Chemist", "Civil Engineer",
                "Cleaner", "Cook", "Designer", "Detective", "Electrician",
                "Editor", "Mechanic", "Farmer", "Fashion Designer", "Firefighter",
                "Flight Attendant", "Florist", "Gardener", "Graphic Designer",
                "Hairdresser", "Journalist", "Librarian", "Lifeguard",
                "Musician", "Nurse", "Photographer", "Plumber", "Police Officer",
                "Receptionist",
            ])
        else:
            self.job = random.choice([
                "unemployed", "mcdonlalds fry cook", "coal miner",
                "human experiment guy", "backround actor",
            ])
        return self.job

    def set_parent(self, parent):
        self.parent = parent
        return self.parent

    def work_job(self):
        if not self.job or self.job == "unemployed":
            print("You can't work because you're unemployed.")
            return

        if self.nepotism == 1:
            daily_salary = random.randint(10000, 200000)
        elif self.nepotism == 0.8:
            daily_salary = random.randint(5000, 100000)
        elif self.nepotism == 0.5:
            daily_salary = random.randint(1000, 5000)
        elif self.nepotism == 0.2:
            daily_salary = random.randint(500, 1000)
        else:
            daily_salary = random.randint(100, 400)

        self.income = daily_salary
        self.money += daily_salary
        print(f"You worked as a {self.job} and earned ${daily_salary}.")

    def what_u_wanna_do(self, nepotism=None):
        if self.money < 1000:
            print("You broke your staying home idc or working a job")
            if self.job != "unemployed":
                self.work_job()
        else:
            print("what u wanna do?")

    def _spend_money(self, amount):
        self.money -= amount
        if self.money < 0:
            self.die()

    def stay_home(self):
        print("You stayed home and did nothing.")
        self._spend_money(100)

    def par_death(self):
        self.parent = None
        print("Your parents have died.")
        self.nepotism = 0

    def gamble(self):
        if self.money <= 0:
            self.die()
            return "You have run out of money."

        try:
            bet = int(input(f"Enter your bet (max ${self.money}): "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if bet <= 0:
            print("Bet must be greater than 0.")
            return
        if bet > self.money:
            print("You can't bet more money than you have.")
            return

        self.money -= bet
        if random.random() < 0.3:
            winnings = bet * 2
            self.money += winnings
            print(f"You won ${winnings} in the gamble.")
        else:
            print(f"You lost ${bet} in the gamble.")

        if self.money <= 0:
            self.die()

    def play_games(self):
        if random.randint(1, 100) < 5:
            print("You got addicted to gaming and lost all your money.")
            self.money = 0
        else:
            print("You played games and had fun.")
            self._spend_money(50)

    def workout(self):
        print("You worked out and improved your health.")
        if self.health < 100:
            self.health = min(100, self.health + 10)
        self._spend_money(50)

    def cry_sadly(self):
        print("You cried sadly.")
        if self.health < 100:
            self.health = min(100, self.health + 5)
        self._spend_money(50)

    def feel_happy(self):
        print("You feel happy.")
        if self.health < 100:
            self.health = min(100, self.health + 5)
        self._spend_money(50)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return (
            f"Player(name={self.name}, age={self.age}, height={self.height}, "
            f"health={self.health}, looks={self.looks}, sex={self.sex}, "
            f"money={self.money}, income={self.income}, job={self.job}, "
            f"hair_type={self.hair_type}, race={self.race}, "
            f"nepotism={self.nepotism}, hair_texture={self.hair_texture})"
        )

    def make_choice(self):
        print("\nWhat would you like to do?")
        print("1. Stay home")
        print("2. Work a job")
        print("3. Gamble")
        print("4. Check your status")
        print("5. Play games")
        print("6. Workout")
        print("7. Cry sadly")
        print("8. Feel happy")
        choice = input("Enter your choice: ").strip().lower()
        time.sleep(1)

        if choice == "1":
            self.stay_home()
            time.sleep(1)
            if self.is_alive():
                print(str(self))
        elif choice == "2":
            self.work_job()
            time.sleep(1)
        elif choice == "3":
            self.gamble()
            time.sleep(1)
        elif choice == "4":
            print(self)
            time.sleep(1)
        elif choice == "5":
            self.play_games()
            time.sleep(1)
        elif choice == "6":
            self.workout()
            time.sleep(1)
        elif choice == "7":
            self.cry_sadly()
            time.sleep(1)
        elif choice == "8":
            self.feel_happy()
            time.sleep(1)
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        parent = Parent("John Doe", "mid", 0, random.randint(0, 100))
        parent.set_wealth_bracket()

        hero = Player(
            None, None, None, 100, None, None, None, None, None, None, None, None
        )
        hero.set_parent(parent)
        hero.set_name()
        if not hero.is_alive():
            print("Game Over")
            print(hero)
            print("Thanks for playing!")
        else:
            hero.set_age()
            hero.set_height()
            hero.set_health(100)
            hero.set_looks()
            hero.set_sex()
            hero.set_money()
            hero.set_income()
            hero.set_hair_type()
            hero.set_race()
            hero.set_nepotism()
            hero.set_job()

            print("\nPlayer characteristics:")
            print("-" * 30)
            print(hero)
            time.sleep(5)

            while hero.is_alive():
                hero.make_choice()

            print("\nGame Over")
            print(hero)
            print("Thanks for playing!")

        play_again = (
            input("Enter 'yes' to play again or 'no' to quit: ").strip().lower()
        )
        if play_again != "yes":
            print("Goodbye!")
            sys.exit()


if __name__ == "__main__":
    main()