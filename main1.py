from selenium import webdriver

'''
Given I am on the homepage 
When I select brand category from the header 
Then I should see the list of brands 
And I select DOLCE & GABBANA brand from the list 
Then I should see the list of products from DOLCE & GABBANA
'''

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.kurtgeiger.es/")
assert "Shoes, Boots & Bags | Kurt Geiger" in driver.title  # Given I am on the homepage

driver.find_element_by_class_name("brands").click()  # When I select brand category from the header
assert "Shop By Brand | Kurt Geiger" in driver.title

brands_element = driver.find_element_by_id("tab1").find_element_by_class_name("col")
brands_list = brands_element.find_elements_by_tag_name("li")
assert len(brands_list) > 0  # Then I should see the list of brands

dolce_and_gabbana_brand_element = brands_element.find_element_by_xpath("//*[text()='Dolce & Gabbana']")
dolce_and_gabbana_brand_element.click()  # And I select DOLCE & GABBANA brand from the list

assert "Dolce & Gabbana | Kids Shoes | Kurt Geiger" in driver.title
products_element = driver.find_element_by_id("product-list")
products = products_element.find_elements_by_tag_name("li")
assert len(products) > 0  # Then I should see the list of products from DOLCE & GABBANA