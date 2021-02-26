Feature: Beer API Beer Data
  As a beer drinker, 
  I want to get the ph content in a beer,
  So that I know the acidity level of what I drink.


  Scenario Outline: Beer API Single Beer Info
    When the Beer API is queried with body: "<beer_id>"
    Then the response status code is 200
    And the response shows PH content of "<beer_ph>"

    Examples: Trivia
      | beer_id      | beer_ph |
      | 1            | 4.4     |
      | 2            | 4.4     |
      | 3            | 3.2     | 
      | 4            | 4.4     |