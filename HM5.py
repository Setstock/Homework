
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

    strdata_all = ""
    if int(strdata[0]) > int(strdata2[0]):
        strdata_all = strdata_all + strdata + strdata2
    elif int(strdata[0]) < int(strdata2[0]):
        strdata_all = strdata_all + strdata2 + strdata
    elif int(strdata[0]) == int(strdata2[0]):
        if len(strdata) > len(strdata2):
            strdata_all = strdata_all + strdata2 + strdata
        else:
            strdata_all = strdata_all + strdata + strdata2
##    print(strdata)
    return strdata_all
 
 
if __name__ == '__main__':
 
    largestNumber = findLargestNumber(x,y)
    print('The largest number is', largestNumber)
