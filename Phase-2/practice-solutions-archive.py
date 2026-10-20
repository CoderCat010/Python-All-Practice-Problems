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
# rightPin = 4829
# count = 1
# while count <= 3:
#     userPin = int(input("Enter Your Pin: "))
#     if userPin != rightPin and count == 1:
#         print("ভুল পিন। আর 2 বার চেষ্টা করতে পারবে।")
#     elif userPin != rightPin and count == 2:
#         print("ভুল পিন। আর 1 বার চেষ্টা করতে পারবে।")
#     elif userPin != rightPin and count == 3:
#         print("ভুল পিন। আর চেষ্টা করতে পারবেন না।")
#         break
#     else:
#         print("স্বাগতম!")
#     count += 1



# ========== TASK: 6 ==========>
# students = int(input("কতজন ছাত্র: "))
# regular = 0
# fined = 0
# count = 1
# while count <= students:
#     attendance = int(input("উপস্থিতি %: "))
#     has_medical = input("মেডিকেল সার্টিফিকেট (yes/no): ")
#     if attendance >= 75:
#         print("ছাত্র", count, ": পরীক্ষায় বসতে পারবে")
#         regular = regular + 1
#     elif (attendance >= 60 and attendance <= 74) and has_medical == "yes":
#         print("ছাত্র", count, ": জরিমানাসহ বসতে পারবে")
#         fined = fined + 1
#     else:
#         print("ছাত্র", count, ": বসতে পারবে না")
#     count = count + 1
# print("সাধারণ:", regular, "| জরিমানাসহ:", fined)



# ========== TASK: 7 ==========>



# ========== TASK: 8 ==========>



# ========== TASK: 9 ==========>



# ========== TASK: 10 ==========>
estimate_mb = 1000
days = 7
count = 1
total_mb = 0
cross_day = None
highest_mb = 0
highest_day = None

while count <= days:
    user_input = int(input('Enter Usage Data: '))
    total_mb = total_mb + user_input
    if total_mb > estimate_mb and cross_day is None:
        cross_day = count
        if cross_day is not None:
            print(f"Limit ({estimate_mb} MB) cross হয়েছে দিন {cross_day}-এ")
    if user_input > highest_mb:
        highest_mb = user_input
        highest_day = count
    count += 1
average_mb = total_mb / days

if cross_day is None:
    print(f"Limit ({estimate_mb} MB) cross হয়নি")
else:
    print(f"Limit ({estimate_mb} MB) cross হয়েছে দিন {cross_day}-এ")
print(f"Total usage: {total_mb} MB")
print(f"Highest: দিন {highest_day} ({highest_mb} MB)")
print(f"Daily average: {average_mb:.2f} MB")