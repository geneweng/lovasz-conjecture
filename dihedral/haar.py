"""
Reflections-only case: Haar graphs H(Z_n, A), n odd.

Cay(D_2n, {r^a s : a in A}) is the bipartite graph with parts Z_n (L) and Z_n (R)
and edges i_L ~ (i+a)_R for a in A.  It is connected iff A - A generates Z_n.

Trivial case: if some a - a' is a unit mod n, the edges labelled a and a' alone
form a Hamiltonian cycle of length 2n.  A "hard" set has no unit difference.
By NOTES.md Lemma 4 a hard generating set exists only if n has at least three
distinct prime factors.  The hard sets are exactly the sets A such that every two
elements agree modulo at least one prime divisor of n, and A is not contained in a
single residue class modulo any prime divisor of n.

This module enumerates hard sets up to the affine group {x -> ux + v} (which is
Aut(D_2n) restricted to reflections), and tests Hamiltonicity by search.

Usage:  python3 haar.py n [max_size]
"""

import sys
from math import gcd
from dihedral import cayley_graph, find_hamiltonian_cycle, verify_cycle, units


def prime_divisors(n):
    ps, m, p = [], n, 2
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        ps.append(m)
    return ps


def agree(x, y, primes):
    return any((x - y) % p == 0 for p in primes)


def generating(A, n, primes):
    return all(len(set(a % p for a in A)) > 1 for p in primes)


def canon(A, n, U):
    best = None
    for u in U:
        uA = [(u * a) % n for a in A]
        for t in uA:
            key = tuple(sorted((x - t) % n for x in uA))
            if best is None or key < best:
                best = key
    return best


def hard_sets(n, max_size=None):
    """All hard generating sets A (0 in A) up to affine equivalence, by DFS over
    cliques of the agreement graph."""
    primes = prime_divisors(n)
    U = units(n)
    if len(primes) < 3:
        return []
    # agreement graph restricted to elements agreeing with 0
    verts = [x for x in range(1, n) if agree(x, 0, primes)]
    nbr = {x: {y for y in verts if y != x and agree(x, y, primes)} for x in verts}
    found = set()
    out = []

    def rec(A, cand):
        if generating(A, n, primes):
            key = canon(A, n, U)
            if key not in found:
                found.add(key)
                out.append(key)
        if max_size is not None and len(A) >= max_size:
            return
        cand = sorted(cand)
        for i, x in enumerate(cand):
            rec(A + [x], [y for y in cand[i + 1:] if y in nbr[x]])

    rec([0], verts)
    out.sort(key=lambda a: (len(a), a))
    return out


def residue_pattern(A, primes):
    return [tuple(a % p for p in primes) for a in A]


# ------------------------------------------------- factor group lemma at a prime

def fgl_witness(n, A, primes, max_cycles=2000):
    """Factor group lemma with N = pZ_n for a prime p | n.
    Quotient: H(Z_p, A mod p). A Hamiltonian cycle of the quotient with lifts
    t_1..t_{2p} in A has voltage sigma = t_1 - t_2 + t_3 - ... - t_{2p}; the lifted
    walk is a Hamiltonian cycle of H(Z_n, A) iff gcd(sigma, n) = p.
    Returns (p, lifts) or None."""
    from dihedral import haar_hamiltonian_cycles, quotient_cycle_classes
    for p in primes:
        Abar = sorted(set(a % p for a in A))
        if len(Abar) < 2:
            continue
        lifts = {res: [a for a in A if a % p == res] for res in Abar}
        for cyc in haar_hamiltonian_cycles(p, Abar, limit=max_cycles):
            classes = quotient_cycle_classes(cyc, p)
            layers = [{0: None}]
            for sign, res in classes:
                nxt = {}
                for s in layers[-1]:
                    for t in lifts[res]:
                        s2 = (s + sign * t) % n
                        if s2 not in nxt:
                            nxt[s2] = (s, t)
                layers.append(nxt)
            for sigma in layers[-1]:
                if gcd(sigma, n) == p:
                    ts, s = [], sigma
                    for layer in range(len(classes), 0, -1):
                        prev, t = layers[layer][s]
                        ts.append(t)
                        s = prev
                    ts.reverse()
                    return p, ts
    return None


