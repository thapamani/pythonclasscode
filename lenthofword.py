#find the total word,list,split
text=input("enter model name;")
number=int(input("enter model number:"))
models=text+number
length=len(models)
length_word=len(models.split())
print(f"length is:{length}")
print(f"word are:{length_word}")

