import gmpy2
n =

e =

m = 7516789928765

for dp in range(1000000):
    f = gmpy2.gcd(m-pow(m, e*dp, n), n)
    if f > 1:
        print(dp, f)
        p = f
        q = n//p
        print(p*q == n)
        print("******************")
        print(p+q)
        break
