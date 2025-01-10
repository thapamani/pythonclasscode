#user input
print("enter the monthly financial data")
sales=float(input("monthly sale;"))
expenses=float(input("monthly expenses;"))
salary=float(input("monthly salary;"))
rent=float(input("monthly rent;"))
electricity=float(input("electricity bill;"))

#calculate profite
net_profit= sales-(expenses+salary+rent+electricity)
print("monthly profit report")
print(f"net_profit;{net_profit}")