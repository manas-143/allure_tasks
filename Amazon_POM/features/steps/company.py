import csv
from behave import given, when, then
from Ui_functions import send_input, click, get_text, get_url
from company_functions import extracting_information_of_company

locators = {
    "INPUT AREA": '//textarea[@id="APjFqb"]',
    "REVIEWS": '//div[@class="CJQ04"]/div/span[@class="hqzQac"]/span/a',
    "ADDRESS": "//div[@data-dtype='d3ifr']/span[@class='LrzXr']",
    "RATINGS": '//div[@class="CJQ04"]/div/span[@aria-hidden="true"]',
    "NAME": "//div[@class='SPZz6b']/h2[@data-attrid='title']/span",
    "DIRECTION BTN": "//a[@class='ab_button' and @tabindex='0']//div"

}


@given(u'User is on the google website searched for "{places}"')
def searching_for_places(context, places):
    context.page.goto("https://www.google.co.in/")
    context.search = places  # this will make the name of csv file according to the search items
    send_input(context.page, locators["INPUT AREA"], places)
    context.page.keyboard.press("Enter")


@when(u'User extracts company\'s information')
def user_extracts_information_of_company(context):
    details = extracting_information_of_company(context.page, locators["NAME"], locators["RATINGS"],
                                                locators["REVIEWS"], locators["ADDRESS"], locators["DIRECTION BTN"])
    context.company_details = []  # stores the details of the company
    context.company_details.append(details)  # details holds a dict containing of information that we append in list


@then("User makes a file to save the information of company in csv")
def user_saves_company_details_to_csv(context):
    # Specify the CSV file name
    csv_file_path = 'company_details.csv'

    # Extract the keys from the first dictionary in the list
    field_names = context.company_details[0].keys()

    # Write data to CSV
    with open(csv_file_path, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(context.company_details)
