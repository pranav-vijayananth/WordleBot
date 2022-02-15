user_guess = "apple"
output = [["" for j in range(2)] for i in range(5)]

for index in range(0, 5):
    output[index][0] = user_guess[index]

print(output)