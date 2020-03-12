import random as rndm

class Pin_counter():
    def __init__(self):
        self.min_range = 0
        self.max_range = 10
        self.turn_amount = 10
        self.roll_per_turn = 2
        self.overall_rolls = self.turn_amount * self.roll_per_turn
        return

    def count_points(self):
        pin_points = 0
        for x in range(self.roll_per_turn):
            pin_points += self.range_pin_hit()
        return pin_points

    def range_pin_hit(self):
        pin_gen_range = rndm.randint(self.min_range, self.max_range)
        return pin_gen_range
