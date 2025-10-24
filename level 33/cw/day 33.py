# 1)ფარენჰეიტებიდან გადავიყვანოთ  გრადუსებზე

# ფოპრმულა არის ეს

# formual -> 5/9 * (f - 32)

# def to_celsius(f):    
#      # aq dawere pasuxii <3 


def to_celsius(f):
    return 5/9 * (f - 32)

print(to_celsius(100))



# 2)sum all parameters <3
# def calculate_damage(opening_attack, core_damage, finishing_move):
    
# ---> "wizzard new life is SUMED_CALCULATED"
# calculate_damage(10, 20, 30)

opening_attack = 10
core_damage = 20
finishing_move = 30
def calculate_damage(opening_attack, core_damage, finishing_move):
    result = opening_attack + core_damage + finishing_move
    return f"wizzard new life is {result}"
print(calculate_damage(10, 20 ,30))