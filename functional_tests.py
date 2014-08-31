from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# User goes to homepage.
		self.browser.get('http://localhost:8000')

		# Sees page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# Is invited to enter a to-do item immediately

		# Types "Bus peacock feathers" into a text box

		# Hits enter, page updates, now page lists
		# 1: Buy peakcock feathers" as an item in the list

		# There's still a text box for another item.
		# Enters "Use peacock feathers to make a fly"

		# Page updates again, both itmes now shown in list

		# There is a unique URL and explanatory text

		# Vists the URL, site still there

		# Fin

if __name__ == '__main__':
	unittest.main(warnings='ignore')
