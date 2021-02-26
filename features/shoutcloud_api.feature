Feature: Shout cloud API Title Casing 
  As a lower case hater, 
  I want to title case words,
  So that I can only have upper case.


  Scenario Outline: Shout Upper Case Query
    When the shout API is queried with body: "<string>"
    Then the response status code is 200
    And the response has the upper cased string "<string>" as output

    Examples: Trivia
      | string      |
      | hello world | 
      | golang      | 
      | fuck school |
      | hardworking student | 