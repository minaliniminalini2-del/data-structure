from  itertools import combinations
list=[-5,6,-9,8,-88,99,98]
print("positive combinations")
for r in range(1,len(list)+1):
    for combo in combinations(list,r):
        if all(num>0 for num in combo):
          print(combo)
