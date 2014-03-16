#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
#Euler #72

def phi_sieve_1(N):

   # O(n) phi sieve
   MAXN = N
   phi = [0]*(MAXN+1)
   prime = [0]*(MAXN//10) # ONLY CORRECT FOR LARGE N, SMALLER N OUT OF RANGE ERRORS
   sz = 0
   mark = [0]*(MAXN+1)

   for i in range(2,MAXN+1):

      if(not mark[i]):
         phi[i] = i-1;
         prime[sz]= i;
         sz+=1

      j = 0
      while (j < sz and prime[j]*i <= MAXN):

         mark[prime[j]*i]=1

         if(i%prime[j]==0):

            phi[i*prime[j]] = phi[i]*prime[j]
            break

         else:
            phi[i*prime[j]] = phi[i]*(prime[j]-1 )

         j += 1

      # YIELD RESULT HERE
      yield phi[i]

   # OR RETURN COMPLETE LIST HERE
   # return phi


res = sum(phi_sieve_1(1000000))
print res
