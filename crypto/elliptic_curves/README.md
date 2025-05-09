# Elliptic Curve Cryptorgraphy (ECC)

Good Resources
1. https://cryptohack.org/challenges/ecc/


Formally understanding the concepts requires some knowledge of
[groups](https://en.wikipedia.org/wiki/Group_(mathematics)) and
[fields](https://en.wikipedia.org/wiki/Field_(mathematics)), however applying
the mathematics may be approachable without these prerequisites. Nevertheless I
recommend understanding the definitions of these terms.

Python is the recommended langauge for these problems because of the built in
`pow(base, exp, mod)` function. No need to fiddle with [Fermat's little
theorem](https://brilliant.org/wiki/fermats-little-theorem/).
Included is a basic point addition and group exponentiation (scalar
multiplication) script written in python.
