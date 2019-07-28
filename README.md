General Description of the project:
Project Name: Math Game - Practice for Elementary School Students
Goal: Answering correctly on as many exercises as possible
Each correct answer gives the user 1 point. By the end of the game he can see he’s\she’s location in the results table.
Game Rules:
5 wrong answers or 3 wrong answers in a row– game over.
Chronological screens:
1.	Welcome screen – “Do you want to practice your math skills?”  Y/N
a.	Y – “Please enter your: “name +age+ city of residence
b.	N – “Have a nice day!”
2.	Game Rules explanation, to start the game press: “Y”
3.	possible demo questions – as an example
4.	questions’ screen: a math ex. Appears, for ex: 3+4 and a text box to give the answer and press Y. 
a.	a screen for indicating if the answer is correct and gives a “GOOD JOB!” notification on screen.
b.	a screen for wrong answer: “error…” and shows the right answer.
5.	Again questions… and repeat 4a & 4b
6.	“GAME OVER” screen after 3 wrong answers in a row or total 5 wrong answers.
7.	Table of results screen with the name of user in bold
8.	Goes back to welcome screen.

Project design:
Classes:
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




UML Class Diagram (first try😊
User/Player
user_name : string
user_age : Double= 0.0
user_city : string
new_user_info (user_name, user_age, user_city)

User_score/Player_score
User_score : int

Add_point (user_score, answer { if the user answered correctly)

User_errors/Player_errors

Num_total_errors : int {after 5 error it is ‘game over’} = 0
Num_errors_in_a_row : int { three errors is a row is ‘game over’} = 0


Count_errors (Num_errors_in_a_row , Num_total_errors , answer)

Answer 

Answer : bool
Update_current_answer (Exersize)


Game_over 

Is_game_over : bool
Show_game_over_screen (Is_game_over)


Exersize

Numer_1 : int
Number_2 : int
Ex_Operater: ?

Random_ex(number_1, number_2, ex_operator)

Result_Table
Winner : String  (?)
Second_place : string
Third_place: string
….
Last_place : string
Add_player(TBD)


 
Appendix:

Open questions and possible features:
1.	How to divide the project to classes? – how to write it in a object oriented way?
2.	Limited time per question? Let say 1-2 minutes?
3.	How\where do I save results table? Google sheet? Else?
4.	Should I have a URL for my game? Or save it as an android app? Else?
5.	How can the user exit the game in the middle? Or pause the game if she\he needs a brake? 


  
 


4.	
