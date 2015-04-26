# Created by Matthew at 26/04/2015
Feature: The command line script
  # Enter feature description here

  Scenario: searching with the command line script
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the search command
     Then I must find "castle.s01.e02.mp4" in the results

  Scenario: Command line search prints out the Show name
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the search command
     Then I must find "Show:        Castle" in the results

  Scenario: Command line search prints out the Season number
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the search command
     Then I must find "Season:      1" in the results

  Scenario: Command line search prints out the Episode number
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the search command
     Then I must find "Episode:     2" in the results

  Scenario: Command line search prints out the Destination path
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the search command
     Then I must find "Destination: castle\season_01\castle.s01.e02.mp4" in the results

  Scenario: Command line move will move files
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I run the move command
     Then I must see "castle.s01.e02.mp4" in the tv show folder