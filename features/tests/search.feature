# Created by andrei at 8/31/20
Feature: Search

  Scenario: User can search for existing product and sees correct results
    Given Open home page
    When Hover over Search icon
    And Enter "IPHONE" in search field
    And Click Submit search
    Then Verify "IPHONE" presented

  Scenario: User can search for non-existing product and sees "No products were found matching your selection."
   Given Open home page
    When Hover over Search icon
    And Enter "DRESS" in search field
    And Click Submit search
    Then Verify "No products were found matching your selection" text presented