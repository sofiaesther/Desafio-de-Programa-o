def escada(n):
    n=int(n)
    a=""
    for i in range(n+1):
        if i==1:
            a=((n-1)*" ")+"*"
        else:
            a=a+'\n'+((n-i)*" ")+(i*"*")
    return print(a)
escada(9)