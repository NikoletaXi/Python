n=input("give a num: ")
for i in range (2,10000):
    plithos=[0 for i in range(10000)]
def isprime(n): #ελεγχω αν ο αριμος που δοθηκε ειναι πρωτος
    if n<=1:
        return False
    d=2
    while d*d <=n:
       if n%d==0:
         return False
       d=d+1
if isprime(n):
    print("ο αριθμος ειναι πρωτος συνεπως δεν αναλυεται σε γινομενο πρωτων παραγοντων")
else:
   for i in range(2,10000):
      while n!=1:
        plithos[i]=0
        isprime(i)
        if isprime(n):
          diairetis=i
          if n%diairetis==0:
              plithos[i]+=1
              while n%diairetis==0:
                  plithos[i]+=1
                  n=n//diairetis
for i in range(2,10000):
       if plithos[i]!=0:
           print("1*plithos[i]")
        
       
      
