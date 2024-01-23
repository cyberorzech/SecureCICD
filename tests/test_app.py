import pytest
from random import randint
from app import multiplicate


class Test_App:
    @pytest.fixture
    def numbers_pairs(self):
        RANDOM_NUMBERS_COUNT = 1000
        rand_floats = [
            randint(100, 1_000_000) / 100 for _ in range(RANDOM_NUMBERS_COUNT)
        ]
        pairs_list = [
            (rand_floats[i], rand_floats[i + 1]) for i in range(0, len(rand_floats), 2)
        ]
        return pairs_list

    def test_multiplicate(self, numbers_pairs):
        X_INDEX = 0
        Y_INDEX = 1
        for pair in numbers_pairs:
            result = multiplicate(x=pair[X_INDEX], times=pair[Y_INDEX])
            assert result == pair[X_INDEX] * pair[Y_INDEX]


if __name__ == "__main__":
    raise NotImplementedError("Use with pytest")
