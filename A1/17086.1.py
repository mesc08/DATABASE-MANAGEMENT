"""
ASSIGNMENT 1
NAME: SRIJAN CHAKRABORTY
ROLL NUMBER : 39/CSE/17086/284
REGISTRATION NUMBER: 0000284
"""
def FETCH(K,L,d):
        k=[]
        for i in range(0,len(L)):
                k.append(0)
        print("ENTER THE COMMAND FOR FETCH DATA")
        a = list(input().split(":"))
        b = list(a[0].split(","))
        c = list(a[1].split(","))
        length1 = len(c)
        for i in range(0,length1,2):
                r = c[i+1]
                for j in range(0,len(d[c[i]])):
                        if(r == d[c[i]][j]):
                                k[j]+=1
        o = -1
        z = 0
        for i in range(0,len(L)):
                if(k[i] > o):
                        z = i
                        o = k[i]
        for i in b:
                print(i+" is:"+d[i][z])
def INSERT(file,K,L,d):
        f0 = open(file,"w")
        f0.write("NAME SEM ROLL AGE MARKS MOB_NO  "+"\n")
        print("NUMBER OF RECORDS WANTS TO ENTER")
        query = int(input())
        for i in range(0, query):
                a = input() # 1 TAB SEPERATED INPUT
                L.append(a)
        for i in L:
                a = list(i.split(" "))
                K.append(a)
        U = []
        V = []
        W = []
        X = []
        Y = []
        Z = []
        for i in range(0,len(K)):
                U.append(K[i][0])
                V.append(K[i][1])
                W.append(K[i][2])
                X.append(K[i][3])
                Y.append(K[i][4])
                Z.append(K[i][5])
        d["NAME"] = U
        d["SEM"] = V
        d["ROLL"] = W
        d["AGE"] = X
        d["MARKS"] = Y
        d["MOB_NO"] = Z
        for i in L:
                f0.write(i+"\n")
        f0.close()  
def UPDATE(file,K,L,d):
        print("ENTER THE UPDATE COMMAND")
        update = list(input().split(":"))
        a1 = list(update[0].split(","))
        a2 = list(update[1].split(","))
        a3 = list(update[2].split(","))
        query = int(a1[0])
        length1 = len(a3)
        k = []
        for i in range(0,len(L)):
                k.append(0)
        for i in range(0,length1,2):
                r = a3[i+1]
                for j in range(0,len(d[a3[i]])):
                        if(r == d[a3[i]][j]):
                                k[j]+=1
        o = -1
        z = 0
        for i in range(0,len(L)):
                if(k[i] > o):
                        z = i
                        o = k[i]
        for i in range(1,query+1):
                d[a1[i]][z] = a2[i]
        f1 = open(file,"w")
        f1.write("NAME SEM ROLL AGE MARKS MOB_NO  "+"\n")
        for i in range(0,len(d["NAME"])):
                f1.write(d["NAME"][i]+" ")
                f1.write(d["SEM"][i]+" ")
                f1.write(d["ROLL"][i]+" ")
                f1.write(d["AGE"][i]+" ")
                f1.write(d["MARKS"][i]+" ")
                f1.write(d["MOB_NO"][i]+" ")
                f1.write("\n")
        f1.close()
def DELETE(file,K,L,d):
        print("ENTER THE DELETE COMMAND")
        a4 = list(input().split(","))
        k = []
        for i in range(0,len(L)):
                k.append(0)
        length1 = len(a4)
        for i in range(0,length1,2):
                r = a4[i+1]
                for j in range(0,len(d[a4[i]])):
                        if(r == d[a4[i]][j]):
                                k[j]+=1
        o = max(k)
        z = []
        j = 0
        for i in k:
                if o == i:
                        z.append(j)
                j+=1
        p = 0
        for i in range(0,len(z)):
                L = L[:z[i]-1*p]+L[z[i]+1-1*p:]
                K = K[:z[i]-1*p]+K[z[i]+1-1*p:]
                p+=1
        
        del d["NAME"]
        del d["SEM"]
        del d["ROLL"]
        del d["AGE"]
        del d["MARKS"]
        del d["MOB_NO"]
        U = []
        V = []
        W = []
        X = []
        Y = []
        Z = []
        for i in range(0,len(K)):
                U.append(K[i][0])
                V.append(K[i][1])
                W.append(K[i][2])
                X.append(K[i][3])
                Y.append(K[i][4])
                Z.append(K[i][5])
        d["NAME"] = U
        d["SEM"] = V
        d["ROLL"] = W
        d["AGE"] = X
        d["MARKS"] = Y
        d["MOB_NO"] = Z
        f1 = open(file,"w")
        f1.write("NAME SEM ROLL AGE MARKS MOB_NO  "+"\n")
        for i in range(0,len(d["NAME"])):
                f1.write(d["NAME"][i]+" ")
                f1.write(d["SEM"][i]+" ")
                f1.write(d["ROLL"][i]+" ")
                f1.write(d["AGE"][i]+" ")
                f1.write(d["MARKS"][i]+" ")
                f1.write(d["MOB_NO"][i]+" ")
                f1.write("\n")
        f1.close()
file = 'Students_Details.txt'
K = []
L = []
d = {}
while(1):
        print("WELCOME")
        print("OPTIONS AVAILABLE ARE AS FOLLOWING")
        print("PRESS 1 FOR INSERT RECORD")
        print("PRESS 2 FOR UPDATE RECORD")
        print("PRESS 3 FOR DELETE RECORD")
        print("PRESS 4 FOR FETCH  RECORDS")
        print("PRESS 5 FOR EXIT")
        print("CHOOSE YOUR OPTION:")
        option = int(input())
        if(option == 1):
                print("INSERT RECORD")
                INSERT(file,K,L,d)
        elif(option == 2):
                print("UPDATE RECORD")
                UPDATE(file,K,L,d)
        elif(option == 3):
                print("DELETE RECORD")
                DELETE(file,K,L,d)
        elif(option == 4):
                print("FETCH DATA")
                FETCH(K,L,d)
        else:
                print("EXIT")
                break;
                
