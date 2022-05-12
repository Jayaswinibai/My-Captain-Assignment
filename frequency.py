test_str = input("Please enter a string")
res = {}
  
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1

print (" \n"+  str(res))

           

