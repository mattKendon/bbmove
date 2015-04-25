# Created by Matthew at 25/04/2015
Feature: It can determine the tree structure for the TV Show

  Scenario: It can determine the TV Show folder name
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
      | the.walking.dead.s01.e02.mp4 |
     When I parse the files
     Then I must see the tv show folder name "castle"
      And I must see the tv show folder name "walking_dead"

    Scenario: It can determine the Season folder name
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I parse the files
     Then I must see the season folder name "season_01"

    Scenario: It can determine the full folder tree
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I parse the files
     Then I must see the folder tree "castle/season_01"


