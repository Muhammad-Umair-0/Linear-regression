from sklearn.metrics import mean_absolute_error as mae


actual = [2,3,5,5,9]
calculated = [3,3,8,7,6]

n= 5 
sum = 0

for i in range(n):
    sum += abs(actual[i] - calculated[i])
    print(sum)
    
error = sum/n

print(sum)
print("Mean absolute error : " + str(error))

x = abs(-7.25)
print(x)


error_Sk = mae(actual, calculated)
print("Mean absolute error : ",error_Sk)



