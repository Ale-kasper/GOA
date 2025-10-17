# 1) მომხმარებელს შემოატანინეთ ერთი რიცხვი და შექმენი ფუნქცია რომელიც შეამოწმებს არის თუ არა რიცხვი ლუწი ან კენტი
num = input("enter your number: ")
def function(num):
    if num % 2 == 0:
        return("luwi")
    else:
        return("kenti")
    

#2) მომხმარებელს შემოატანინეთ ერთი რიცხვი და შექმენი ფუნქცია რომლითაც გაიგებ არის თუ არა ეს რიცხვი დადებითი თუ უარყოფითი
num1 = input("enter your number: ")
def uaryofitdadebiit(num1):
    if num1 > 0:
        return "dadebiti"
    else:
        return "uaryofiti"
    

# 3) მომხარებელს შემოატანინეთ ორი რიცხვი და შექმენი ფუნქცია რომელიც შეადარებს რომელია უფრო დიდი

ricxvi = input("enter your number: ")
ricxvi2 = input("enter your second number: ")

def function(ricxvi, ricxvi2):
    if ricxvi > ricxvi2:
        return "ricxvi metia ricxvi2-ze"
    elif ricxvi < ricxvi2:
        return "ricxvi naklebia ricxvi2-ze"
    else:
        return "ra dawere maseti"
    

# 4) დაწერე პროგრამა, რომელიც მომხმარებლისგან შეიტანს სტუდენტის მიღებულ ქულას (0-დან 100-მდე) და გამოიტანს შესაბამის ნიშანს დამოკიდებულს ქულაზე:
# ქულა        ნიშანი
# 90 – 100      A
# 80 – 89       B
# 70 – 79       C
# 60 – 69       D
# # 0 – 59        F

grade = input("enter your grade: ")

def function():
    if grade > 90:
        return "A"
    elif 89 > grade > 80:
        return "B"
    elif 79 > grade > 70:
        return ("C")
    elif 69 > grade > 60:
        return "D"
    elif 59 > grade > 0:
        return "F"
    else:
        return "u cooked gng"
    


# #5) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში.
# თუ ტემპერატურა 0-ზე ნაკლებია დააბრუნეთ “Today is very cold! Wear warm clothes 💙”,
# თუ 0–30 შორისაა → დაპრინტეთ “Today is a really nice weather 🥰”,
# თუ 30-ზე მეტია → დაპრინტეთ “Today is very hot! Drink plenty of water 🔥”.

weather = input("enter your weather: ")

def function():
    if 0 > weather:
        return "Today is very cold! Wear warm clothes 💙"
    elif weather < 30:
        return "Today is a really nice weather 🥰"
    elif weather > 30:
        return "Today is very hot! Drink plenty of water 🔥"
    else:
        return "ur bout to burn"