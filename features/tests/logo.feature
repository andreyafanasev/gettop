# Created by andrei at 8/31/20
Feature: Get Top logo
  # Enter feature description here

  Scenario: GetTop logo is clickable and takes to https://gettop.us/
    Given Open home page
    When Click Logo
    Then Verify logo clickable and takes to https://gettop.us/