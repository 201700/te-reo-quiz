#Base quiz learning code

#importing the random libary
import random

#globals and  questions lists
score = 0
english = ["computer", "Lake", "food","test"]
right_answer = ["rorohiko", "roto", "kai", "Test"]
option_1 = ["wrong Answer", "Wrong Answer", "wrong answer", "Test"]
option_2 = ["wrong Answer", "Wrong Answer", "wrong answer", "Test"]

#define a function to generate a question
def generate_question(english, right_answer, option_1, option_2):
 global score
 print("what is the correct  word for", english, "in maori")
#generate a random number to determine the sequence of questions
random_sequence = random.randint(0,2)
#seperate print statements for readability 
if(random_sequence == 0):
 print("A", option_1)
 print("B", option_2)
 print("c", right_answer)
 answer = input().lower()
 if answer == "C":
   score += 1
 else:
   print("incorrect.")
elif(random_sequence == 1):
  print("A, option_1")
  print("B", right_answer)
  print("C", option_2)
  answer = input().lower()
  if answer == "B":
   score += 1
  else:
   print("incorrect.")
elif(random_sequence == 2):
  print("A, right_answer")
  print("B", option_2)
  print("C", option_1)
  answer = input().lower()
  if answer == "A":
   score += 1
  else:
   print("incorrect.")

#generate 3 questions pulling possoble answers from lists.
for i in range(0, 3):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])
#print the score at the end of the quiz
print(score)
