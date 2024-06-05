n= 2
results =[]
count =0
for i in range (11):
    result4 = ( n*i)
    count+=1
    print (n, "x",i , "=", result4)
    results.append(n*i)

print(results)
print(results[::-1])
print(n*count)
print(sum(results))
