def duqu_zxt():
    f=open("C:/Users/Administrator/Documents/GitHub/aar/pydm/txt/print_zxt.txt","r")
    s=f.read()

    astr=s.split('\n')
    ZXsrt=""
    z=0
    x=0
    h=0
    f.close()
    for i in astr:


        if i=="x":
            x=x+1
            if z != 0:
                ZXsrt=ZXsrt+"Z"+str(z) +","
                z=0
                h=0
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) +","
                z=0
                h=0
        elif i=="z":
            z=z+1
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x) +","
                x=0
                h=0
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) +","
                x=0
                h=0
        elif i=="h":
            h=h+1
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x) +","
                x=0
            elif z !=0:
                ZXsrt=ZXsrt+"Z"+str(z) +","
                z=0
        elif i=="KO":
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x)
            elif z !=0:
                ZXsrt=ZXsrt+"Z"+str(z) 
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) 
                z=0
                x=0
                h=0
    return ZXsrt


print(duqu_zxt())
