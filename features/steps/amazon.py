from behave import given, when, then
from Ui_functions import send_input, click
from Amazon_functions import select_items_extract_prices, total_cart_prices

"""......................all the locators......................"""

locators = {
    "SEARCH BOX": "xpath=//input[@type='text']",
    "RATING": "xpath =//section[@aria-label='{} Stars & Up']",
    "ITEMS LIST": "xpath=//span[@class='a-size-medium a-color-base a-text-normal']",
    "ADD TO CART BTN": "xpath=//input[@id='add-to-cart-button' and @title='Add to Shopping Cart']",
    "CART ICON": "xpath=//*[@class='nav-cart-icon nav-sprite']",
    "TOTAL CART PRICE": "xpath=//*[@id='sc-subtotal-amount-buybox']/span",
    "ITEM PRICE": "xpath=//span[@id='tp_price_block_total_price_ww']/descendant::span[@class='a-price-whole']"
}
""".............................................................."""


@given(u'User is on the amazon website search for "{search_query}"')
def searching_for_products(context, search_query):
    context.page.goto("https://www.amazon.in/")
    send_input(context.page, locators["SEARCH BOX"], search_query)  # user entered search item and searched for product
    context.page.keyboard.press("Enter")


@when(u'User filter by "{star}" ratings')
def filtering_the_items(context, star):
    # locators["RATING"] = f"xpath =//section[@aria-label='{star} Stars & Up']"
    ratings = locators["RATING"].format(star)
    click(context.page, ratings)


@when(u'add top "{num}" laptops to the cart')
def adding_multiple_items(context, num):
    context.amount = []  # to store the price of each item
    x = select_items_extract_prices(context.page, locators["ITEMS LIST"], locators["ITEM PRICE"],locators["ADD TO CART BTN"], num)
    context.amount = x


@then(u'the total amount in the cart should match the laptop prices')
def price_compare(context):
    click(context.page, locators["CART ICON"])
    cart_amt = total_cart_prices(context.page, locators["TOTAL CART PRICE"])
    laptop_amt = sum(context.amount)
    assert laptop_amt == cart_amt, "Amount not matching"  # comparing the price
