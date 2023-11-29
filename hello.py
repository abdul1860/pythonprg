n=int(input("Enter a Number"))
print("Numbers from 1 to ",n," are")
for i in range(n):
    if i%2==0:  
        print(f"{i} is Even")    #prints even numbers
    else:
        print(f"{i} is Odd")
