s1=input()
s2=input()[-1]
cnt=0
for i in s1:
    if i==s2:
        cnt+=1
print(cnt)
