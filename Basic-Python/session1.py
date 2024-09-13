'''print("-------------------------   Operations on String   -----------------------")
name = input("Enter Your Name : ")
print(f"Name of Candidate : {name}")
roll = int(input("Enter Your Roll no : "))
print("Roll No : ", roll)
str = " Hello , Welcome to Python Training "
print(" 4th Character of String :", str[3])
print(" String Upto 5th Character : ", str[:6])

print("-------------------------   String Methods   -----------------------")
str1 = "This is Sanjivani College of Engineering , Kopargaon"
print("Lowercase : ", str1.lower())
print("Uppercase : ", str1.upper())
print("Length : ", len(str))
print(str1.split(','))
dir(str) '''

''' Bitwise Operators '''
x=10
y=5
print("X : ", x, " Y :", y)
result = x & y
print("And operation : ", result)
result = x^y
print("Ex-Or operation : ", result)
result = ~ x
print("Not operation on X : ", result)
result = x<<1
print("x<<", result)
