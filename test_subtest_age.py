import unittest
from age import categorize_by_age

class TestIsChild(unittest.TestCase):

    def test_child_age(self):
        for age in range(0, 9):   # ages 0–8 (adjust if needed)
            with self.subTest(age=age):
                result = categorize_by_age(age)

                # Print message like in your screenshot
                print(f"{age} is considered as a child.")

                self.assertEqual(result, "Child")


class TestIsAdult(unittest.TestCase):

    def test_adult_age(self):
        for age in range(19, 25):   # example adult range
            with self.subTest(age=age):
                result = categorize_by_age(age)

                print(f"{age} is considered as an adult.")

                self.assertEqual(result, "Adult")


if __name__ == "__main__":
    unittest.main(verbosity=2)