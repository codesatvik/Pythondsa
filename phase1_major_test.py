# PYTHON FOR DSA — PHASE 1 MAJOR TEST
# Name: ______________________
# Date: ______________________
#
# Instructions:
# 1. Solve independently. Do not look up answers while taking the test.
# 2. Write code wherever requested. Use clear variable names and indentation.
# 3. For output-prediction questions, write the EXACT output (including line breaks).
# 4. If unsure, attempt it anyway and add a comment explaining your thinking.
# 5. Save your completed file as: phase1_test_solved.py
# 6. Upload your solved file for grading.
#
# Total: 100 marks
# Suggested time: 90–120 minutes
#
# ============================================================
# PHASE 1 SUMMARY / QUICK REFERENCE (NOT ANSWERS TO THE TEST)
# ============================================================
#
# print(value)              -> displays output
# # comment                 -> comment
# variable = value          -> assignment
# type(value)               -> checks type
# int(), float(), str()     -> type conversion
# input("prompt")            -> reads input as a STRING
#
# Types: int, float, str, bool
# Boolean values: True, False (capitalized)
#
# Arithmetic:
# +  -  *  /  //  %  **
# /  -> normal division (usually float)
# // -> floor division
# %  -> remainder
# ** -> exponent/power
#
# Comparisons: == != > < >= <=
# Logical operators: and, or, not
#
# if condition:
#     ...
# elif condition:
#     ...
# else:
#     ...
#
# for item in range(start, stop, step):
#     ...
# range(stop) starts at 0 and excludes stop
#
# while condition:
#     ...
#     update condition variable!
#
# break    -> exits the loop
# continue -> skips current iteration
#
# def function(parameters):
#     ...
#     return value
#
# print() displays; return sends a value back to the caller.
# A function without an explicit return returns None.
#
# ============================================================
# SECTION A — OUTPUT PREDICTION (20 marks)
# Write exact output for each question. (2 marks each)
# ============================================================
#
# Q1.
# x = 7
# x = x + 3
# print(x)
# print("x")
#
# Your output:
# 10
# x

# Q2.
# a = "12"
# b = 3
# print(a + str(b))
# print(int(a) + b)
#
# Your output:
# 123
# 15

# Q3.
# print(17 // 4)
# print(17 % 4)
# print(2 ** 5)
#
# Your output:
# 4
# 1
# 32 

# Q4.
# x = 9
# if x > 10:
#     print("A")
# elif x > 5:
#     print("B")
# else:
#     print("C")
#
# Your output:
#  B
#
# Q5.
# for i in range(2, 8, 2):
#     print(i)
#
# Your output:
#  2 4 6 
#
# Q6.
# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 5:
#         break
#     print(i)
#
# Your output:
#   1 3 4 
#
# Q7.
# i = 3
# while i > 0:
#     print(i)
#     i -= 1
#
# Your output:3 2 1 
#
#
# Q8.
# def add(a, b):
#     return a + b
#
# result = add(4, 6)
# print(result)
# print(add(2, 3))
#
# Your output: 10
#  5
#
# Q9.
# def change(x):
#     x = x + 5
#     return x
#
# a = 10
# print(change(a))
# print(a)
#
# Your output:
#  15
#  10

# Q10.
# x = 8
# if x > 5 and x < 10:
#     print("YES")
# if x == 5 or x == 8:
#     print("OK")
# if not x == 8:
#     print("NO")
# else:
#     print("DONE")
#
# Your output: YES
#  OK
#  DONE

# ============================================================
# SECTION B — DEBUGGING (15 marks)
# Identify the mistake(s), then rewrite the corrected code. (3 marks each)
# ============================================================
#
# Q11. This should print 1, 2, 3, 4, 5.
# for i in range(1, 5):
#     print(i)
#
# Mistake and corrected code:
# for i in range(1,6):
#      print(i)

# Q12. This should print the sum of a and b.
# def add(a, b)
#     return a + b
#
# print(add(3, 4))
#
# Mistake and corrected code:
#  def add(a, b):
#      return a + b 
#  print(add(3,4))

# Q13. This should print 15 after asking the user for a number and adding 5.
# n = input("Enter a number: ")
# print(n + 5)
#
# Mistake and corrected code:
# n = int(input("Enter a number: "))
# print(n + 5)

# Q14. This loop should print 1, 2, 3 and stop.
# i = 1
# while i <= 3:
#     print(i)
#
# Mistake and corrected code:
# i = 1
# while i <= 3:
#    print(i)
#    i += 1

