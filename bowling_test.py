import pytest
import bowling

pin_count = bowling.Pin_counter()

class Tests_range_pin_hit():
    def test_range_int_pin(self):
        assert isinstance(pin_count.range_pin_hit(), int) ==  True

    def test_min_range_pin(self):
        assert pin_count.min_range == 0
        return

    def test_max_range_pin(self):
        assert pin_count.max_range == 10
        return

    def test_points_is_list(self):
        assert isinstance(pin_count.count_round_points(), list) == True
        return

    def test_points_per_turn_under_10(self):
        turn_points_list = pin_count.count_round_points()
        combined_points = turn_points_list[0] + turn_points_list[1]
        assert 0 <= combined_points <= 10
        return

    def test_current_point_list(self):
        spare_strike_checked = pin_count.spare_strike_checker()
        assert pin_count.game_length == len(pin_count.spare_strike_checker())
        return
