import random as rndm

class Pin_counter():
    def __init__(self):
        self.min_range = 0
        self.max_range = 10
        self.turn_amount = 10
        self.roll_per_turn = 2
        self.overall_rolls = self.turn_amount * self.roll_per_turn
        self.game_score = []
        return

    def count_points(self):
        #self.count_round_points()
        #pin_points = 0
        return #pin_points

    def count_round_points(self):
        pin_points_round = []
        for x in range(self.roll_per_turn):
            pin_points_round.append(self.range_pin_hit())
            if (x == 0 and pin_points_round[0] == 10):
                pin_points_round = [10, 0]
                break
            elif (x == 1 and pin_points_round[0] + pin_points_round[1] >= 10):
                pin_points_round[1] = 10 - pin_points_round[0]
                break
        return pin_points_round

    def range_pin_hit(self):
        pin_gamount_gen = rndm.randint(self.min_range, self.max_range)
        return pin_gamount_gen
