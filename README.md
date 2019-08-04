
# General Description of the project:
## Project Name: Math Game - Practice for Elementary School Students

## Goal: Answering correctly on as many exercises as possible
Each correct answer gives the user 1 point. By the end of the game he can see he’s\she’s location in the results table.

## Getting Started
This game requires basic knolaged at math :)

## Prerequisites
in order to play on your computer you need to have python 3.0 or above

Give examples
*TBD*

Give the example
*TBD*

Running the tests
Explain how to run the automated tests for this system

Break down into end to end tests
Explain what these tests test and why

Give an example
And coding style tests
Explain what these tests test and why

Give an example
Deployment
Add additional notes about how to deploy this on a live system

Built With
Dropwizard - The web framework used
Maven - Dependency Management
ROME - Used to generate RSS Feeds
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
We use *TBD* for versioning. For the versions available, see the tags on this repository.

# Authors
Lior Trieman  *See also the list of contributors who participated in this project.

# License
this project is not protected by any license

## Game Rules:
5 wrong answers or 3 wrong answers in a row– game over.
Chronological screens:
### 1.	Welcome screen – “Do you want to practice your math skills?”  Y/N
    a.	Y – “Please enter your: “name +age+ city of residence
    b.	N – “Have a nice day!”
### 2.	Game Rules explanation, to start the game press: “Y”
### 3.	possible demo questions – as an example
4.	questions’ screen: a math ex. Appears, for ex: 3+4 and a text box to give the answer and press Y. 
a.	a screen for indicating if the answer is correct and gives a “GOOD JOB!” notification on screen.
b.	a screen for wrong answer: “error…” and shows the right answer.
5.	Again questions… and repeat 4a & 4b
6.	“GAME OVER” screen after 3 wrong answers in a row or total 5 wrong answers.
7.	Table of results screen with the name of user in bold
8.	Goes back to welcome screen.

## Project design:
### Classes:
  1.	Table of results
    a.	Add user – according to his score result
    b.	Update score of user if the user already exists in the table?
  2.	Current User
    a.	Name – String
    b.	Age – int/float
    c.	City of residence - string
    d.	Number of correct answer/number of scores
    e.	Number of wrong answers – total (start with zero – goes until 5)
    f.	Number of wrong answers in a row (start with Zero until 3, and resets each time the user gives a correct answer)
  3.	Exercise:
    a.	-Questions - The SW choose randomly 2 numbers and an operator
    b.	-Right answer – the result of the exercise

 
# Appendix:

Open questions and possible features:
1.	How to divide the project to classes? – how to write it in a object oriented way?
2.	Limited time per question? Let say 1-2 minutes?
3.	How\where do I save results table? Google sheet? Else?
4.	Should I have a URL for my game? Or save it as an android app? Else?
5.	How can the user exit the game in the middle? Or pause the game if she\he needs a brake? 


  
# Acknowledgments
I want to thank SHECODES, expecialy the amazing team at google-campus (Tal, Noa & Miri!!!)
I would like also to thank my partner for being with our kids all the long hours of me coding...

Some __last words__ before you start playing my math game:
Always believe in youtself !

 



