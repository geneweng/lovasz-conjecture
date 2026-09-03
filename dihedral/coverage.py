"""
Which dihedral groups D_2n (n odd) are already covered by published theorems?

Sources (see ../lovasz-conjecture-survey.md, Sections 5.2 and 5.3):
  KW85   Keating-Witte: [G,G] cyclic of prime-power order.  [D_2n, D_2n] = Z_n for n odd,
         so this covers n = p^a.
  KMMMS  Kutnar-Marusic-Morris-Morris-Sparl 2012 (+ 16p, 27p, 30p papers):
         orders kp (k<32, k!=24), kpq (k<6), pqr, kp^2 (k<5), kp^3 (k<3).
  MW20   Morris-Wilk: 6pq.        AMRS23: 8pq.
  M21    Morris: pqrs, all odd.   LMM26: pqrs, distinct primes (any).
Prints the odd n < LIMIT for which order 2n is not covered by any of these.
"""

from math import gcd


def factor(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def covered(order):
    f = factor(order)
    primes = sorted(f)
    exps = [f[p] for p in primes]
    # pqrs / pqr / pq / p : squarefree with <= 4 primes
    if all(e == 1 for e in exps) and len(primes) <= 4:
        return "squarefree, <=4 primes"
    for p in primes:
        k = order // p
        if k < 32 and k != 24:
            return f"kp with k={k}, p={p}"
        if order % (p * p) == 0:
            k = order // (p * p)
            if k < 5:
                return f"kp^2 with k={k}, p={p}"
        if order % (p ** 3) == 0:
            k = order // (p ** 3)
            if k < 3:
                return f"kp^3 with k={k}, p={p}"
    sf = [p for p in primes if f[p] == 1]
    for i in range(len(sf)):
        for j in range(i + 1, len(sf)):
            k = order // (sf[i] * sf[j])
            if k < 6 or k in (6, 8):
                return f"kpq with k={k}"
    return None


if __name__ == "__main__":
    LIMIT = 400
    print("odd n whose dihedral group D_2n is NOT covered by the listed theorems:")
    for n in range(3, LIMIT, 2):
        f = factor(n)
        if len(f) == 1:
            continue  # prime power: Keating-Witte
        why = covered(2 * n)
        if why is None:
            print(f"  n={n:4d}  order {2*n:4d}  n = " + " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items())))
