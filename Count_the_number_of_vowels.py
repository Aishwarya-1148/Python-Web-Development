# count the total number of vowels 

text = "Aishwarya"
cnt = 0
for i in text:
    # text[i] == "a" this is wrong because i is already a char in text so u dont need to use text[i]
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"  ):
        cnt += 1 
print("The total Number of Vowels present in text is : = ",cnt)


# way 2 : with using some inbult fuctions 
text = "Aishwarya"
cnt = 0
for i in text:
    if i.lower() in "aeiou":
        cnt += 1

print("The total Number of Vowels present in text is:", cnt)
