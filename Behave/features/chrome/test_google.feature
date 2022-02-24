@smoke @jira_ticket_number @testing
Feature: Launch Google and search some text

  @chrome
  Scenario: Search on google website
    Given the user opens google
    When the user searches with the string Testing
    Then user should see some results populated
