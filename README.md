# selenium-test

Language used: Python 3.4
Tested on: Firefox 61.0 (64-bit), Windows 10

# main1.py
Given I am on the homepage 

When I select brand category from the header 

Then I should see the list of brands 

And I select DOLCE & GABBANA brand from the list 

Then I should see the list of products from DOLCE & GABBANA



# main2.py
Given I select men category from the header

And I am on PDP

When I select any colour and size for the chosen men category

And I add the product to the bag

Then I can see the bag with single item

And I click 'Proceed to Checkout'

Then I should be on checkout page

