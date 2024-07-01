print("Welcome to Quize Game")
Entry = input("Your Login Quize Game YES or NO :")
if Entry.upper() == "YES":
    print("Your Login Successfully...!")
else:
    quit()

Question_No_01 = input("Enter 'RAM' full form : ")

score = 0
if Question_No_01.upper() == "RANDOM ACCESS MEMORY":
    print("anser is correct...!")
    score += 1
else:
    print("answer is Incorrect...!")

Question_No_02 = input("Enter 'R0M' full form : ")

if Question_No_02.upper() == "READ ONLY MEMORY":
    print("anser is correct...!")
    score += 1
else:
    print("answer is Incorrect...!")

Question_No_03 = input("Enter 'CPU' full form : ")

if Question_No_03.upper() == "CENTRAL PROCESS UNIT":
    print("anser is correct...!")
    score += 1
    
else:
    print("answer is Incorrect...!")

Question_No_04 = input("Enter 'HD' full form : ")

if Question_No_04.upper() == "HARD DRIVE":
    print("anser is correct...!")
    score += 1
else:
    print("answer is Incorrect...!")

# Question_No_05 = input("Enter 'SD' full form : ")

# if Question_No_05.upper() == "STANDART DRIVE":
#     print("anser is correct...!")
#     score += 1
# else:
#     print("answer is Incorrect...!")

print("Totel Score :",score)
print("Score value", (score/4)*100)



