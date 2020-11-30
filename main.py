# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
new_name1 = name1.lower()
new_name2 = name2.lower()
name1_t = (new_name1.count("t"))
name1_r = (new_name1.count("r"))
name1_u = (new_name1.count("u"))
name1_e = (new_name1.count("e") * 2)
name1_true = name1_t + name1_r + name1_u + name1_e
name1_l = (new_name1.count("l"))
name1_o = (new_name1.count("o"))
name1_v = (new_name1.count("v"))
name1_love = name1_l + name1_o + name1_v
name1_total = str(name1_true) + str(name1_love)
name2_t = (new_name2.count("t"))
name2_r = (new_name2.count("r"))
name2_u = (new_name2.count("u"))
name2_e = (new_name2.count("e") * 2)
name2_true = name2_t + name2_r + name2_u + name2_e
name2_l = (new_name2.count("l"))
name2_o = (new_name2.count("o"))
name2_v = (new_name2.count("v"))
name2_love = name2_l + name2_o + name2_v
name2_total = str(name2_true) + str(name2_love)
score = int(name1_total) + int(name2_total)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score} .")
