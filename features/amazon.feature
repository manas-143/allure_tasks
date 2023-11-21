Feature: Amazon laptop purchase
  Scenario Outline: Search for laptops,add to cart and verify the total price
    Given User is on the amazon website search for "<items>"
    When User filter by "<star>" ratings
    And add top "<num>" laptops to the cart
    Then the total amount in the cart should match the laptop prices
    Examples:
      |   items    | star |  num |
      | hp laptops |   2  |   3  |
      |dell laptops|   3  |   3  |
      |acer laptops|   2  |   3  |

