import unittest

from stats import average, median, spread, summarize


class StatsTest(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)

    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_even(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_spread(self):
        self.assertEqual(spread([5, 1, 9]), 8)

    def test_summarize(self):
        self.assertEqual(summarize([1, 2, 3]), {"average": 2, "median": 2, "spread": 2})


if __name__ == "__main__":
    unittest.main()
