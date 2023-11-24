from Ui_functions import send_input, click


def select_items_extract_prices(page, item_list_selector, price_selector, cart_btn_selector,
                                number, close_btn):  # function for item's price extract
    all_items = page.locator(item_list_selector)
    amount = []
    links = []
    for i in range(int(number)):
        page_link = "https://www.amazon.in/"+all_items.nth(i).get_attribute("href")
        print(page_link)
        links.append(page_link)

    for link in links:
        page.goto(link)
        amt = page.locator(price_selector).inner_text()  # locator for amount
        amount.append(float(amt.replace(",", "")))  # storing each laptop value in float
        page.locator(cart_btn_selector).click()  # adding the laptop to cart
        page.locator(close_btn).click()
    return amount  # returning the amount to base page


def total_cart_prices(page, selector):
    final_price = page.locator(selector).inner_text()  # extracting the total price of the cart
    price = final_price.replace(",", "")
    cart_amt = float(price)
    return cart_amt
