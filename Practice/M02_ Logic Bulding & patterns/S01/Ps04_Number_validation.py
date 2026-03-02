'''
Armstorng number:
input : 153
output : Armstrong number

input: 24
output : not an Armstrong '''

n = int(input())
count = len(str(n))
s = 0
for digit in str(n):
     s+= int(digit) ** count

print("Armstorng number" if s == n else "not an Armstorng number")

'''
perfect number 
input : 6
output : perfect number
'''
#n = int(input())
#for i in range(1,n//2+1):
  #  if n % i == 0:
   #      s += i
#print("perfect number" if s == n else"not a perfect number") 

'''
Strong number:
input: 123
output : not a strong number
explination : 1! + 2! + 3! = 1+2+6 = 9
'''            
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "No factorial for -ve numbers"
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
 