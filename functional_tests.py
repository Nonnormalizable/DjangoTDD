from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        sefl.assertIn('To-Do', header_text)

        # Is invited to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # Types "Bus peacock feathers" into a text box
        inputbox.send_keys('Buy peakcock feathers')

        # Hits enter, page updates, now page lists
        # 1: Buy peakcock feathers" as an item in the list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assrtTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
            )

        # There's still a text box for another item.
        # Enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        # Page updates again, both itmes now shown in list

        # There is a unique URL and explanatory text

        # Vists the URL, site still there

        # Fin

if __name__ == '__main__':
    unittest.main(warnings='ignore')
