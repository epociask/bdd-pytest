Feature: Number Five Trivia 
  As a math addict, 
  I want to know an interesting fact about different numbers,
  So that I can build my numeric correlation trivia.


  Scenario Outline: Numbers API Trivia Query
    When the Numbers API is queried with "<number>"
    Then the response status code is 200
    And the response has the number "<number>"

    Examples: Trivia
      | number | 
      | 1 | 
      | 4 |
      | 5 | 