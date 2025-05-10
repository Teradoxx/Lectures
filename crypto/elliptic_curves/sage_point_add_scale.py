from sage.all import FiniteField, EllipticCurve

M = 9739
A = 497
B = 1768
F = FiniteField(M)
E = EllipticCurve(F, [A, B])

P = (1089, 6931)
P = E.point(P)

Q_a = (815, 3190)
Q_a = E.point(Q_a)
n_b = 1829

print(P + P + Q_a)

S = n_b * Q_a
print(S)
