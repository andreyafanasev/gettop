# Created by andrei at 9/4/20
Feature: Product
  # Enter feature description here

  Scenario: Product (MacBook Air) has image, name, price, description
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    Then Verify product (MacBook Air) has image, name, price, description

  Scenario: User can zoom in product image, scroll thru images and close them (by clicking X)
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Zoom button
    Then Verify User can scroll through images
    When Click [x] to close images
    Then Verify images closed

  Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Hover over MAC picture
    And Click on the heart icon
    Then Verify product added to wishlist(message "Product added!" shown)

  Scenario: "Home" link takes user to Home Page
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Logo
    Then Verify logo clickable and takes to https://gettop.us/

  Scenario: Category link (MacBook) takes users to correct category page
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click category "Macbook" link
    Then Verify MACBOOK page opens

  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    Then Verify Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn

  Scenario: Clicking on a social network (Facebook) link opens a new window to login to social network
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Facebook link
    Then Verify a new window to login to Facebook opens

  Scenario: Clicking on a social network (Twitter) link opens a new window to login to social network
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Twitter link
    Then Verify a new window to login to Twitter opens

  Scenario: Clicking on a social network (Email) link opens a new window to login to social network
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Email link
    Then Verify a new window to login to Email opens

  Scenario: Clicking on a social network (Pinterest) link opens a new window to login to social network
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click Pinterest link
    Then Verify a new window to login to Pinterest opens

  Scenario: Clicking on a social network (LinkedIn) link opens a new window to login to social network
    Given Open home page
    When Hover over MAC
    And Click MacBookAir link
    And Click LinkedIn link
    Then Verify a new window to login to LinkedIn opens