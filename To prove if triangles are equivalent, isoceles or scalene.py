s1=int(input("Enter first side :"))
s2=int(input("Enter second side :"))
s3=int(input("Enter third side :"))

if s1==s2==s3:
    print("The triangle is equilateral")
elif s1==s2!=s3 or s1!=s2==s3 or s1==s3!=s3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")

print("Thank you for choosing this program")