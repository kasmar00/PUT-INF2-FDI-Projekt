from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("../results") if isfile(join("../results", f))]

exp=open("results.txt", "w+")
for i in onlyfiles:
    print(i)
    a=open("../results/"+i, "r")
    b=a.read()
    c=b.split("\n")
    res=[]
    res.append(c[1].split(" ")[-1])
    res.append(c[3].split(" ")[-1])
    res.append(c[4].split(" ")[-1])
    res.append(c[5].split(" ")[-1])
    res.append(c[-2])
    n=0

    for j in c:
        # print(j)
        if len(j)>0:
            if j[0]=="(":
                liczba=int(j.split(", ")[0][1:])
                n=max(n, liczba)
    print(n)
    res.append(str(n))
    #res=[float(x) for x in res]

    # print(res)
    exp.write(" ".join(res)+"\n")

