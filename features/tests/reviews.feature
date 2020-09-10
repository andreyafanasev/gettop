# Created by andrei at 9/8/20
Feature: Reviews
  # Enter feature description here

  Scenario: User can submit a review
    Given Open macbook-air product page
    When Click review top link
    And Click 5-star review link
    And Fill out review form (review, name, email)
    And Click SUBMIT button
    Then Verify review is shown

  Scenario: Correct amount of product reviews are shown
    Given Open macbook-air product page
    When Click review top link
    Then Verify correct amount of product (MacBook Air) reviews are shown