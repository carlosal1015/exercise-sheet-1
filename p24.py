#!/usr/bin/env python


beta: int = 2
t: int = 3
L: int = -2
U: int = 2

cardinal = lambda beta, t, L, U: 2 * (beta - 1) * beta ** (t - 1) * (U - L + 1) + 1
x_min = lambda beta, L: beta ** (L - 1)
x_max = lambda beta, U, t: beta**U * (1 - beta ** (-t))

print(f"El cardinal de F(beta, t, L, U) es {cardinal(beta=beta, t=t, L=L, U=U)}.")
print(f"x_min: {x_min(beta=beta, L=L)}")
print(f"x_max: {x_max(beta=beta, U=U, t=t)}")

print()
