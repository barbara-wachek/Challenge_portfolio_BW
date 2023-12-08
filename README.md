## Table of Contents 
* [Introduction](#introduction)
* [Task 1: Software configuration](#task-1-software-configuration)
* [Task 2: Selectors](#task-2-selectors)
* [Task 3: First automatic test and assertions](#task-3-first-automatic-test-and-assertions)
* [Task 4: Refactor, debugger and test cases](#task-4-refactor-debugger-and-test-cases)
* [Task 5: Robot Framework](#task-5-robot-framework)
* [Task 6: Bug reporting and test report](#task-6-bug-reporting-and-test-report)

## Introduction
This repository contains an automated testing environment for the [Scouts Panel website](https://scouts-test.futbolkolektyw.pl/login). This project was carried out as part of the [Dare IT Challenge](https://www.dareit.io/challenges/wstep-do-testow-automatycznych).

Other outputs of Challenge:
* [Manual test cases](https://docs.google.com/spreadsheets/d/1RCin82tfSesU4tCNpFl7ppMIG3XLe50hg9Kswb1hSpE/edit#gid=0) 
* [Automated tests in Robot Framework](https://github.com/barbara-wachek/panelscout_robotframework) 

## Task 1: Software configuration
Task goals: 
* perform exploratory tests of the application,
* find out what programs are necessary to start automatic testing,
* set up a remote repository on GitHub,
* clone the repository and configure the work environment,
* format the README file.

#### Subtask 1: Why I decided to take part in the [Dare IT Challenge](https://www.dareit.io/challenges/wstep-do-testow-automatycznych)?"
###### I decided to take part in the challenge to learn the basics of automated testing using Python and to create my own portfolio.
#### Subtask 4: 
###### The result of the first attempt at the test [GET ISTQB (Purpurowy)](https://getistqb.com/#quizzes): 10/14

## Task 2: Selectors
#### Subtask 2:
The purpose of this task is to analyze this [web page](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true) elements to create effective selectors.

**scouts_panel_text_xpath**
+ //h5
+ //*[@id="__next"]/form/div/div[1]/h5
+ //*[text()="Scouts Panel"]

**login_field_xpath**
+ //*[@id="login"]
+ //*[@name="login"]
+ //*[text()="Login"]
+ //child::div[1]/label

**password_field_xpath**
+ //*[@id="password"]
+ //*[@name="password"]
+ //*[text()="Password"]
+ //child::div[2]/label

**remind_password_button_xpath**
+ //*[@id="__next"]/form/div/div[1]/a
+ //*[text()="Remind password"]
+ //child::div/a

**sign_in_button_xpath**
+ //button
+ //*[@type="submit"]
+ //*[@id="__next"]/form/div/div[2]/button

**drop_down_list_xpath**
+ //*[@id="__next"]/form/div/div[2]/div/div
+ //*[@role="button"]
+ /html/body/div/form/div/div[2]/div/div

**polish_language_option_xpath**
+ //*[@id="menu-"]/div[3]/ul/li[1]
+ //li[text()="Polski"]
+ //*[@data-value='pl']

**english_language_option_xpath**
+ //*[@id="menu-"]/div[3]/ul/li[2]
+ //*[@data-value="en"]
+ //li[text()="English"]

## Task 3: First automatic test and assertions
## Task 4: Refactor, debugger and test cases
#### Test cases and test videos: https://drive.google.com/drive/folders/1lQEnFcOP7LvCqcQRDxyhBLe6o-JqOaJ3
## Task 5: Robot Framework
[Github repository](https://github.com/barbara-wachek/panelscout_robotframework)
## Task 6: Bug reporting and test report

