# Created by Matthew at 26/04/2015
Feature: Regular expression read the filename

  Scenario: It can parse the s01e02 filename type
    Given there are some files
      | filename          |
      | castle.s01e02.mp4 |
    When I parse the files
     Then I must see the title "Castle"
     Then I must see the season number "1"
     Then I must see the episode number "2"

  Scenario: It can parse the s01.e02 filename type
    Given there are some files
      | filename          |
      | castle.s01.e02.mp4 |
    When I parse the files
     Then I must see the title "Castle"
     Then I must see the season number "1"
     Then I must see the episode number "2"

  Scenario: It can parse the 102 filename type
    Given there are some files
      | filename          |
      | castle.102.mp4 |
    When I parse the files
     Then I must see the title "Castle"
     Then I must see the season number "1"
     Then I must see the episode number "2"