"split numeric data from string in python and find the max value"
a=input("Enter the string: ")
number=[]
x=a.split()
for i in x:
    if i.isnumeric():
        number.append(int(i))
        #print(number)
        k=max(number)
        print(k)
