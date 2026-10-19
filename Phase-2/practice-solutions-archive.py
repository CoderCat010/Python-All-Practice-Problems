# ========== TASK: 1 ==========>
# days = int(input('how many days? '))
# free_days = 3
# fine_per_day = 5
# max_fine = 100
# fine_days = days - free_days
# fine = fine_days * fine_per_day
# if fine < 0:
#     fine = 0
# elif fine > max_fine:
#     fine = max_fine
# print('জরিমানা:', fine, 'টাকা')


# ========== TASK: 2 ==========>
# balance = int(input('Balance? ',))
# withdraw = int(input('Enter Withdraw Amount: '))
# remaining = balance - withdraw
# min_withdraw = 500
# max_withdraw = 20000
# if withdraw < min_withdraw or withdraw % 500 != 0:
#     print('Invalid amount: must be a multiple of 500 (minimum 500)')
# elif withdraw > max_withdraw:
#     print('Limit exceeded: maximum 20000 per withdrawal')
# elif withdraw > balance:
#     print('Insufficient balance')
# else:
#     print(f'withdrawn: {withdraw}  Remaining balance: {remaining}')


# ========== TASK: 3 ==========>
# i = 6
# while i > 1:
#     i -= 1
#     if i == 2:
#         print('')
#         continue
#     print(i)
#     if i == 1:
#         print('লিফট-অফ!')


# ========== TASK: 4 ==========>
# total_marks = 0
# count = 0
# while count < 5:
#     marks = int(input("নম্বর: "))
#     total_marks = total_marks + marks
#     count += 1
# print("Total:", total_marks)


# ========== TASK: 5 ==========>
rightPin = 4829
count = 1
while count <= 3:
    userPin = int(input("Enter Your Pin: "))
    if userPin != rightPin and count == 1:
        print("ভুল পিন। আর 2 বার চেষ্টা করতে পারবে।")
    elif userPin != rightPin and count == 2:
        print("ভুল পিন। আর 1 বার চেষ্টা করতে পারবে।")
    elif userPin != rightPin and count == 3:
        print("ভুল পিন। আর চেষ্টা করতে পারবেন না।")
        break
    else:
        print("স্বাগতম!")
    count += 1
