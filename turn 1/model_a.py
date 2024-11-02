import unittest
import random

class MyAPI:
	def process_data(self, data):
		if random.randint(1, 5) == 1:
			raise ValueError("Invalid data format")
		elif random.randint(1,10) ==1:
			raise KeyError("Missing required key")
		return data.upper()

class TestMyAPI(unittest.TestCase):

	def setUp(self):
		self.api = MyAPI()

	def test_process_data_with_valid_data(self):
		data = "hello"
		result = self.api.process_data(data)
		self.assertEqual(result, "HELLO")

	def test_process_data_handles_valueerror(self):
		with self.assertRaises(ValueError) as cm:
			self.api.process_data("invalid")
		self.assertEqual(str(cm.exception), "Invalid data format")

	def test_process_data_handles_keyerror(self):
		with self.assertRaises(KeyError) as cm:
			self.api.process_data({"key": "value"})
		self.assertEqual(str(cm.exception), "Missing required key")

	def test_process_data_handles_unexpected_exceptions(self):
		for _ in range(10):
			with self.assertRaises(Exception):
				self.api.process_data(None)

if __name__ == '__main__':
	unittest.main()
