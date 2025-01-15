import random

class RussianRoulette:
    def __init__(self, num_bullets=1, num_chambers=6):
        """
        Initializes a new game of Russian Roulette.

        Args:
            num_bullets: The number of bullets in the chamber (default: 1)
            num_chambers: The total number of chambers in the revolver (default: 6)

        Raises:
            ValueError: If the number of bullets is greater than the number of chambers.
        """
        if num_bullets > num_chambers:
            raise ValueError("Number of bullets cannot exceed number of chambers.")
        self.num_bullets = num_bullets
        self.num_chambers = num_chambers
        self.chamber_index = 0 

    def spin_chamber(self):
        """
        Spins the chamber randomly.
        """
        self.chamber_index = random.randint(0, self.num_chambers - 1)

    def pull_trigger(self):
        """
        Simulates pulling the trigger.
        """
        if self.chamber_index < self.num_bullets:
            return "BANG!"  # Game Over
        else:
            self.chamber_index = (self.chamber_index + 1) % self.num_chambers 
            return "Click"

def play_game():
    """
    Plays a single round of Russian Roulette.

    Warns the user about the dangers of real-life Russian Roulette.
    """
    print("WARNING: This is a simulation. Russian Roulette is a highly dangerous and irresponsible game. "
          "This code is for educational and entertainment purposes only and should never be attempted in reality.")

    game = RussianRoulette()
    game.spin_chamber()

    while True:
        input("Press Enter to pull the trigger... ") 
        result = game.pull_trigger()
        print(result)
        if result == "BANG!":
            print("Game Over! You have successfully killed yourself!")
            break

if __name__ == "__main__":
    play_game()