# Created by andrei at 9/11/20
Feature: Filter
  # Enter feature description here

  Scenario: User can filter products by price
    Given Open macbook Category page
    When Slide left dot of the price slider 50% to the right
    And Apply filter (Click Filter btn)
    Then Verify correct products for category macbook (after filter applying) are presented

  Scenario: User can reset price filter after they were applied
    Given Open macbook Category page
    When Slide left dot of the price slider 50% to the right
    And Apply filter (Click Filter btn)
    Then Verify correct products for category macbook (after filter applying) are presented
    When Reset price filter
    Then Verify correct products for category macbook (after filter reset) are presented

  Scenario: "No products were found matching your selection." message shown if no products match selected filters
    Given Open macbook Category page
    When Slide left dot of the price slider 100% to the right
    And Apply filter (Click Filter btn)
    Then Verify "No products were found matching your selection." message shown