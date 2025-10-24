# 1) ახსენი  რას ნიშნავს “default value” ფუნქციის პარამეტრებში. iyeneba rodesac ar gvaqvs raime mnishvneloba minichebuli raime sityvistvis da is gamoiyeneba rac weria defaultshi

# 2) ახსენით return ის მნიშვნელობა. gamoiyeneba rom daabrunos mnishvneloba da daasrulos kodis shesruleba

#3) შექმენით ფუნქცია სახელწოდებით substract, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების სხვაობა.
a = int(input("enter your number: "))
b = int(input("enter your number: "))

def substract(a, b):
    result = a - b
    return f"{result}"
print(substract(a, b))


#4)  შექმენით ფუნქცია სახელწოდებით multiply, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების ნამრავლი.

c = int(input("enter your number: "))
d = int(input("enter your number: "))

def multiply(c, d):
    result = c * d
    return f"{result}"
print(multiply(c, d))

# 5) შექმენით ფუნქცია სახელწოდებით divide, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების განაყოფი.
e = int(input("enter your number: "))
f = int(input("enter your number: "))

def divide(e, f):
    result = e // f
    return f"{result}"
print(divide(e, f))