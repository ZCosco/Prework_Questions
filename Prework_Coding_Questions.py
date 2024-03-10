# Question 1
def hello_name():
    print("What is your username")
    username = input()
    print(f'Hello_{username}!')

# Question 2
def first_odds():
    for number in range(1,100,2):
        print(number)

# Question 3
a_list = [3,6,2,8,4,9,3,]
def max_num_in_list(a_list):
     max(a_list)
     return

# Question 4 
a_year = (2024)
def is_leap_year(a_year):     
    if a_year % 4 == 0:
        # Check if the year is not divisible by 100, or it is divisible by 400
        if a_year % 100 != 0 or a_year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


# Question 5 
def is_consecutive(a_list):
    if len(a_list) <= 1:
        return False
      
    for i in range(1, len(a_list)):
        # Check if the current element is not one more than the previous element
        if a_list[i] != a_list[i-1] + 1:
            return False

    # If the loop completes without returning False, the numbers are consecutive
    return True

hello_name()
first_odds()
max_num_in_list(a_list)
print(is_leap_year(a_year))
print(is_consecutive(a_list))