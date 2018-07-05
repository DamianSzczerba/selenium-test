import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
Given I select men category from the header
And I am on PDP
When I select any colour and size for the chosen men category
And I add the product to the bag
Then I can see the bag with single item
And I click 'Proceed to Checkout'
Then I should be on checkout page
'''

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.kurtgeiger.es/")
assert "Shoes, Boots & Bags | Kurt Geiger" in driver.title

driver.find_element_by_class_name("men").click()  # Given I select men category from the header
assert "Men's Shoes | Kurt Geiger" in driver.title

products_element = driver.find_element_by_id("product-list")
products_list = products_element.find_elements_by_tag_name("li")
assert len(products_list) > 0
products_list[0].click()  # And I am on PDP

options_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "product-options"))
)

colours_list = options_element.find_element_by_id("colours").find_elements_by_tag_name("li")
colours_list[1].click()  # When I select any colour for the chosen men category

''' 
the first sizes list is a list for mobile view, which will cause the following Exception: 
ElementNotInteractableException: could not be scrolled into view. 
Select the next class which is for bigger screens 
'''
sizes_list = options_element.find_elements_by_class_name("sizes ")[1].find_elements_by_tag_name("li")
sizes_list[0].click()  # When I select any size for the chosen men category

add_to_bag_btn = driver.find_element_by_id("add-to-cart-ss17")
add_to_bag_btn.click()  # And I add the product to the bag

time.sleep(1)  # give it some time for the item to be added to the bag

bag_icon = driver.find_element_by_class_name("skiplinks_count")
hover = ActionChains(driver).move_to_element(bag_icon)
hover.perform()  # open the dropdown menu

time.sleep(1)  # let the dropdown cart stay open for a while

cart_list = driver.find_element_by_id("mini-cart").find_elements_by_class_name("btn-remove")
assert len(cart_list) == 1  # Then I can see the bag with single item

go_to_bag_and_checkout_btn = driver.find_element_by_xpath("//*[text()='go to bag & checkout']")
go_to_bag_and_checkout_btn.click()  # And I click 'Proceed to Checkout'

assert "My Bag | Kurt Geiger" in driver.title  # Then I should be on checkout page
