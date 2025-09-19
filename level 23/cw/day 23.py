a = "lomi"
print(len(a))

for i in range (len(a)):
    print(a [i])


b = 'mizi and sua'

print(len(b))

new_b = ""

for i in range(len(b)):
    if b[i] != " ":
        new_b += b[i]

    print(new_b)