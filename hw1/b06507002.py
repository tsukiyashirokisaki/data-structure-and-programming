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
def takeSecond(elem):
    return elem[1]
def Optimal(r):
	n=len(r)
	lis=[]
	for i in range(10):
		lis.append([i,0])
	for i in range(n):
		lis[int(r[i])][1]+=1
	lis.sort(key=takeSecond,reverse=True)
	c=0
	for i in range(10):
		c+=int(lis[i][1])*(i+1)
	return c
	#print(n,c)
def MTF(r):
	n=len(r)
	lis=[]
	for i in range(10):
		lis.append(i)
	c=0
	clis=[]
	for i in range(n):
		check=int(r[i])
		for j in range(10):
			if check==lis[j]:
				c+=(j+1)
				lis=[lis[j]]+lis[:j]+lis[j+1:]
		if (i+1)%50==0:
			clis.append(c)
	return clis
def Transpose(r):
	n=len(r)
	lis=[]
	for i in range(10):
		lis.append(i)
	c=0
	clis=[]
	for i in range(n):
		check=int(r[i])
		for j in range(10):
			if check==lis[j]:
				c+=(j+1)
				if j!=0:

					lis[j]=lis[j-1]
					lis[j-1]=check
		if (i+1)%50==0:
			clis.append(c)
	return clis

def BIT(r):
	lis=[]
	for i in range(10):
		lis.append([i,random.randint(0,1)])
	ran=""
	for i in range(10):
		ran+=str(lis[i][1])
	#print(ran,lis)
	n=len(r)
	c=0
	clis=[]
	for i in range(n):
		check=int(r[i])
		for j in range(10):
			if lis[j][0]==check:
				lis[j][1]=(1+lis[j][1])%2
				c+=(j+1)
				if lis[j][1]==1:
					lis=[[check,1]]+lis[:j]+lis[j+1:]
	
		if (i+1)%50==0:
			clis.append(c)
	return [ran]+clis
def FC(r):
	n=len(r)
	lis=[]
	c=0
	clis=[]
	for i in range(10):
		lis.append([i,0])
	for i in range(n):
		check=int(r[i])
		for j in range(10):
			if lis[j][0]==check:
				c+=(j+1)
				lis[j][1]+=1
				lis.sort(key=takeSecond,reverse=True)
				break
		if (i+1)%50==0:
			clis.append(c)
	return clis


output=["optimal:"]
for i in range(20):
	output.append(Optimal(r[:50*(i+1)]))
output.append("MTF:")
output+=MTF(r)
output.append("Transpose:")
output+=Transpose(r)
output.append("BIT:")
output+=BIT(r)
output.append("FC:")
output+=FC(r)
w=open(w_path,"w")
for ele in output[:-1]:
	w.write(str(ele)+"\n")
w.write(str(output[-1]))
w.close()
