# to check greater number below
n1=int(input("first number:"))
n2=int(input("second number:"))
n3=float(input("third number:"))

if n1>n2 and n2>n3 :
    print(f"{n1} is greaterthan {n2} and{n3}")
elif n2>n3 and n3>n1:
    print(f"{n2} is greaterthan {n3} and {n1}")
elif n3>n2 and n2>n1:
    print(f"{n3} id greaterthan {n2} and {n1}")

else:
    print("input data is not true")
    print("should be given condition is not true")
    print("check again condition and data")
#and
#true and true is true
#true and false is false
#false and true is false
#false and false is false

#OR
#true and true is true
#true and false is true
#false and true is true
#false and false is false