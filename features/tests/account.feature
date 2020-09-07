# Created by andrei at 9/1/20
Feature: Account
  # Enter feature description here

  Scenario: Clicking on Account icon opens Login form
    Given Open home page
    When Click Account icon
    Then Verify Login form opens