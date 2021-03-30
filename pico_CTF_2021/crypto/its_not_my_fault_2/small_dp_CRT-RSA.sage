import time
import numpy as np

#-----------------------------------Fast Interpolation------------------------------------#


def interpolate(n, e, L, m):
    FR. < x > = PolynomialRing(IntegerModRing(n))
    f = prod([(m.powermod(e*l-1, n)*x - 1) for l in range(1, L)])
    print("Done building poly.")
    return f


#----------------------------------------------------------------------------------------#


#-----------------------------------Fast Evaluation--------------------------------------#

# http://www.cecm.sfu.ca/CAG/theses/justine.pdf

class Node:  # binary tree
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def constructTree(nodes, mo):
    FR. < x > = PolynomialRing(IntegerModRing(mo))
    if len(nodes) == 2:
        return Node("Subproduct Tree", nodes[0], nodes[1])
    newnodes = []
    for i in range(len(nodes)-1):
        if i % 2 == 0:
            newnodes.append(
                Node(nodes[i].data*nodes[i+1].data, nodes[i], nodes[i+1]))
    return constructTree(newnodes, mo)


def subproductTree(points, mo):
    FR. < x > = PolynomialRing(IntegerModRing(mo))
    print("Building subproduct tree...")
    base = []
    start = time.time()
    for j in range(len(points)):
        base.append(Node(x-points[j]))
    end = time.time()
    print("Done building base of subproduct tree. Took " +
          str((end-start)/60)+" minutes.")
    start = time.time()
    tree = constructTree(base, mo)
    end = time.time()
    print("Done building subproduct tree. Took " +
          str((end-start)/60)+" minutes.")
    return tree


def downTree(f, tree, mo):
    FR. < x > = PolynomialRing(IntegerModRing(mo))
    if len(f.coefficients()) == 1:
        return f.coefficients()
    start = time.time()
    r0 = f.quo_rem(tree.left.data)[1]
    r1 = f.quo_rem(tree.right.data)[1]
    end = time.time()
    if len(f.coefficients()) == 1:
        return f.coefficients()
    return downTree(r0, tree.left, mo) + downTree(r1, tree.right, mo)

#----------------------------------------------------------------------------------------#

#---------------------------Small RSA-CRT Exponent Algorithm-----------------------------#


def solve(n, e, L, m):
    S = time.time()
    points = []
    print("Starting point calculation...")
    start = time.time()
    for di in range(L):
        if di == 5:
            st = time.time()
        c = m.powermod(e*L*di, n)
        points.append(c)
        if di == 5:
            en = time.time()
            print("Point calculation time remaining: " +
                  str((L-5)*(en-st)/60) + " minutes")
    end = time.time()
    print("Point calculation done. Took " + str((end-start)/60) + " minutes")

    poly = interpolate(n, e, L, m)

    print("Building subproduct tree...")
    tree = subproductTree(points, n)
    print("Evaluating points...")

    evaluations = downTree(poly, tree, n)
    for num in evaluations:
        p = gcd(num, n)
        if p > 1:
            p = Integer(p)
            q = Integer(n)//Integer(p)
            d = e.inverse_mod((p-1)*(q-1))
            dp = e.inverse_mod(p-1)
            dq = e.inverse_mod(q-1)
            E = time.time()
            m, s = divmod(int(E-S), 60)
            h, m = divmod(m, 60)
            print("Total time taken: {} hours, {} minutes, and {} seconds.".format(
                h, m, s+((E-S)-int(E-S))))
            return (p, q, d, dp, dq)

    E = time.time()
    m, s = divmod(int(E-S), 60)
    h, m = divmod(m, 60)
    print("Total time taken: {} hours, {} minutes, and {} seconds.".format(
        h, m, s+((E-S)-int(E-S))))
    print("No solutions found.")
    return (None, None, None, None, None)

#----------------------------------------------------------------------------------------#


DP_BITS = 36
L = 1 << (DP_BITS/2)  # sqrt of max of smaller private exponent

n = 124820867833961512255121751609049306179897666404096891662718071264088624606195417583639161066276975279640599118437354335640828498035985542095139168119692839404116968042389114810846687132156292424607681366934277727898599922856113752913454673986423798381847193428071452354375463030105066256138253881897882994099
e = 46413346084333645012143147319389347924397373027897998120051654242937480130282545034433967290231436105403203157816717530203079607233722565425714290923944628662988841561125900662835135189696637301075373141006198752365262569240099036001408525284187514463343741272674488593785654318061637768053550355072803501569
m = 2

p, q, d, dp, dq = solve(n, e, L, m)
print("N = ", n)
print("E = ", e)
print("P = ", p)
print("Q = ", q)
print("D = ", d)
print("Dp = ", dp)
print("Dq = ", dq)
print("P + Q = ", (p+q))
