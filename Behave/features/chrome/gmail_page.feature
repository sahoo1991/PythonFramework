@smoke @jira_ticket_number
Feature: Launch Google and Verify Gmail Link

  @chrome @testing
  Scenario: Verify Gmail Landing Page
    Given the user opens google
    When the user clicks the gmail link
    Then user should see the gmail inbox page