def theorem_h3_cycle(n, A, primes):
    """Follow the proof of Theorem H3 (NOTES.md) literally, for n with exactly
    three distinct prime factors p < q < r:
      1. classes of A mod p; pick classes X, Y whose union is non-constant mod q
         and mod r;
      2. pick d in Y - X with q | d, r does not divide d, and d' in Y - X with
         r | d', q does not divide d';
      3. for some j in 1..p-1, sigma = j d + (p-j) d' has gcd(sigma, n) = p;
      4. lift the alternating (Y, X) cycle of H(Z_p, A mod p) n/p times.
    Returns the Hamiltonian cycle (a vertex list) or raises AssertionError
    when a step of the proof fails, which would mean the proof is wrong."""
    assert len(primes) == 3
    p, q, r = primes
    classes = {}
    for a in A:
        classes.setdefault(a % p, []).append(a)
    pair = None
    for c1 in classes:
        for c2 in classes:
            if c1 == c2:
                continue
            U = classes[c1] + classes[c2]
            if len(set(u % q for u in U)) > 1 and len(set(u % r for u in U)) > 1:
                pair = (classes[c1], classes[c2])
                break
        if pair:
            break
    assert pair is not None, "no pair of classes non-constant mod q and mod r"
    X, Y = pair
    D = [(y, x) for y in Y for x in X]
    dq = next(((y, x) for y, x in D if (y - x) % q == 0 and (y - x) % r != 0), None)
    dr = next(((y, x) for y, x in D if (y - x) % r == 0 and (y - x) % q != 0), None)
    assert dq is not None and dr is not None, "missing q-type or r-type difference"
    (y, x), (y2, x2) = dq, dr
    for j in range(1, p):
        sigma = j * (y - x) + (p - j) * (y2 - x2)
        if gcd(sigma % n, n) == p:
            ts = [y, x] * j + [y2, x2] * (p - j)
            cyc = build_fgl(n, A, p, ts)
            assert verify_cycle(cayley_graph(n, (), A), cyc), "lifted walk is not a Hamiltonian cycle"
            return cyc
    raise AssertionError("no j in 1..p-1 gives gcd(sigma, n) = p")


def build_fgl(n, A, p, ts):
    """Lift the quotient cycle with reflection labels ts (length 2p) n/p times."""
    cyc = []
    i, side = 0, 0
    for _ in range(n // p):
        for t in ts:
            cyc.append(2 * i + side)
            if side == 0:
                i, side = (i + t) % n, 1
            else:
                i, side = (i - t) % n, 0
    return cyc


if __name__ == "__main__":
    n = int(sys.argv[1])
    max_size = int(sys.argv[2]) if len(sys.argv) > 2 else None
    primes = prime_divisors(n)
    sets = hard_sets(n, max_size)
    print(f"n={n} primes={primes}: {len(sets)} hard reflection sets up to equivalence"
          + (f" (|A| <= {max_size})" if max_size else ""), flush=True)
    by_size = {}
    for A in sets:
        by_size[len(A)] = by_size.get(len(A), 0) + 1
    print("  sizes:", dict(sorted(by_size.items())), flush=True)
    fails, fgl_fails, fgl_bugs = [], [], []
    for A in sets:
        adj = cayley_graph(n, (), A)
        w = fgl_witness(n, A, primes)
        if w is not None:
            p, ts = w
            if verify_cycle(adj, build_fgl(n, A, p, ts)):
                continue  # proved Hamiltonian by an explicit lifted cycle
            fgl_bugs.append(A)
        else:
            fgl_fails.append(A)
            print(f"  FGL fails: A={A} residues={residue_pattern(A, primes)}", flush=True)
        cyc = find_hamiltonian_cycle(adj)
        ok = verify_cycle(adj, cyc)
        if not ok:
            fails.append(A)
            print(f"  NOT FOUND: A={A} residues={residue_pattern(A, primes)}", flush=True)
    print(f"  factor group lemma at a prime certifies {len(sets) - len(fgl_fails) - len(fgl_bugs)} of {len(sets)}", flush=True)
    print(f"  Hamiltonian cycle found by search for all of the remaining {len(fgl_fails) + len(fgl_bugs)}: {not fails}", flush=True)
    if fgl_bugs:
        print("  !!! FGL witness failed verification:", fgl_bugs)
    if fails:
        print("  search failures (not proofs of non-Hamiltonicity):", fails)
