# k = 20
# N = 1
# i = 1
# check = true
# limit = sqrt(k)
# while p[i] <= k
#      a[i] = 1
#      if check then
#          if p[i] <= limit then
#             a[i] = floor( log(k) / log(p[i]) )
#          else
#             check = false
#          end if
#      end if
#      N = N * p[i] ^ a[i]
#      i = i + 1
# end while
# output N
#

# Python program to find the smallest number evenly
# divisible by all number 1 to n
import fractions

# Returns the lcm of first n numbers
def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i)/fractions.gcd(ans, i)
    return ans

# main 
n = 20
print lcm(n)
