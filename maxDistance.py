n=input("give the number of distances")
array=[]
for i in range (n):
    array.append(input("Give a distance: "))
m=input("give the max num")
def maxDistance(array,m,n):
    array.sort()
    print array
    f=0
    while f<m:
        if f==m:
            print "Max sum ",m
            break
        for i in range(n,0,-1):
            print array[i-1]
            if array[i-1]<=m:
                k=i-1
                print k
                y=m-array[k]
                break
        if y not in array:
            for i in range(k,0,-1):
                print "In for ",i
                spot=len(array)-i
                print spot
                if array[spot]<m and m-f>0:
                         f+=array[spot]
                if array[0]+k>m:
                    print "The max sum is f",f
                    break
        else:
            print "The max sum is k",array[k]
            break
        
maxDistance(array,m,n)
