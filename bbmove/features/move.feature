# Created by Matthew at 26/04/2015
Feature: Moving a file to the tv_show folder

  Scenario: Moving a file from one location to another
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
     When I move the files
     Then I must see "castle.s01.e02.mp4" in the tv show folder

  Scenario: Moving a several files from one location to another
    Given there are some files
      | filename           |
      | castle.s01.e02.mp4 |
      | the.walking.dead.s01.e02.mp4 |
     When I move the files
     Then I must see "castle.s01.e02.mp4" in the tv show folder
      And I must see "the.walking.dead.s01.e02.mp4" in the tv show folder

  Scenario: Moving a several files from subfolders to another
    Given there are some files
      | filename                                |
      | subfolder1/castle.s01.e02.mp4           |
      | subfolder2/the.walking.dead.s01.e02.mp4 |
     When I move the files
     Then I must see "castle.s01.e02.mp4" in the tv show folder
      And I must see "the.walking.dead.s01.e02.mp4" in the tv show folder