Feature: get company details
  Scenario Outline: Fetch company details and save to CSV
   Given User is on the google website searched for "<company name>"
    When User extracts company's information
    Then User makes a file to save the information of company in csv
    Examples:
      |            company name              |
      |actualize consulting engineers pvt.ltd|
      |         nimesa technologies          |
      |    sulopa technologies pvt ltd       |
