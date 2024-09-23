



# ONE LINE - NO MORE, NO LESS
table = [x*y for x in range(1, 11) for y in range(1, 11)]




########### NO TOUCHY ###########
for i, num in enumerate(table):
    if i % 10 == 0:
        print()
    
    print(num, end="\t")
print()
#################################