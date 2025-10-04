# reverse the string 

# Way 1 :  by using the pyhton slicing 
str = "Aishwarya"
rev = str[::-1] # pyhton slicing method 
print("The Reverse String is : = ",rev)

# Way 2 : withiut using inbuilt functions 
s1 = "Diviksha"
rev1 =""
for i in s1:
    # rev1 = rev1 + i # this will give u result as : => Diviksha
    rev1 = i + rev1 # this will give u result as : => ahskiviD
print("The Reverse String is : = ",rev1)

# way 3 : using inbuilt functions 
text = "Aishwarya"
reversed_text = "".join(reversed(text))
print(reversed_text)  # Output: ayrawhsiaA