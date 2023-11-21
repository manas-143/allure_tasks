from behave import given, when, then
import csv
from Ui_functions import send_input, click
from Google_functions import scrolling_down_until_it_gets_desire_number, extracting_information_of_places

tags = {
    "INPUT_AREA": "xpath=//*[@jslog='11886']",
    "SEARCH_BTN": "xpath=//*[@jslog='11887']",
    "SEARCH ITEMS": "xpath=//*[@class='Nv2PK THOPZb CpccDe ']/a",
    "PLACE_NAME": "//h1[@class='DUwDvf lfPIob']",
    "RATINGS": "(//span[@class='ceNzKf']//preceding-sibling::span)[1]",
    "REVIEW": "(//div[@class='F7nice ']//span)[9]",
    "ADDRESS": "(//div[@class='rogA2c ']//div)[1]"

}


@given(u'User is on the google map website searched for "{places}"')
def searching_for_places(context, places):
    context.page.goto("https://www.google.com/maps")
    context.search = places  # this will make the name of csv file according to the search items
    send_input(context.page, tags["INPUT_AREA"], places)
    click(context.page, tags["SEARCH_BTN"])


@when(u'add top "{number}" places with its information')
def adding_places_with_information(context, number):
    context.L = []  # List of all places
    num = int(number)  # Converting string to int
    total_item = scrolling_down_until_it_gets_desire_number(context.page, tags["SEARCH ITEMS"], num)  # this returns
    # the total number of items

    for i in range(num):
        total_item[i].click()
        values=extracting_information_of_places(context.page,tags["PLACE_NAME"], tags["RATINGS"],tags["REVIEW"], tags["ADDRESS"])

        # adding individual details to list by removing duplicates
        if values not in context.L:
            context.L.append(values)


@then(u'User makes a csv file to save the information')
def saves_places_details_to_csv(context):
    # Specify the CSV file path
    csv_file_path = f'{context.search}.csv'

    # Extract the keys from the first dictionary in the list (assuming all dictionaries have the same keys)
    field_names = context.L[0].keys()

    # Write data to CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(context.L)

