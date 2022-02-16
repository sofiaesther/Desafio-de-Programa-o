def senhaforte(senha):
    l=list(senha)
    caractere="!@#$%^&*()-+"
    if len(senha)>=6:
        d=0
    else:
        d=6-len(senha)
        return d
    a=0
    b=0
    c=0
    e=0
    s=""
    for i in l:
        if i.isnumeric()==True:
            a=a+1
        if i.lower()==i:
            b=b+1
        if i.upper()==i:
            c=c+1
        if i in caractere:
            e=e+1
    if a>=1 and b>=1 and c>=1 and d==0 and e>=1:
        s="Sua senha é forte!"
    else:
        if a==0:
            s="Adicione 1 dígito. "
        if b==0:
            s=s+"Adicione 1 letra em minúsculo. "
        if c==0:
            s=s+"Adicione 1 letra em maiúsculo. "
        if e==0:
            s=s+"Adicione 1 caractere especial."
    return print(s)