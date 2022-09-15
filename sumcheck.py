# 9-13-2022
# MSSG

# Go through and add all 2-digit numbers (0 to 99) to another 2-digit numbers but not repeating any of the digits from the first one.  Do the same for the RHS, again not repeating any of the digits.  (So 8 of the 10 digits from 0 to 9 should be used.)  See how many times the LHS and RHS sums check

# 
count=0
countmatch=0


for i in range(0,10):
  for j in range(0,10):

    if i != j:
      numstr = str(i)+str(j)

      num1 = int(numstr)
      
      for ii in range(0,10):
        for jj in range(0,10):

          if ii != jj and i!=ii and i!=jj and j!=ii and j!=jj  :
            numstr = str(ii)+str(jj)
            num2 = int(numstr)



            for k in range(0,10):
              for l in range(0,10):

                if k != l and k!=i and k!=j and k!=ii and k!=jj   and l!=i and l!=j and l!=ii and l!=jj:
                  numstr = str(k)+str(l)

                  num3 = int(numstr)
      
                  for kk in range(0,10):
                    for ll in range(0,10):

                      if kk != ll and kk!=i and kk!=j and kk!=ii and kk!=jj  and kk!=k and kk!=l and ll!=i and ll!=j and ll!=ii and ll!=jj  and ll!=k and ll!=l: 
                        count+=1
                        numstr = str(kk)+str(ll)
                        num4 = int(numstr)
                        sum1 = num1+num2                        

                        
                        if num1+num2 == num3+num4:
                          print num1,num2,num3,num4, num1+num2,num3+num4
                          countmatch+=1


print count, countmatch

  