# Q15. This should print "Adult" when age is 18 or above.
# age = 20
# if age >= 18
#     print("Adult")
# else:
#     print("Minor")
#
# Mistake and corrected code:
# if age >= 18:
#      print("Adult")
# else:
#      print("Minor")
# ============================================================
# SECTION C — WRITE CODE YOURSELF (40 marks)
# Write complete working Python code for each. (5 marks each)
# ============================================================
#
# Q16. Create variables for your name, age, and height. Print each
# value and its type.
#
# Your code: name = "sam"
#   age = 20
#  height = 176
#  print(name)
# print(age)
# print(height)

# Q17. Ask the user for two integers. Print their sum, difference,
# product, and quotient (normal division).
#
# Your code: userinput1 = int(input("enter a number: "))
# userinput2 = int(input("enter another number: "))
#  print(userinput1 + userinput2)
#  print(userinput1 - userinput2)
# print(userinput1 * userinput2)
# print(userinput1 / userinput2)

# Q18. Ask the user for a number. Print whether it is even or odd.
# (Hint: remainder operator)
#
# Your code: user1 = int(input("a number: "))
# 
#   if user1 % 2 == 0:
 #   print("its a even number")
  # else:
  #  print("its a odd number")
#
#
# Q19. Ask the user for marks (0–100). Print:
# "A" for marks >= 90
# "B" for marks >= 75 and < 90
# "C" for marks >= 60 and < 75
# "Fail" for marks < 60
#
# Your code:
# usermarks = int(input("enter your marks: "))
# if usermarks >= 90:
#     print("A")
# elif usermarks >= 75 and usermarks < 90:
#     print("B")
# elif usermarks >= 60 and usermarks < 75:
#     print("C")
# else:
#     print("Fail")
#
#
# Q20. Use a for loop to print all numbers from 1 to 10.
#
# Your code: for i in range(1, 11):
#               print(i)
#
#
# Q21. Use a loop to calculate the sum of numbers from 1 to n.
# Ask the user for n. Example: n = 5 -> sum = 15.
#
# Your code: n = int(input("enter a number "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print(total)
#      
#     
#
#
# Q22. Print the multiplication table of a number entered by the user,
# from 1 to 10.
#
# Your code:
# n = int(input("enter a number"))
# 
# for i in range(1, 11):
#     print(i * n)
#     
#     
#
# Q23. Write a function called square(n) that returns n*n.
# Call it with 6 and print the result.
#
# Your code:def square(n):
#               return n*n
#   print(square(6))
#
# ============================================================
# SECTION D — FUNCTIONS & LOOP LOGIC (15 marks)
# ============================================================
#
# Q24. (5 marks)
# Write a function is_positive(n) that returns True if n > 0,
# otherwise False. Test it with at least two values.
#
# Your code: def is_positive(n):
#                if n > 0:
#                  return True
#                else: 
#                  return False
#print(is_positive(3))
#print(is_positive(-2))

# Q25. (5 marks)
# Write a function max_of_three(a, b, c) that returns the largest
# of three numbers WITHOUT using max().
#
# Your code:
# def max_of_three(a, b, c):
  #  largest = a
   # if b > largest:
    #    largest = b
    #if c > largest:
     #   largest = c
    #return largest
#print(max_of_three(10, 20, 15))
# Q26. (5 marks)
# Write code that prints numbers from 1 to 20, but:
# - skips multiples of 3
# - stops completely when it reaches 17
#
# Your code:
#  for i in range(1,21):
#       if i % 3 == 0:
#           continue
#       if i == 17:
#           break
#       print(i)

# ============================================================
# SECTION E — EXPLAIN IN YOUR OWN WORDS (10 marks)
# ============================================================
#
# Q27. (2 marks) Explain the difference between = and ==.
#
# Answer:
# = assigns value to variable 
# == checks if both valuse are same 
#
# Q28. (2 marks) Explain the difference between print() and return.
#
# Answer:
#  print() logs everything and return needs to called print to show output in terminal and return sends output to the function call element
#
# Q29. (2 marks) Explain the difference between break and continue.
#
# Answer: break stops the loop if it meets the requirenment and continue skips that element 
#
#
# Q30. (2 marks) What does input() return by default? How do you
# convert it to an integer?
#
# Answer: str , int(input())
#
#
# Q31. (2 marks) Why can a while loop become infinite? How can
# you prevent that?
#
# Answer: if there is not end statement to stop look it will run till infinite , by using break 
#
#
# ============================================================
# END OF PHASE 1 TEST
# ============================================================
# When finished, upload this file. I will:
# - run/check your code where possible,
# - grade each question and give a score out of 100,
# - explain errors and identify weak topics,
# - give targeted revision questions (including similar questions later),
# - decide whether you pass Phase 1 and can move forward quickly.
