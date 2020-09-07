# Created by andrei at 9/2/20
Feature: Footer links
  # Enter feature description here

  Scenario: Footer shows Best Selling, Latest, Top Rated categories
    Given Open home page
    Then Verify footer shows Best Selling, Latest, Top Rated categories

  Scenario: All products in the footer have price, name, star-rating
    Given Open home page
    Then Verify All products in the footer have price, name, star-rating

  Scenario: "Copyright 2020" shown in footer
    Given Open home page
    Then Verify "Copyright 2020" shown in footer

  Scenario: Footer has button to go back to top
    Given Open home page
    Then Verify Footer has button to go back to top

  Scenario: Footer has working links to all product categories
    Given Open home page
    Then Verify Footer has working links to all product categories