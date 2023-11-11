## Task 1: Software configuration
#### Subtask 1: Why I decided to take part in the [Dare IT Challenge](https://www.dareit.io/challenges/wstep-do-testow-automatycznych)?"
###### I decided to take part in the challenge to learn the basics of automated testing using Python and to create my own portfolio.
#### Subtask 4: 
###### The result of the first attempt at the test [GET ISTQB (Purpurowy)](https://getistqb.com/#quizzes): 10/14

## Task 2: Selectors
#### Subtask 2:
The purpose of this task is to analyze this [web page](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true) elements to create effective selectors


**login_field**
+ //*[@id="login"]
+ //*[@name="login"]
+ //*[text()="Login"]

**password_field**
+ //*[@id="password"]
+ //*[@name="password"]
+ //*[text()="Password"]

**remind_password_button**
+ //*[@id="__next"]/form/div/div[1]/a
+ //*[text()="Remind password"]
+ //child::div/a

**sign_in_button**
+ //button
+ //*[@type="submit"]
+ //*[@id="__next"]/form/div/div[2]/button

**drop_down_list**
+ //*[@id="__next"]/form/div/div[2]/div/div
+ //*[@role="button"]
+ /html/body/div/form/div/div[2]/div/div

**polish_language_option**
+ //*[@id="menu-"]/div[3]/ul/li[1]
+ //li[text()="Polski"]
+ //*[@data-value='pl']

**english_language_option**
+ //*[@id="menu-"]/div[3]/ul/li[2]
+ //*[@data-value="en"]
+ //li[text()="English"]



