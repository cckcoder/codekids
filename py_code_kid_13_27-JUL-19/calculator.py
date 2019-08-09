number1 = int(input('First number: '))
number2 = int(input('Second number: '))

operator = input('add/sub/mul/div: ')

if operator == 'add':
   ans = number1 + number2
elif operator == 'sub':
   ans = number1 - number2
elif operator == 'mul':
   ans = number1 * number2
elif operator == 'div':
   ans = number1 / number2
else:
   print('Error')

print(ans)
