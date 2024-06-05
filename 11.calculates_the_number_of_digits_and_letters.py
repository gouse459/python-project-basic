user_input = input()
degits = 0
letters =0
for i in user_input :
    if i.isdigit():
        degits = degits +1
    elif i.isalnum():
        letters =letters +1
print ("The Given String", user_input, "has",letters, "letters and", degits, "digits.")