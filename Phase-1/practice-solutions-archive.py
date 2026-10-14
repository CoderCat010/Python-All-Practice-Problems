# ========== TASK: 1 =========> 
# pocketMoney = 2500
# coachingDays = 12
# rickshawPerTrip = 60
# lunchParDay = 80 

# totalSpent = (lunchParDay * 12) + (rickshawPerTrip * 12)
# remaining = pocketMoney - totalSpent
# averagPerDay = lunchParDay + rickshawPerTrip
# print('Total Spent:', totalSpent)
# print('Remaining:', remaining)
# print('Average Per Day:', averagPerDay)



# ========== TASK: 2 ==========> 
# bangla = 72
# english = 65
# math = 91

# totalMarks = bangla + english + math 
# totalPerMarks = totalMarks / 3
# condition = totalPerMarks > 40 
# print(totalMarks)
# print(totalPerMarks)
# print('Paased:',condition)



# ========== TASK: 3 ==========> 
# A = 'Milk'
# B = 'Juice'
# C = B
# B = A
# A = C

# # print(C)
# # print(D)
# print(A)
# print(B)



# ========== TASK: 4 ==========> 
# name = "rahim"
# # error -> 1
# # name[0] = "R" # string is immutable so we cant change substring of a string
# # fixed
# name = name.capitalize() # so we simpley used this instead of breaking the rule of string mutability

# # error -> 2
# # age = input("Tomar boyosh koto? ") # input() always returns a string by default, so we have to convert it to int first. Otherwise it will stay a string, and for that in next line of code age + 1 fails because age is still a string.
# # fixed
# age = int(input("Tomar boyosh koto? ")) 
# next_year = age + 1 

# # error -> 3
# # print("Hello " + name + ", next year age: " + next_year) # it seems we wanted to concatenate int with str but we can't concatenate int type with string in python so that python throws an error that int and str cant be concatinate. 
# # fixed
# print("Hello", name+',', "next year age:", next_year) # so we used comma for puttting every part in one line instead of using plus sign.



# ========== TASK: 5 ==========> 
# firstName = '     RAFI'
# lastName = 'Ahmed'
# rollNo = 21

# studentUserName = f'{firstName}.{lastName}.{rollNo}'.replace(' ', '').lower()
# studentEmailAddress = f'{studentUserName}@school.edu'
# print('email:', studentEmailAddress)
# print('username:', studentUserName)
# print(len(studentUserName))
# print(firstName) 



# ========== TASK: 6 ==========> 
# # error: 1
# quantity = input("কয়টা কলম: ") # input() always returns a string by default, so we have to convert it to int first. Otherwise it will stay a string, and for that in next line of code fails because quantity is still a string. 
# # fixed
# quantity = int(input("কয়টা কলম: "))
# print("তুমি পাবে", quantity * 3, "টা খাতা")

