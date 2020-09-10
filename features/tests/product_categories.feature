# Created by andrei at 9/1/20
Feature: Product categories
  # Enter feature description here

  Scenario: User can hover over Mac and see correct menu options
    Given Open home page
    When Hover over MAC
    Then Verify correct menu options for MAC presented

  Scenario: User can hover over iPhone and see correct menu options
    Given Open home page
    When Hover over iPhone
    Then Verify correct menu options for iPhone presented

  Scenario: User can hover over iPad and see correct menu options
    Given Open home page
    When Hover over iPad
    Then Verify correct menu options for iPad presented

  Scenario: User can hover over Watch and see correct menu options
    Given Open home page
    When Hover over Watch
    Then Verify correct menu options for Watch presented

  Scenario: User can hover over Accessories and see correct menu options
    Given Open home page
    When Hover over Accessories
    Then Verify correct menu options for Accessories presented

  Scenario: User can select Mac product from top menu and correct page opens
    Given Open home page
    When Hover over Mac
    And Click MacBookAir link
    Then Verify MacBookAir page opens

  Scenario: User can select iPhone product from top menu and correct page opens
    Given Open home page
    When Hover over iPhone
    And Click iPhone 11 Pro link
    Then Verify iPhone 11 Pro page opens

  Scenario: User can select iPad product from top menu and correct page opens
    Given Open home page
    When Hover over iPad
    And Click iPad Pro link
    Then Verify iPad Pro page opens

  Scenario: User can select Watch product from top menu and correct page opens
    Given Open home page
    When Hover over Watch
    And Click Watch Series 5 link
    Then Verify Watch Series 5 page opens

  Scenario: User can select Accessories product from top menu and correct page opens
    Given Open home page
    When Hover over Accessories
    And Click AirPods Pro link
    Then Verify AirPods Pro page opens