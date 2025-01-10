text= "python class"
next_text="it was going fast"
#using sting
print(text.upper())
print(text.lower())
print(text.title())
print(f"{text}\t{next_text}")
print(text)
print(text[4:6])
print(f"{text.split()}{next_text.split()}") 
total=text+next_text
total_cha=len(total)
total_word=len(total.split())
print(F"number of character:{total_cha}")
print(f"number of word:{total_word}")