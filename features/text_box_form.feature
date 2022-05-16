Feature: Log utility


Background:
  Given that a User is opened text box page

  @implemented
  Scenario: User wants to add an entry with all inputted fields
    When a user inputs full name
    And a user inputs valid email
    And a user inputs current address
    And a user inputs permanent address
    And a user clicks on the submit button
    Then an entry will be added


  Scenario: User wants to add an entry without a name value
    When a user inputs valid email
    And a user inputs current address
    And a user inputs permanent address
    And a user clicks on the submit button
    Then an entry will be added without name value


  Scenario: User wants to add an entry without an email value
    When a user inputs full name
    And a user inputs current address
    And a user inputs permanent address
    And a user clicks on the submit button
    Then an entry will be added without an email value


  Scenario: User wants to update an added value
    When a user inputs full name
    And a user inputs valid email
    And a user inputs current address
    And a user inputs permanent address
    And a user clicks on the submit button
    Then an entry will be added
    When a user inputs new full name value
    And a user clicks on the submit button
    Then the new added value is shown
