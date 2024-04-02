s=input()
p=input()
p1=set(p)
l=[]
for i in range(len(s)-len(p)+1):
    if(set(s[i:i+len(p)])==p1):
        l.append(i)
print(l)