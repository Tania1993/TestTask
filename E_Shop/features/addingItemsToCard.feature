# Created by Tetiana_Haiuk at 11/4/2020

Feature: adding items to the card
  Guest user goes to a favorite e-shop, navigates to some category and adds two
  most expensive items to the shopping cart from this category

  Scenario Outline: open the e-shop
    Given guest user opens the e-shop with <url>
    Examples:
      | url                    |
      | https://makeup.com.ua/ |

  Scenario: adding expensive items to a card
    When user selects a category
      | category      |
      | Health & Care |
    Then sorts results by price in desc order
    Then user adds <count> most expensive items to the card
      | count |
      | 2     |