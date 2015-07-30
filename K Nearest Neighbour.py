"""
Machine Learning 
Program to implement K Nearest neighbor and calculate the error and standard deviation for different permutation
 and the given sample"""
import math
# Data Structures Used in the program
my_dict=[]
inter_list = []
inter2_list = []
org_sym_mat = []
k=0
m=0
t=0
row=0
col=0

"""Find the nearest neighbor from a given test data to all the training data and hence find the resultant symbol of the test 
as per the neighbors which will be used to calculate the error and hence standard deviation
Input: K Nearest Neighbor Value, Test list and Training List
Returns: - or +"""
def nearest(zk,test,train):#zk is Kth term in Nearest Neighbor
    distance=[]
    dist = 0
    for i in train:#Euclidian Distance
        x=(test[1]-i[1])
        y=(test[0]-i[0])
        dist = pow(x,2)+pow(y,2)
        distance.append(dist)#Distance List
    KnearN=[]
    KnearN=topnear(zk,distance,train)#Given the top K smallest distance
    symbol=Prioritysym(KnearN)#Calling for function to check priority
    return symbol#Returns the symbol
    
"""Sort the Distance List and storing in tpnear in increasing order
Input: K Nearest Neighbour value, Distance List and Training Value List
Return: List of distance value index from distance list in increasing order"""
def topnear(zk,distance,train):
    dist = distance[:] 
    tpnear =[]
    for im in range(0,zk):
        minimum=min(dist)
        min_indx=dist.index(minimum)
        tpnear.append(train[min_indx])
        dist[min_indx]=99999 
    return tpnear
"""Check the priority of the test data Input: SymbolList; Returns : + or -"""
def Prioritysym(symlist):
    sympos=0
    symneg=0
    for i in range(0,len(symlist)):
        if(symlist[i][2]=="+"):
            sympos=sympos+1
        else:
            symneg=symneg+1
    if(sympos > symneg):
        return"+"
    else:
        return"-"
"""Calculate the error value and returns to the main code. Uses the Nearest and Prioritysym for calculating the value
Input: The original tuple list(List_fold)Value of k and m and zk; k id the number of fold and m is the number of given input
Returns: Error value"""
def fold(list_fold,k,m,zk):
    error=0
    div = int(m/k) 
    rem = int(m%k)
    testset=[]    
    for i in range(0,k+1,1):
        if(k-i<rem):
            testset.append(i*div+rem-k+i)
        else:
            testset.append(i*div)
    for i in range(0,k):
        testdata=[]
        traindata=[]
        for m in range(0,len(list_fold)):
            if((m>=testset[i]) and (m<testset[i+1])):
                testdata.append(list_fold[m])
            else:
                traindata.append(list_fold[m])
        """Testing and Training Data is divided amongest the given set for Cross Validation"""        
        for e in range(0,len(testdata)):
            ch = nearest(zk, testdata[e], traindata)
            if(ch != testdata[e][2]):
                error=error+1
              
    return error

"""The Input files is read and the data is read in different file for calculation"""
file_name = input("Enter the file name : ")
with open(file_name) as f:
    for line in f:
        if (len(line)<10):
            (k,m,t) = line.rstrip('\n').split(' ')#first line splitting for k m and t 
            
        else: 
            list_1 =[]
            for val in line:
                if(val.isdigit()):
                    list_1.append(val)
            inter_list.append(list_1)#Contains all the permutation in this matrix
    
file_name2 = input("Enter the file name : ")
with open(file_name2) as f1:
    rownum =0
    colnum =0
    indx = 0
    for lines in f1:
        if (len(lines)<6):
            (row,col) = lines.rstrip('\n').split(' ')#Row and Column is separated and values is stored
        else:
            temp=[]
            for i in lines.rstrip('\n'):
                if (i != " "):
                    temp.append(i)
            org_sym_mat.append(temp)#Original Matrix which stores all the symbols
            colnum =0
            for sym in lines.rstrip('\n'):
                if (sym != " "):
                    my_dict.append((colnum,rownum,sym))#making a list of tuples which stores coordinates and symbol associated
                    indx = indx+1
                    colnum =colnum+1
            rownum =rownum+1
    index_train=0
    finaltest=[]
    
    for sym in my_dict:
        
        if(sym[2]=="+" or sym[2]=="-"):
            inter2_list.append(sym)#separating all the symbol which contains all plus and negative. In other words given data
    for o in inter_list:
        index_ratio =[]
        for n in o:
            index_ratio.append(inter2_list[int(n)])#Permutation tuples are arranged in given permutation values 
        finaltest.append(index_ratio)#this is final matrix which contain all the permutation
#converting to integers          
k=int(k)
m=int(m)
t=int(t)
for zk in range(1,6):#Zk is the value of K in nearest Neighbor
    error=[]#will hold the list of error value
    totalerr=0#total value of error
    stand_div=0#Standard Deviation
    #if (int(m/k)>=zk):
    """Mean Calculations"""
    for j in range(0,t):
            #print(inter_list[j])
        errval=fold(finaltest[j],k,m,zk)# Gets the error value
               
        error.append(errval)
        totalerr=errval+totalerr
       
        meanerror = float(totalerr/(m*t))
        """Standard Deviation"""
    for j in range(0,t):                
        differ = error[j]/m - meanerror
        div = pow(differ, 2)
        stand_div=stand_div+ div
    stand_div= stand_div/(t-1)
    stand_div=math.sqrt(stand_div)
        #print("OUTPUT : ")
    print("K :"+ str(zk),"Error :"+str(meanerror),"Smiga :"+str(stand_div))
    final_output=[]
    """Printing the matrix output"""
    for set in my_dict:
        if(set[2]=="."):
            symbol=nearest(zk, set, inter2_list)
        else:
            symbol=set[2]
        final_output.append(symbol)
        #print(final_output)
    #printing the final output in matrix format
    for a in final_output:
        coll=0
        temp_prt=""
            
    for b in final_output:
        if (coll <= 5):
            temp_prt=temp_prt+b+" "
            coll= coll+1
        if(coll == 5):
            print(temp_prt)
            temp_prt=""
            coll=0                  
                
        
                
            
                
            
  