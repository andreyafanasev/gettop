# Created by andrei at 9/10/20
Feature: Category
  # Enter feature description here

  Background:
    Given Open ipad Category page

  Scenario: Only items of correct category are shown
    Then Verify items of correct category (ipad) are shown

  Scenario: "Showing all <N> results" is present and reflects correct amount of items
  (count amount of products on the page to verify this)
    Then "Showing all <N> results" is present and reflects correct amount of items

  Scenario: All items have Category, Name and Price
    Then Verify all items have Category, Name and Price

  Scenario: User can open and close Quick View by clicking on closing X
    Then Verify user can open and close Quick View by clicking on closing X

  Scenario: User can click Quick View and add product to cart
    When Hover over iPad product
    And Click quick view iPad
    And Click add to cart button
    And Open the cart
    Then Verify iPad added to cart