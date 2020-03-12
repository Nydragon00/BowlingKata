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

    def test_points_per_turn(self):
        assert  0 <= pin_count.count_points() <= 20 
        return

#isinstance(pin_count.chance_pin_hit(), int) ==  True
