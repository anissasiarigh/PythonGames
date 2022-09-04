print('Welcome to the Quiz Master')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What year did pluto go extinct?')
    if answer.lower()=='2006':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What is the largest planet in our solar system? ')
    if answer.lower()=='Jupitar':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: You have a bowl of 6 apples, you take away 4, how many do you have? ')
    if answer.lower()=='4':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Quiz master is totaling your score',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Goodbye!')