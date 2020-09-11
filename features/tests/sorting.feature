# Created by andrei at 9/11/20
Feature: Sorting
  # Enter feature description here

  Scenario: User can sort products by price: high to low
    Given Open macbook Category page
    When Sort products on macbook Category page by price: high to low
    Then Verify products sorted by price: high to low

  Scenario: User can sort products by price: low to high
    Given Open macbook Category page
    When Sort products on macbook Category page by price: low to high
    Then Verify products sorted by price: low to high

  Scenario: User can sort products by popularity
    Given Open macbook Category page
    When Sort products on  macbook Category page by popularity
    Then Verify products on macbook Category page sorted by popularity

  Scenario: User can sort products by rating
    Given Open macbook Category page
    When Sort products on macbook Category page by rating
    Then Verify products on macbook Category page sorted by rating

  Scenario: User can sort products by latest
    Given Open macbook Category page
    When Sort products on macbook Category page by latest
    Then Verify products on macbook Category page sorted by latest