num1=int(input("escribe un  numero:"))
num2=int(input("escribe otro  numero: "))
num3=int(input("escribe otro  numero: ")) 
if(num1>num2 and num1<num3 or num1<num2 and num1<num3):
    print(f"El número mayor es {num1}")
elif(num2>num1):
    print(f"El número mayor es {num2}")
else:
    print("los numeros son iguales") 
