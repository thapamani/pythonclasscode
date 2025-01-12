#yearly financial report
#yearly sales
print("yearly sales mention below")
jan=int(input("jan:"))
feb=int(input("feb:"))
march=int(input("march:"))
april=int(input("april:"))
may=int(input("may"))
jun=int(input("jun:"))
july=int(input("july:"))
agust=int(input("agust:"))
sep=int(input("sep:"))
oct=int(input("oct:"))
nov=int(input("nov:"))
dec=int(input("dec:"))
sales=jan+feb+march+april+may+jun+july+agust+sep+oct+nov+dec
print(f"total sales:{sales}")
#yearly expenses
print("yearly expenses mention below")
jan=int(input("jan:"))
feb=int(input("feb:"))
march=int(input("march:"))
april=int(input("april:"))
may=int(input("may"))
jun=int(input("jun:"))
july=int(input("july:"))
agust=int(input("agust:"))
sep=int(input("sep:"))
oct=int(input("oct:"))
nov=int(input("nov:"))
dec=int(input("dec:"))
expenses=jan+feb+march+april+may+jun+july+agust+sep+oct+nov+dec
print(f"total expenses of year:{expenses}")

#yearly profit
total_profit=sales-expenses
print(f"total\tprofit;{total_profit}")
