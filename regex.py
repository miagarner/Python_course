import re
h=open('regex-sum.txt')
t=list()
for line in h:
    x=re.findall('[0-9]+',line)
    t=t+x

sum=0
for l in t:
    sum= sum+int(l)

print(sum)
