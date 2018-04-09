COUNT=0
def perm(begin,end):
    global COUNT
    if begin>=end:
        print(n)
        COUNT +=1
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(begin+1,end)
            n[num],n[i]=n[i],n[num]
 
n=[1,2,3]
perm(0,len(n))
print(COUNT)
