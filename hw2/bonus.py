import sys
r_path=sys.argv[1]
w_path=r_path.split(".")[0]+"_b_out.pgm"
def readfile(r_path):
    a=open(r_path,"r")
    r=a.read()
    r1=r.split("\n")
    n=len(r1)
    i=0
    while 1:
        if i==n:
            break
        if "#" in r1[i]:
            r1.remove(r1[i])
            i-=1 ; n-=1
        i+=1
    t=[]
    for i in range(len(r1)):
        app=r1[i].split(" ")
        while "" in app:
            app.remove("")
        for j in range(len(app)):
            t.append(app[j])
    w=int(t[1])
    h=int(t[2])
    if t[0]!="P2":
        wr=open(w_path,"w")
        wr.write("error")
        wr.close()
        sys.exit()
    t=t[4:]

    lis=[]
    for i in range(len(t)):
        if i%w==0:
            app=[]
        app.append(int(t[i]))
        if i%w==w-1:
            lis.append(app)
    return lis,h,w
def convolution(pic,mask):
    out=[]
    n=len(mask)//2
    h=len(pic)
    w=len(pic[0])
    for i in range(h):
        app=[]
        for j in range(w):
            val=0
            for k in range(-n,n+1):
                for l in range(-n,n+1):
                    m=i+k
                    val+=mask[k+n][l+n]*pic[(i+k)%h][(j+l)%w]
            app.append(int(val))
        out.append(app)
    return out
def Log(sig,n=1): #n=1 equals to 3*3 kernel
    exp=2.718281828459045
    out=[]
    for i in range(-n,n+1):
        app=[]
        for j in range(-n,n+1):
            val=(i**2+j**2-2*sig**2)/4/sig**2*exp**(-(i**2+j**2)/2/sig**2)
            app.append(val)
        out.append(app)
    return out
def Gaussian(sig,n=1): #n=1 equals to 3*3 kernel
    exp=2.718281828459045
    out=[]
    tot=0
    for i in range(-n,n+1):
        app=[]
        for j in range(-n,n+1):
            val=exp**(-(i**2+j**2)/2/sig**2)
            tot+=val
            app.append(val)
        out.append(app)
    for i in range(2*n+1):
        for j in range(2*n+1):
            out[i][j]/=tot
            
    return out

def L_edge(pic,lis,t):#t stands for threshold
    h=len(pic)
    w=len(pic[0])
    out=pic #copy an h*w matrix
    for i in range(h):
        for j in range(w):
            
            if lis[i][j]*lis[(i+1)%h][j]<0 and abs(pic[i][j]-pic[(i+1)%h][j])>t:
                #print(1)
                out[i][j]=out[(i+1)%h][j]=0
            if lis[i][j]*lis[i][(j+1)%w]<0 and abs(pic[i][j]-pic[i][(j+1)%w])>t:
                out[i][j]=out[i][(j+1)%w]=0
                #print(1)
            if out[i][j]!=0:
                out[i][j]=255
    return out
 
def writefile(w_path,out,h,w):
    wr=open(w_path,"w")
    wr.write("P2\n#\n")
    wr.write(str(w)+" "+str(h)+"\n")
    wr.write("255\n")
    for i in range(len(out)):
        for j in range(len(out[i])):
            wr.write(str(out[i][j])+"  ")
        wr.write("\n")
    wr.close()
lis,h,w=readfile(r_path)
out=convolution(lis,Log(1.6,4))
out_edge=L_edge(lis,out,16)
#direct using Laplacian operator
#La=[[0,1,0],[1,-4,1],[0,1,0]]
#out=convolution(lis,La)
#out_edge=L_edge(lis,out,32)
writefile(w_path,out_edge,h,w)
