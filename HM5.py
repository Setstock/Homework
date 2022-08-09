
x = int(input("Number1 : "))

y = int(input("Number2 : "))

def findLargestNumber(x,y):
    a=str(x)
    b=str(y)
    data = []
    data2=[]
    for i in range(0,len(a)):
       data.append(int(a[i]))
    for i in range(0,len(b)):
       data2.append(int(b[i]))
##    print(data)
    data.sort()
    data.reverse()
    data2.sort()
    data2.reverse()
##    print(len(data))
    strdata = ""
    strdata2 = ""
    for i in range(0,len(data)) :
       strdata = strdata + str(data[i])
    for i in range(0,len(data2)) :
       strdata2 = strdata2 + str(data2[i])
    data_all = [int(strdata),int(strdata2)]
    data_all.sort()
    data_all.reverse()
    strdata_all = ""
    for i in range(0,len(data_all)) :
       strdata_all = strdata_all + str(data_all[i])
##    print(strdata)
    return strdata_all
 
 
if __name__ == '__main__':
 
    largestNumber = findLargestNumber(x,y)
    print('The largest number is', largestNumber)
