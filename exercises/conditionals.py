i=1000
checking=False
while checking==False:
    if i%6==2 and (i**3)%5==3:
        print(i)
        checking=True
    else:
        i-=1