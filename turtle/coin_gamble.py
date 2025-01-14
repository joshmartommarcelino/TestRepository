import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'  # Default side

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

# Create an instance of the Coin class
my_coin = Coin()

# Toss the coin
my_coin.toss()

# Display the result after the toss
print("You got:", my_coin.get_sideup())
