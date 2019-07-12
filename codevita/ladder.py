# # def countWays(n) :
# #     a = 1
# #     b = 1
# #     c = 2
# #     if n==1:
# #       return 1
# #     if n==2:
# #       return 2
# #
# #     for i in range(3, n + 1) :
# #         d = a + b + c
# #         a = b
# #         b = c
# #         c = d
# #
# #     return d%1000000007
# #
# # n = int(input())
# # print(countWays(n))
#
# def noOfWays(n):
#     a_pos = (19 + 3*(33**.5))**(1./3)
#     a_neg = (19 - 3*(33**.5))**(1./3)
#     b = (586 + 102*(33**.5))**(1./3)
#     return round(3*b * ((1./3) * (a_pos+a_neg+1))**(n+1) / (b**2 - 2*b + 4))
# #
# # def approx2(n):
# #     return round((0.618363 * 1.8392**n + \
# #                   (0.029252 + 0.014515j) * (-0.41964 - 0.60629j)**n + \
# #                   (0.029252 - 0.014515j) * (-0.41964 - 0.60629j)**n).real)

def multiply(T, M):

    a = (T[0][0] * M[0][0] + T[0][1] *
         M[1][0] + T[0][2] * M[2][0])
    b = (T[0][0] * M[0][1] + T[0][1] *
         M[1][1] + T[0][2] * M[2][1])
    c = (T[0][0] * M[0][2] + T[0][1] *
         M[1][2] + T[0][2] * M[2][2])
    d = (T[1][0] * M[0][0] + T[1][1] *
         M[1][0] + T[1][2] * M[2][0])
    e = (T[1][0] * M[0][1] + T[1][1] *
         M[1][1] + T[1][2] * M[2][1])
    f = (T[1][0] * M[0][2] + T[1][1] *
         M[1][2] + T[1][2] * M[2][2])
    g = (T[2][0] * M[0][0] + T[2][1] *
         M[1][0] + T[2][2] * M[2][0])
    h = (T[2][0] * M[0][1] + T[2][1] *
         M[1][1] + T[2][2] * M[2][1])
    i = (T[2][0] * M[0][2] + T[2][1] *
         M[1][2] + T[2][2] * M[2][2])

    T[0][0] = a
    T[0][1] = b
    T[0][2] = c
    T[1][0] = d
    T[1][1] = e
    T[1][2] = f
    T[2][0] = g
    T[2][1] = h
    T[2][2] = i

# Recursive function to raise
# the matrix T to the power n
def power(T, n):

    # base condition.
    if (n == 0 or n == 1):
        return;
    M = [[ 1, 1, 1 ],
                [ 1, 0, 0 ],
                [ 0, 1, 0 ]]

    # recursively call to
    # square the matrix
    power(T, n // 2)

    # calculating square
    # of the matrix T
    multiply(T, T)

    # if n is odd multiply
    # it one time with M
    if (n % 2):
        multiply(T, M)

def tribonacci(n):

    T = [[ 1, 1, 1 ],
        [1, 0, 0 ],
        [0, 1, 0 ]]

    # base condition
    if (n == 0 or n == 1):
        return 0
    else:
        power(T, n - 2)

    # T[0][0] contains the
    # tribonacci number so
    # return it
    return T[0][0]


n = int(input())
print(tribonacci(n+2)%1000000007)
