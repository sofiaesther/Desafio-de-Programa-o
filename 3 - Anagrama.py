import collections
def anagrama(st):
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    size=len(st)
    sizeana=1
    listw=list(st)
    total=0
    while sizeana<size:
        qntana=size-sizeana
        for i in range(qntana):
            count=0
            word=""
            while count<sizeana:
                word=word+listw[i+count]
                count=count+1


            for j in range(qntana-i):
                count=1
                wordr=""
                while count<=sizeana:
                    wordr=wordr+listw[j+i+count]
                    count=count+1
                w=list(word)
                wr=list(wordr)
                a=0
                if compare(w,wr)==True:
                    total=total+1
        sizeana=sizeana+1

    return total