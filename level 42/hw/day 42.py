# 1

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    

#2

# ver gavige


#3

# ver gavige


#4

def two_decimal_places(n):
    return round(n, 2)


#5
def distinct(seq):
    kasper = []
    for i in seq:
        if i not in kasper:
             kasper.append(i)
    return kasper