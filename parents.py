import random
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
        self.love_for_child = love_for_child
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