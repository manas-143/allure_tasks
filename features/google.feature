 Feature: Google map feature
  Scenario Outline: Search for top 20 places
    Given User is on the google map website searched for "<places>"
    When add top "<num>" places with its information
    Then User makes a csv file to save the information
    Examples:
      |   places      | num   |
      | Restaurant    |  5    |
      | Hotels        |  5    |
      | temples       |  5    |











