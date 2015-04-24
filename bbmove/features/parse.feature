# Created by Matthew at 22/04/2015
Feature: Parse filenames to determine TV Show metadata

  Scenario: It can determine the TV Show title
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I parse the files
     Then I should see the title "Castle"