# Created by andrei at 8/28/20
Feature: Top Banner functionality
  # Enter feature description here

  Scenario: User can click right and left arrows to see top banners;
    Given Open home page
    Then Verify that user can click right arrow
    And Verify that user can click left arrow


  Scenario: User can click bottom dots to see top banners
    Given Open home page
    Then Verify that user can click bottom dots to see top banners


  Scenario: User can click on product banner and is taken to correct category page 1
    Given Open home page
    When Click on banner 1
    Then Verify if taken to correct category page - IPAD


  Scenario: User can click on product banner and is taken to correct category page 2
    Given Open home page
    When Click on banner 2
    Then Verify if taken to correct category page - MACBOOK