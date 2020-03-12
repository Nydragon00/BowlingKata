import random as rndm

class Pin_counter():
    def __init__(self):
        self.min_range = 0
        self.max_range = 10
        self.turn_amount = 10
        self.roll_per_turn = 2
        self.overall_rolls = self.turn_amount * self.roll_per_turn
        self.game_score = []
        self.game_points = []
        self.game_length = 0
        return

    def count_points(self):
        for x in range(self.turn_amount):
            self.game_points += self.count_round_points()
            self.game_points = self.spare_strike_checker()
        return self.game_points

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

    def spare_strike_checker(self):
        self.game_length = len(self.game_points)
        except_str = "Out of index range: first(spare)/second(strike)."
        try:
            current_round_points = self.game_points[self.game_length][0] + self.game_points[self.game_length][1]
            former_round_points = self.game_points[self.game_length-1][0] + self.game_points[self.game_length-1][1]
        except:
            print(except_str)
            pass
        try:
            if (self.game_points[self.game_length-2][0] == 10):
                self.game_points[self.game_length-2][0] += current_round_points
        except:
            print(except_str)
            pass
        try:
            if (former_round_points == 10):
                self.game_points[self.game_length-1][1] += current_round_points
        except:
            print(except_str)
            pass
        return self.game_points
