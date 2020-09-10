# Created by andrei at 9/8/20
Feature: You may also like
  # Enter feature description here

  Scenario: "You may also like…" bock is shown and contains products
    Given Open macbook-air product page
    Then Verify "You may also like…" bock is shown
    And Verify "You may also like…" bock contains products

  Scenario: Product links under "You may also like…" block are clickable and take to correct pages
    Given Open macbook-air product page
    When Click MacBook Pro 16 inch product link
    Then Verify MacBook Pro 16 inch product page opens

  Scenario: Product links under "You may also like…" block are clickable and take to correct pages
    Given Open macbook-air product page
    When Click MacBook Pro 13 inch product link
    Then Verify MacBook Pro 13 inch product page opens

