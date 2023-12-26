import csv
from behave import given, when, then
from Ui_functions import send_input, click, get_text, get_url
from company_functions import extracting_information_of_company

locators = {
    "INPUT AREA": '//textarea[@id="APjFqb"]',
    "REVIEWS": "//span[@class='hqzQac']//a//span",
    "ADDRESS": "//div[@data-dtype='d3ifr']/span[@class='LrzXr']",
    "RATINGS": "//*[@class='Aq14fc']",
    "NAME": "//div[@data-attrid='title']",
    "DIRECTION BTN": "(//span[@class='AQtWSd' and @aria-hidden='true'])[2]/following-sibling::div"

}

company_details = []
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
    print(details)
    company_details.append(details)  # details holds a dict containing of information that we append in list
    print(company_details)


@then("User makes a file to save the information of company in csv")
def user_saves_company_details_to_csv(context):
    # Specify the CSV file name
    csv_file_path = 'company_details.csv'

    # Extract the keys from the first dictionary in the list
    field_names = ["Name", "Rating", "Review", "Address", "Latitude and Longitude"]

    # Write data to CSV
    with open(csv_file_path, mode="w", newline="", encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(company_details)
