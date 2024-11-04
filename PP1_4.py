'''
  Lesson: Input and F Strings
  Author: Helen Lin
  Date Created: September 19, 2024
  Date Last Modified: September 19, 2024
'''

def q1():
  #Write Assignment code here
  word = input("enter a word: ") 
  print (word)
  
def q2():
  #Write Assignment code here
  name = input("enter your name: ") 
  print ("your name is " + name) #prints name out

def q3():
  #Write Assignment code here
  firstname = input("enter your first name: ")
  lastname = input("enter your last name: ")

  word = f"your name is {firstname} {lastname}"
  print (word)
def q4():
  #Write Assignment code here
  student1 = input("input a student: ")
  student2 = input("input another student: ")

  word = f"your students are {student1} and {student2}"
  print(word)

#Do not edit code below this comment

# q1()
# q2()
# q3()
# q4()
