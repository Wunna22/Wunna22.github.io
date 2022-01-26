from ctypes.wintypes import PINT


#num1 = int (input('Enter first Number: '))
#num2 = int (input('Enter second Number: '))
num1 = 15
num2 = 3
num3 = num1 + num2 
num5 = num1 * num2
num6 = num1 / num2
num7 = num1 % num2
num8 = num1 // num2  #floor division
num9 = num1 ** num2  #exponent
print(num3,num5,num6,num7,num8,num9)

if(num1 == num2) :
    print('%s is equal to %s.' %(num1,num2))
if(num1 != num2) :
    print('Num1 is not equal to num2')
if num1 > num2 :
    print('Num1 is greater than Num2')

num10 = num1 + num2
num10 += num2
num10 -= num2
num10 *= num1
print('Num 10 is %s' %(num10))

a= 60
print(a>>2)

a = 9
b = 12
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)

if(5<9) and (2>1): 
    print('ok')
print(True and False)
print(False or True)

print('Enter two to divide')
divident = int(input('Enter divident: '))
divisor = int(input('Enter dividor: '))
result = divident/divisor
print(divident, '/', divisor, '=', result)

value = int(input('Enter a number to split: '))
result = value/2
print('Half of ',value, ' is ', result)

degreeF = float(input('Enter F Degree: '))
degreeC = 5/9 * (degreeF - 32)
print(degreeF, 'degree F = ', degreeC, 'degree C = ')

seconds = int(input('Please enter seconds: '))
hour = seconds//3600
seconds = seconds%3600
minutes = seconds//60
seconds = seconds%60
print(hour, 'Hours: ', minutes, 'Minutes: ',seconds, 'Seconds: ')
