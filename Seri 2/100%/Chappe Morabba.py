# n=int(input())
# print((n*'*'+'\n')+((n-2)*('*'+((n-2)*' ')+'*'+'\n'))+(n*'*'))
m = int(input())
print('*' * m)
print((('*'+(m-2)*' '+'*'+'\n')*(m-3))+('*'+(m-2)*' '+'*'))
print('*' * m)
