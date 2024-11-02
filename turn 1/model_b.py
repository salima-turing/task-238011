import unittest
import random


# Module under test
class MyAPI:
    def process_data(self, input_data):
        if random.randint(1, 3) == 1:  # Simulate random exception behavior
            raise ValueError("Some random error occurred")
        return input_data + 1


class TestMyAPI(unittest.TestCase):
    def setUp(self):
        self.api = MyAPI()

    # Decorator to handle expected exceptions
    @unittest.expectedFailure
    def test_process_data_expects_value_error(self):
        with self.assertRaises(ValueError):
            self.api.process_data("something")

    # Wrap test function to handle non-determinism
    def test_process_data_non_determinism_wrapper(self):
        for _ in range(10):  # Try multiple times to catch the exception
            try:
                self.api.process_data("something")
            except ValueError:
                # Exception is caught, test passes
                return
        # If the exception is never caught, the test fails
        self.fail("Expected ValueError to be raised")


if __name__ == "__main__":
    unittest.main()
