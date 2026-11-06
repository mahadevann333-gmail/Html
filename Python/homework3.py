Is_Logged_in = True 
Is_Subscribed = False

# Initialize credits
user_credits = 100
max_credits = 200
min_credits = 50

# check valid credit range
Credits_valid =(user_credits >= min_credits and
                user_credits <= max_credits and
                user_credits != min_credits)

# Check bonus eligibility
Bonus_eligible = Is_Subscribed or not (user_credits >= min_credits)

# Modify user credits using assignment operators
user_credits +=50
user_credits -=20
user_credits *=2
user_credits %=150

# calculate the square

Power_result = user_credits * 2

# check full access
Full_access = Is_Logged_in and Is_Subscribed

# check identity operator
Is_true_login = Is_Logged_in is True

# Demonstrate operator precedence
Access_result = Is_Logged_in or Is_Subscribed and False

# print results
print("Is Logged In:", Is_Logged_in)
print("Is Subscribed:", Is_Subscribed)
print("Credits Valid:", Credits_valid)
print("Bonus Eligible:", Bonus_eligible)
print("User Credits:", user_credits)
print("Power Result:", Power_result)
print("Full Access:", Full_access)
print("Is True Login:", Is_true_login)
print("Access Result:", Access_result)