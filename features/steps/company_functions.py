from Ui_functions import click, scroll, get_text, get_url, title
import re


def extracting_information_of_company(page, name_selector, rating_selector, review_selector, address_selector,
                                      direction_selector):
    """this function takes locators of each element that will provide the information about the company and store the
    information in a dict as key and value pair, after that it returns the dict"""

    company_details_dict = {}  # adding the place details in dictionary
    try:
        company_details_dict['Name'] = get_text(page, name_selector)
    except:
        company_details_dict['Name'] = None
    try:
        company_details_dict['Rating'] = get_text(page, rating_selector)
    except:
        company_details_dict['Rating'] = None
    try:
        company_details_dict['Review'] = get_text(page, review_selector)
    except:
        company_details_dict['Review'] = None
    try:
        company_details_dict['Address'] = get_text(page, address_selector)
    except:
        company_details_dict['Address'] = None

    try:
        click(page, direction_selector)
        page.reload()
        company_url = get_url(page)
        pattern = r'@([0-9.-]+,[0-9.-]+,[0-9a-zA-Z]+)'  # regular expression pattern to extract lat and long
        matches = re.search(pattern, company_url)
        company_details_dict["Latitude and Longitude"] = matches.group(1)
    except:
        company_details_dict["Latitude and Longitude"] = None

    return company_details_dict


