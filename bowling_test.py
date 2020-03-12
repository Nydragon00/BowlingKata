import pytest
import bowling

class Tests():

    def test_created_chance_pin(self):
        pin_count = bowling.Pin_counter()
        assert pin_count.chance_pin_hit() == True
