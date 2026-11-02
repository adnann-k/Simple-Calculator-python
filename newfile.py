Num1= float(input("Enter Num1:"))
Num2= float(input("Enter Num2:"))
Operator=input("Enter the Operator:(+,-,*,/,%)")
#+ - * /%
if Operator == "+":
  print("Num1+Num2=",Num1+Num2)
elif Operator == "-":
   print("Num1-Num2=",Num1-Num2)
elif Operator == "*":
   print("Num1*Num2=", Num1*Num2)
elif Operator =="/":
   if Num2 == 0:
       print("cannot be divided by 0 or Not defined")
   else:       
       print("Num1/Num2=",Num1/Num2)
elif Operator == "%":
    if Num2 != 0 :
        print("Num1%Num2=",Num1%Num2)
    else:
         print("Cant be divided by zero or not defined")
    
else:
  print("error")
                      