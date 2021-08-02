def hello_name(user_name):
    print("Hello_"+ user_name.upper() + "!")
hello_name("Paris is awesome")

# odd numbers between 1 and 100
def odd_numbers():
    for num in range(1, 101, 2):
        print(num)

        print(odd_numbers())


 # even numbers
 def even_numbers():
     for num in range(1, 100, 2):
         if num % 2 !=0:
             print(num)       

#3. max number
def max_num_in_list(a_list):
    max=a_list[0]
    for x in a_list:
         if x > max:
            max = x
    return max
# print (max_num_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def is_leap_year(a_year):
    leap_year = False
    if a_year % 400 == 0:
        leap_year = True
    elif a_year % 100 == 0:
        leap_year = False
    elif a_year % 4 ==0:
        leap_year = True
    if leap_year == True:
        print(str(a_year) + " is a leap year!")
    else:
        print(str(a_year) + " is not a leap year.")


def is_consecutive(a_list):
    x= a_list[0] - 1
    for number in a_list:
        if number == x + 1:
            number = x
            return True
        else:
            return False

print(is_consecutive([2, 1, 7, 8, 1, 17]))