# Created by andrei at 8/29/20
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: "Browse Our Categories" text is shown
    Given Open home page
    Then Verify "Browse Our Categories" text is shown

  Scenario: 4 correct categories are shown
    Given Open home page
    Then Verify 4 correct categories are shown

  Scenario: Upon clicking on each category, correct page opens
    Given Open home page
    When Click ACCESSORIES category
    Then Verify ACCESSORIES page opens

  Scenario: Upon clicking on each category, correct page opens
    Given Open home page
    When Click IPAD category
    Then Verify IPAD page opens

  Scenario: Upon clicking on each category, correct page opens
    Given Open home page
    When Click IPHONE category
    Then Verify IPHONE page opens

  Scenario: Upon clicking on each category, correct page opens
    Given Open home page
    When Click MACBOOK category
    Then Verify MACBOOK page opens