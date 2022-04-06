str = "This is the string ee"

maxch = ''
maxnum = 0
minnum = 1
minch = []

for ch in str:
    #print(str.count(ch))
    if (ch == ' '):
        continue
    if (str.count(ch) > maxnum):
        maxnum = str.count(ch)
        maxch = ch
    if (str.count(ch) <= minnum):
        minnum = str.count(ch)
        minch.append(ch)
        

print(maxch,maxnum)
print(minch,minnum)