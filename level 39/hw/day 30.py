#1
def no_space(x):
    return x.replace(" " ,"")


#2
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
    return count


#3
def greet():
    return "hello world!"


#4
def string_to_number(s):
    return int(s)


#5
def summation(num):
    result = 0
    for kasper in range(1, num + 1):
        result += kasper
    return result