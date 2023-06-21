Find the sentence is a anagram
"take 2 input
convert then into lower case
len=
sort then

eg
ate=eta
it is a anagram"


i=input() 
j=input()
newtext1=i.lower()
newtext2=j.lower()
if len(newtext1)==len(newtext2):
    a=sorted(newtext1)
    b=sorted(newtext2)
    if a == b:
        print("It is a Anagram")
    else:
        print("It is not a Anagram")
else:
    print("it is not a Anagram")
