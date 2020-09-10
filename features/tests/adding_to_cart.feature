# Created by andrei at 9/7/20
Feature: Adding to cart
  # Enter feature description here

  Scenario: User can add product to cart
    Given Open macbook-pro-13 product page
    When Click add to cart button
    And Open the cart
    Then Verify "MacBook Pro 13-inch" added to cart

  Scenario: User can click + to modify amount of items to add to cart,
    upon adding to cart, correct amount of items shown in the cart
    Given Open macbook-pro-13 product page
    When Click + to increase amount of items to add to cart
    And Click add to cart button
    And Open the cart
    Then Verify that amount of items (2) shown in top nav menu are correct

  Scenario: User can click "-" to modify amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    Given Open macbook-pro-13 product page
    When Click + to increase amount of items to add to cart
    And Click + to increase amount of items to add to cart
    And Click "-" to decrease amount of items to add to cart
    And Click add to cart button
    And Open the cart
    Then Verify that amount of items (2) shown in top nav menu are correct

  Scenario: User can type in amount of items to add to cart, upon adding to cart,
  correct amount of items shown in the cart
    Given Open macbook-pro-13 product page
    When Type in amount of items to add to cart (2)
    And Click add to cart button
    Then Verify that amount of items (2) shown in top nav menu are correct

  Scenario: User sees " ... have been added to your cart" confirmation upon adding items to cart
    Given Open macbook-pro-13 product page
    When Click add to cart button
    Then Verify MacBook Pro 13-inch has been added to your cart message is shown

  Scenario: User can click through multiple products by clicking back and forward arrows
    Given Open macbook-pro-13 product page
    When Click back arrow
    Then Verify macbook-pro-16 page open
    When Click forward arrow
    Then Verify macbook-pro-13 page open

  Scenario: If product is out of stock, user sees 'Out of Stock',
  Add to Cart and Checkout buttons are not shown (https://gettop.us/product/land-tee-jack-jones/)
    Given Open land-tee-jack-jones product page
    Then Verify "Out of Stock" sign is shown
    And Verify "Add to Cart" button is not shown
    And Verify "Checkout" button is not shown
