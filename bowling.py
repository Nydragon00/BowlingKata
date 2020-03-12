import random as rndm

class Pin_counter():
    def __init__(self):
        self.min_range = 0
        self.max_range = 10
        return

    def range_pin_hit(self):
        pin_gen_range = rndm.randint(self.min_range, self.max_range)
        return pin_gen_range
