def number(num):
    num_str = str(num)
    total_sum = sum(int(num_str[i]) ** (i + 1) for i in range(len(num_str)))
    return num == total_sum

try:
    user_input = int(input("Enter a number: "))
    if number(user_input):
        print(user_input, "is a disarium number.")
    else:
        print(user_input, "is not a disarium number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
