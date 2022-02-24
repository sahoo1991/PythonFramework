@smoke @jira_ticket_number
Feature: Launch Google And Search The Image

  @chrome
  Scenario: Search on google website and click the image
    Given the user opens google
    When the user clicks the image link on the home page
    Then user should see google image home page