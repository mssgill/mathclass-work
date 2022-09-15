# 9-13-2022
# MSSG

# Go through and add all 1-digit numbers (0 to 9) to another 1-digit number but not repeating the digit from the first one.  Do the same for the RHS, again not repeating any of the digits.  (So 4 of the 10 digits from 0 to 9 should be used.)  See how many times the LHS and RHS sums check.

count=0
countmatch=0


for i in range(1,10):
      for ii in range(1,10):

          if i != ii:

            for k in range(0,10):
              for kk in range(0,10):

                if k != kk and k!=i and k!=ii:

                        count+=1

                        if i*ii == k*kk:
                          print i, ii, k, kk ,  i*ii, k*kk 
                          countmatch+=1



print count, countmatch

  
