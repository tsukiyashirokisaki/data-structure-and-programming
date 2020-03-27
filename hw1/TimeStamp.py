import sys
import random
#c=cost;c_lis=cost list for output
r_path=sys.argv[1]
w_path=sys.argv[2]
random.seed()
a=open(r_path,"r")
r=a.read()
a.close()
r=r.replace(" ","")
p=0.5*(3-5**0.5)
c=0
def TS(r,p):
    clis=[]
    zeros=[]
    c=0
    n=len(r)
    for i in range(10):
        zeros.append(0)
    zeros.append(1)
    lis=[]
    for i in range(10):
        lis.append(i)
    lisa=[]
    for i in range(10):
        lisa.append([])
        for j in range(11):
            lisa[i].append(0)
    for i in range(n):
        check=int(r[i])
        for j in range(10):
            if check==lis[j]:
                c+=(j+1)
                if random.uniform(0,1)<=p:
                    lis=[lis[j]]+lis[:j]+lis[j+1:]
                else:
                    ind=j
                    if lisa[check][10]==0:
                        lisa[check][10]=1
                    else:
                        while j!=0:
                            j-=1
                            if lisa[check][lis[j]]<=1:
                                lis=lis[:j]+[lis[ind],lis[j]]+lis[j+1:ind]+\
                                lis[ind+1:]
                                break
                for k in range(10):
                    if lisa[k][10]==1:
                        lisa[k][check]+=1
                for k in range(10):
                    lisa[check][k]=0
        if (i+1)%50==0:
            clis.append(c)
    return clis                    
output=["TS"]+TS(r,p)

w=open(w_path,"w")
for ele in output[:-1]:
    w.write(str(ele)+"\n")
w.write(str(output[-1]))
w.close()

            