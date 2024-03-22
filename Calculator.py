from replit import clear
def add(n1,n2):
  sum=n1+n2
  return sum
def subtract(n1,n2):
  diff=n1-n2
  return diff
def multiply(n1,n2):
  prod=n1*n2
  return prod
def division(n1,n2):
  div=n1//n2
  return div  

def calculator():
  num1=int(input('Enter number1: ')) 
  operations={'+':add,'-':subtract,'*':multiply,'/':division}
  for i in operations:
    print(i)
  check= True
  while check==True:
    num2=int(input('Enter number2: ')) 
    operation_symbol=input('Pick an operation')
    calc_func=operations[operation_symbol]
    result=calc_func(num1,num2)
    print('The result is: ',result)
    ans =input('type y if you want to continue or type n for new calculation')
    if ans==y:
      num1 = result
    else:
      check =False
      clear()
      calculator()
calculator()