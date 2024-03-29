str1=input()
str2=input()
str3=sorted(str1)
str4=sorted(str2)
if(len(str1)==len(str2) and str3==str4):
    print(True)
else:
    print(False)