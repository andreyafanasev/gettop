# Created by andrei at 9/11/20
Feature: Browse
  # Enter feature description here

  Scenario: User sees correct categories under Browse
    Given Open accessories Category page
    Then Verify user sees correct categories under Browse

  Scenario: User can click on categories under Browse and correct page opens
    Given Open accessories Category page
    Then Verify user can click on categories under Browse and correct page opens