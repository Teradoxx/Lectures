# Elliptic Curve Cryptorgraphy (ECC)

Good Resources
1. [Cryptohack](https://cryptohack.org/challenges/ecc/) - A cool website for learning cryptography
2. [Sagemath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/index.html) - A powerful python math library
3. [Sage Cell Server](https://sagecell.sagemath.org/) - An online server for Sagemath


Formally understanding the concepts requires some knowledge of
[groups](https://en.wikipedia.org/wiki/Group_(mathematics)) and
[fields](https://en.wikipedia.org/wiki/Field_(mathematics)), however applying
the mathematics may be approachable without these prerequisites. Nevertheless I
recommend understanding the definitions of these terms.

Python is the recommended langauge for these problems for a few reasons.
1. `pow(base, exp, mod)` function. No need to fiddle with [Fermat's little theorem](https://brilliant.org/wiki/fermats-little-theorem/).
2. Sagemath/Sympy - both are incredible and convenient python libraries for symbolic calculations, with support for many concepts in cryptography

Included is a basic point addition and group exponentiation (scalar
multiplication) script written in python.
