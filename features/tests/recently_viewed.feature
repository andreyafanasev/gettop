# Created by andrei at 9/11/20
Feature: User can see recently viewed items, open them and is taken to correct page
  # Enter feature description here

  Background:
    Given Open macbook-air product page

  Scenario: User can see recently viewed items
    When Open macbook Category page
    Then Verify User can see recently viewed item (Macbook Air)

  Scenario: User can open recently viewed items and is taken to correct page
    When Open macbook Category page
    And Click recently viewed item (Macbook Air)
    Then Verify MacBookAir page opens