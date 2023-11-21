from Ui_functions import click, scroll, get_text


def scrolling_down_until_it_gets_desire_number(page, selector, number):
    """this function take the locator in which all displayed item stored. after that it scroll down to make visible the
    items that are invisible in initial state. after getting desired number of items it stores them in a list and return
     the list"""

    all_item = []
    while len(all_item) < number:
        items = page.query_selector_all(selector)  # all displayed items
        items[0].click()
        scroll(page)  # Scrolling for displaying more items
        all_item = items
    return all_item


def extracting_information_of_places(page, name_selector, rating_selector, review_selector, address_selector):
    """this function takes locators of each element that will provide the information about the place and store the
    information in a dict as key and value pair, after that it returns the dict"""

    item_dict = {}  # adding the place details in dictionary
    try:
        item_dict['Name'] = get_text(page, name_selector)
    except:
        item_dict['Name'] = None
    try:
        item_dict['Rating'] = get_text(page, rating_selector)
    except:
        item_dict['Rating'] = None
    try:
        item_dict['Review'] = get_text(page, review_selector)
    except:
        item_dict['Review'] = None
    try:
        item_dict['Address'] = get_text(page, address_selector)
    except:
        item_dict['Address'] = None

    return item_dict
