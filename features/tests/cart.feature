# Created by andrei at 9/1/20
Feature: Cart
  # Enter feature description here

  Scenario: Clicking on Cart icon opens Empty Cart page if no products were added
    Given Open home page
    When Click cart icon
    Then Verify Empty cart page opens

  Scenario: Hovering over empty cart icon shows "No products in the cart." message
    Given Open home page
    When Hover over Cart icon
    Then Verify "No products in the cart." message is shown

  Scenario: Add product to cart, verify that price in top nav menu is correct
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Click cart icon
    Then Verify that price in top nav menu is correct

  Scenario: Add products to cart, verify that amount of items shown in top nav menu are correct
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    Then Verify that amount of items shown in top nav menu are correct

  Scenario: Add products to cart, hover over cart icon, verify correct products and subtotal shown
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Hover over Cart icon
    Then Verify correct product - "iPad mini" and subtotal shown

  Scenario: Add products to cart, hover over cart icon, verify user can click on "View Cart" and is taken to cart page
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Hover over Cart icon
    And Click VIEW CART button
    Then Verify cart page is open

  Scenario: Add products to cart, hover over cart icon, verify user can click on "Checkout" and is taken to checkout page
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Hover over Cart icon
    And Click CHECK OUT button
    Then Verify CHECK OUT page is open

  Scenario: Add a product to cart, hover over cart icon, verify user can remove a product
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Hover over Cart icon
    And Click REMOVE BTN [X]
    Then Verify "No products in the cart." message is shown