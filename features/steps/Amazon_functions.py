from Ui_functions import send_input, click


def select_items_extract_prices(page, item_list_selector, price_selector, cart_btn_selector,
                                number):  # function for item's price extract
    all_items = page.locator(item_list_selector)
    amount = []

    for i in range(int(number)):
        with page.expect_popup() as page1_info:
            all_items.nth(i).click()  # click on each laptop
        page1 = page1_info.value  # going to the next tab
        amt = page1.locator(price_selector).inner_text()  # locator for amount
        amount.append(float(amt.replace(",", "")))  # storing each laptop value in float
        page1.locator(cart_btn_selector).click()  # adding the laptop to cart
        page1.close()  # closing the new tab
    return amount  # returning the amount to base page


def total_cart_prices(page, selector):
    final_price = page.locator(selector).inner_text()  # extracting the total price of the cart
    price = final_price.replace(",", "")
    cart_amt = float(price)
    return cart_amt
