'''
  Lesson: Input and F Strings
  Author: Helen Lin
  Date Created: September 19, 2024
  Date Last Modified: September 19, 2024
'''

def q1():
  #Write Assignment code here
  word = input("Input a word: ") 
  print(word)
  
def q2():
  #Write Assignment code here
  name = input("Input your first name: ") 
  print("Your name is " + name) #prints name out

def q3():
  #Write Assignment code here
  firstname = input("Input your first name: ")
  lastname = input("Input your last name: ")

  word = f"your name is {firstname} {lastname}"
  print(word)

def q4():
  #Write Assignment code here
  student1 = input("Input a student: ")
  student2 = input("Input another student: ")

  word = f"your students are {student1} and {student2}"
  print(word)

#Do not edit code below this comment

#q1()
#q2()
#q3()
#q4()
