# Created by andrei at 8/28/20
Feature: Latest on Sale


  Scenario: "Latest Products on Sale" text is shown
    Given Open home page
    Then Verify that LATEST PRODUCTS ON SALE text is shown

  Scenario: Every product has Sale icon, image, product category, name, price, and star-rating
    Given Open home page
    Then Verify Every product has Sale icon, image, product category, name, price, and star-rating

  Scenario: User can click on heart icon to add to wishlist
    Given Open home page
    Then Hover over product, click on heart icon to add to wishlist
    # I built 1 TC for all 4 products, used sleep because played with EC and didn't find right solution,
    #  got exception

  Scenario: User can open product from Sale and add it to cart
    Given Open home page
    When Click on product "MacBook Pro 13-inch" on sale
    And Click add to cart button
    And Open the cart
    Then Verify "MacBook Pro 13-inch" added to cart

  Scenario: User can open product from Sale and add it to cart
    Given Open home page
    When Click on product "iPhone SE" on sale
    And Click add to cart button
    And Open the cart
    Then Verify "iPhone SE" added to cart

  Scenario: User can open product from Sale and add it to cart
    Given Open home page
    When Click on product "iPad mini" on sale
    And Click add to cart button
    And Open the cart
    Then Verify "iPad mini" added to cart

  Scenario: User can open product from Sale and add it to cart
    Given Open home page
    When Click on product "Watch Series 5" on sale
    And Click add to cart button
    And Open the cart
    Then Verify "Watch Series 5" added to cart

  Scenario: User can open product from Sale and see product price and description
    Given Open home page
    When Click on product "MacBook Pro 13-inch" on sale
    Then Verify "MacBook Pro 13-inch" has price
    And Verify "MacBook Pro 13-inch" has description

  Scenario: User can open product from Sale and see product price and description
    Given Open home page
    When Click on product "iPhone SE" on sale
    Then Verify "iPhone SE" has price
    And Verify "iPhone SE" has description


  Scenario: User can open product from Sale and see product price and description
    Given Open home page
    When Click on product "iPad mini" on sale
    Then Verify "iPad mini" has price
    And Verify "iPad mini" has description

  Scenario: User can open product from Sale and see product price and description
    Given Open home page
    When Click on product "Watch Series 5" on sale
    Then Verify "Watch Series 5" has price
    And Verify "Watch Series 5" has description

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open home page
    When Hover over "MacBook Pro 13-inch"
    And Click Quick view "MacBook Pro 13-inch"
    Then Verify Quick view is open
    When Click X to close Quick view
    Then Verify Quick view closed

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open home page
    When Hover over "iPhone SE"
    And Click Quick view "iPhone SE"
    Then Verify Quick view is open
    When Click X to close Quick view
    Then Verify Quick view closed
#
  Scenario: User can open and close Quick View by clicking on closing X
    Given Open home page
    When Hover over "iPad mini"
    And Click Quick view "iPad mini"
    Then Verify Quick view is open
    When Click X to close Quick view
    Then Verify Quick view closed
#
  Scenario: User can open and close Quick View by clicking on closing X
    Given Open home page
    When Hover over "Watch Series 5"
    And Click Quick view "Watch Series 5"
    Then Verify Quick view is open
    When Click X to close Quick view
    Then Verify Quick view closed

  Scenario: User can click Quick View and add product to cart
    Given Open home page
    When Hover over "MacBook Pro 13-inch"
    And Click Quick view "MacBook Pro 13-inch"
    And Click add to cart button
    And Open the cart
    Then Verify "MacBook Pro 13-inch" added to cart

  Scenario: User can click Quick View and add product to cart
    Given Open home page
    When Hover over "iPhone SE"
    And Click Quick view "iPhone SE"
    And Click add to cart button
    And Open the cart
    Then Verify "iPhone SE" added to cart

  Scenario: User can click Quick View and add product to cart
    Given Open home page
    When Hover over "iPad mini"
    And Click Quick view "iPad mini"
    And Click add to cart button
    And Open the cart
    Then Verify "iPad mini" added to cart

  Scenario: User can click Quick View and add product to cart
    Given Open home page
    When Hover over "Watch Series 5"
    And Click Quick view "Watch Series 5"
    And Click add to cart button
    And Open the cart
    Then Verify "Watch Series 5" added to cart

  Scenario: User can click Quick View and click through product images
    Given Open home page
    When Hover over "MacBook Pro 13-inch"
    And Click Quick view "MacBook Pro 13-inch"
    Then Verify that click through "MacBook Pro 13-inch" images

  Scenario: User can click Quick View and click through product images
    Given Open home page
    When Hover over "iPhone SE"
    And Click Quick view "iPhone SE"
    Then Verify that click through "iPhone SE" images

  Scenario: User can click Quick View and click through product images
    Given Open home page
    When Hover over "iPad mini"
    And Click Quick view "iPad mini"
    Then Verify that click through "iPad mini" images

  Scenario: User can click Quick View and click through product images
    Given Open home page
    When Hover over "Watch Series 5"
    And Click Quick view "Watch Series 5"
    Then Verify that click through "Watch Series 5" images