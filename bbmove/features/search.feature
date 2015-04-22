# Created by Matthew at 22/04/2015
Feature: Search for files and display their details
  # Enter feature description here

  Scenario: Search with a single file and see filename
    Given there are some files
      | filename           |
      | castle.e01.e02.mp4 |
     When I search for files
     Then I must see "castle.e01.e02.mp4"

  Scenario: Search non-video file and see filename
    Given there are some files
      | filename        |
      | not_a_movie.txt |
     When I search for files
     Then I must not see "not_a_movie.txt"

  Scenario: Search multiple video files and see all filenames
    Given there are some files
      | filename           |
      | castle.s01.e01.mp4 |
      | castle.s01.e02.mp4 |
     When I search for files
     Then I must see "castle.s01.e01.mp4"
      And I must see "castle.s01.e02.mp4"

  Scenario: Search looks through sub folders to find all video files
    Given there are some files
      | filename                      |
      | subfolder1/castle.s01.e01.mp4 |
      | subfolder2/castle.s01.e02.mp4 |
     When I search for files
     Then I must see "castle.s01.e01.mp4"
      And I must see "castle.s01.e02.mp4"