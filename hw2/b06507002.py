import sys
r_path=sys.argv[1]
w_path=r_path.split(".")[0]+"_out.pgm"

try:
    limit=float(sys.argv[2])
except:
    limit=128

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
def writefile(w_path,lis,h,w):
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
out=[]
for i in range(h):
    app=[]
    if i==0 or i==h-1:
        for j in range(w):
            app.append(255)            
    else:
        
        for j in range(w):
            if j==0 or j==w-1:
                app.append(255)
            else:
                
                a=lis[i-1][j-1];d=lis[i-1][j];g=lis[i-1][j+1]
                b=lis[i][j-1];e=lis[i][j];h2=lis[i][j+1]
                c=lis[i+1][j-1];f=lis[i+1][j];i2=lis[i+1][j+1]
                x=(c+2*f+i2)-(a+2*d+g);y=(g+2*h2+i2)-(a+2*b+c)
                if (x**2+y**2)**0.5>=limit:
                    app.append(0)
                else:
                    app.append(255)                   
    out.append(app)
writefile(w_path,out,h,w)

