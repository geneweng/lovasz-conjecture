"""
Cayley graphs on dihedral groups D_2n with n odd.

Conventions
-----------
D_2n = < r, s | r^n = s^2 = 1, s r s = r^{-1} >.
Rotation r^i is the pair (i, 0); reflection r^i s is the pair (i, 1).
A symmetric generating set is S = R u T where
    R = set of rotation exponents, closed under negation, 0 not in R;
    T = set of reflection exponents (each reflection is an involution).
The Cayley graph Cay(D_2n, S) has vertex set D_2n and edges g ~ g x, x in S.

Structure (n odd)
-----------------
Right multiplication by r^b maps r^i -> r^{i+b} and r^i s -> r^{i-b} s, so the
rotation coset and the reflection coset each induce the circulant Circ(n, R).
Right multiplication by r^a s maps r^i -> r^{i+a} s and r^i s -> r^{i-a}, so
each reflection contributes the perfect matching  i_L ~ (i+a)_R.

Reduction lemmas implemented in `classify` (proofs in NOTES.md)
    L1  R generates Z_n                                   -> Hamiltonian.
    L3  some difference t - t' (t, t' in T) is a unit mod n -> Hamiltonian
        (the 2n-cycle alternating the two reflections).
    L2  |R| >= 4, R generates dZ_n (d > 1): Hamiltonian if the Haar graph
        H(Z_d, T mod d) has a Hamiltonian cycle; in particular if T mod d has a
        unit difference mod d.
    L5  |R| = 2, R = {+-b}, d = gcd(b, n), m = n/d: Hamiltonian if H(Z_d, T mod d)
        has a Hamiltonian cycle C and a lift of C with alternating sum sigma such
        that k b = -sigma (mod n) for some even k with |k| <= 2d.
        `build_L5` constructs the cycle explicitly and it is verified.
Generating sets not settled by these lemmas are reported as "unresolved" and
handed to the Hamiltonian cycle search (Posa rotation heuristic, then DFS).

Usage
-----
    python3 dihedral.py                 # sweep odd composite n < 100 (|T|<=4, |R|<=4)
    python3 dihedral.py n [maxT [maxR]] # one n
"""

import sys
import random
from math import gcd
from itertools import combinations

sys.setrecursionlimit(20000)


# ---------------------------------------------------------------- group / graph

def cayley_graph(n, R, T):
    """Adjacency lists. Vertex 2*i is r^i, vertex 2*i+1 is r^i s."""
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for b in R:
            adj[2 * i].add(2 * ((i + b) % n))
            adj[2 * i + 1].add(2 * ((i - b) % n) + 1)
        for a in T:
            j = (i + a) % n
            adj[2 * i].add(2 * j + 1)
            adj[2 * j + 1].add(2 * i)
    return [sorted(s) for s in adj]


def is_generating(n, R, T):
    """S = R u T generates D_2n iff T nonempty and R u (T - T) generates Z_n."""
    if not T:
        return False
    g = n
    for b in R:
        g = gcd(g, b)
    t0 = min(T)
    for t in T:
        g = gcd(g, t - t0)
    return g == 1


def units(n):
    return [u for u in range(1, n) if gcd(u, n) == 1]


def canonical(n, R, T):
    """Canonical form of (R, T) under Aut(D_2n): r -> r^u, s -> r^v s (n odd).
    R -> uR, T -> uT + v."""
    best = None
    for u in units(n):
        uR = tuple(sorted((u * b) % n for b in R))
        uT = [(u * t) % n for t in T]
        for t in uT:  # translate so that some element of T becomes 0
            key = (uR, tuple(sorted((x - t) % n for x in uT)))
            if best is None or key < best:
                best = key
    return best


def has_unit_difference(n, T):
    return any(gcd(t - t2, n) == 1 for t, t2 in combinations(sorted(T), 2))


# ------------------------------------------------------------ Haar graph tools

def haar_graph(d, A):
    """Bipartite graph on Z_d x {L, R}: i_L ~ (i+a)_R for a in A. Vertex 2i / 2i+1."""
    return cayley_graph(d, (), tuple(set(a % d for a in A)))


def haar_hamiltonian_cycles(d, A, limit=200):
    """Up to `limit` Hamiltonian cycles of H(Z_d, A) through 0_L, as vertex lists."""
    adj = haar_graph(d, A)
    N = 2 * d
    out = []
    path = [0]
    seen = [False] * N
    seen[0] = True

    def rec(v):
        if len(out) >= limit:
            return
        if len(path) == N:
            if 0 in adj[v]:
                out.append(list(path))
            return
        for w in adj[v]:
            if not seen[w]:
                seen[w] = True
                path.append(w)
                rec(w)
                path.pop()
                seen[w] = False

    rec(0)
    return out


# --------------------------------------------------------- Hamiltonian search

def verify_cycle(adj, cyc):
    N = len(adj)
    if cyc is None or len(cyc) != N or len(set(cyc)) != N:
        return False
    return all(cyc[(i + 1) % N] in adj[cyc[i]] for i in range(N))


def posa_search(adj, rng, max_steps=400000):
    """Posa rotation-extension heuristic. Returns a Hamiltonian cycle or None."""
    N = len(adj)
    nbr = [set(a) for a in adj]
    start = rng.randrange(N)
    path = [start]
    pos = [-1] * N
    pos[start] = 0
    steps = 0
    while steps < max_steps:
        steps += 1
        end = path[-1]
        if len(path) == N:
            if start in nbr[end]:
                return path
            # Posa closing: v_0 ~ v_i and v_{N-1} ~ v_{i-1}  =>  cycle
            for w in adj[end]:
                i = pos[w]
                if i + 1 < N and path[i + 1] in nbr[start]:
                    cyc = path[: i + 1] + path[i + 1:][::-1]
                    # cyc: v0..v_i, v_{N-1}..v_{i+1}; closes since v_{i+1} ~ v_0
                    return cyc
        ext = [w for w in adj[end] if pos[w] < 0]
        if ext:
            w = min(ext, key=lambda x: (sum(1 for y in adj[x] if pos[y] < 0), rng.random()))
            pos[w] = len(path)
            path.append(w)
            continue
        # rotate: pick a neighbour w of end inside the path, reverse the tail after w
        cands = [w for w in adj[end] if pos[w] >= 0 and pos[w] < len(path) - 2]
        if not cands:
            # dead end: reverse the whole path and try from the other side
            path.reverse()
            for i, v in enumerate(path):
                pos[v] = i
            continue
        w = rng.choice(cands)
        i = pos[w]
        tail = path[i + 1:][::-1]
        path = path[: i + 1] + tail
        for j in range(i + 1, len(path)):
            pos[path[j]] = j
    return None


def dfs_search(adj, rng, budget=200000):
    """Randomised DFS with Warnsdorff ordering and a feasibility prune."""
    N = len(adj)
    nbr = [set(a) for a in adj]
    start = rng.randrange(N)
    visited = [False] * N
    free_deg = [len(a) for a in adj]
    path = [start]
    visited[start] = True
    for w in adj[start]:
        free_deg[w] -= 1
    nodes = 0
    result = None

    def feasible(end):
        for u in range(N):
            if not visited[u]:
                c = free_deg[u] + (u in nbr[end]) + (u in nbr[start])
                if c < 2:
                    return False
        return True

    def rec(v):
        nonlocal nodes, result
        nodes += 1
        if nodes > budget:
            return True
        if len(path) == N:
            if start in nbr[v]:
                result = list(path)
                return True
            return False
        cands = [w for w in adj[v] if not visited[w]]
        rng.shuffle(cands)
        cands.sort(key=lambda w: free_deg[w])
        for w in cands:
            visited[w] = True
            path.append(w)
            for x in adj[w]:
                free_deg[x] -= 1
            if (len(path) == N or feasible(w)) and rec(w):
                return True
            for x in adj[w]:
                free_deg[x] += 1
            path.pop()
            visited[w] = False
            if result is not None or nodes > budget:
                return True
        return False

    rec(start)
    return result


def find_hamiltonian_cycle(adj, tries=30, seed=0):
    """Posa heuristic with restarts, then DFS. A returned cycle is verified.
    None is NOT a proof of non-Hamiltonicity."""
    rng = random.Random(seed)
    for _ in range(tries):
        cyc = posa_search(adj, rng)
        if cyc is not None and verify_cycle(adj, cyc):
            return cyc
    for _ in range(3):
        cyc = dfs_search(adj, rng)
        if cyc is not None and verify_cycle(adj, cyc):
            return cyc
    return None


# ------------------------------------------------------------- lemma L5

def quotient_cycle_classes(cyc, d):
    """For a Hamiltonian cycle of H(Z_d, A) as a vertex list, return the list of
    (sign, residue) per edge: L->R edges contribute +a, R->L edges -a."""
    out = []
    for idx in range(len(cyc)):
        v, w = cyc[idx], cyc[(idx + 1) % len(cyc)]
        if v % 2 == 0:
            out.append((+1, ((w // 2) - (v // 2)) % d))
        else:
            out.append((-1, ((v // 2) - (w // 2)) % d))
    return out


def find_L5_witness(n, R, T, cycle_limit=500):
    """Search for (quotient cycle, lifts, k) satisfying lemma L5. Returns dict or None."""
    b = R[0]
    d = gcd(n, b)
    m = n // d
    bp = (b // d) % m
    Tbar = sorted(set(t % d for t in T))
    lifts = {res: [t for t in T if t % d == res] for res in Tbar}
    if d > 40:
        return None
    for cyc in haar_hamiltonian_cycles(d, Tbar, limit=cycle_limit):
        classes = quotient_cycle_classes(cyc, d)
        # DP over edges: reachable sigma mod n with back-pointers
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
            if sigma % d:
                continue
            target = (-(sigma // d)) % m
            for k in range(-2 * d, 2 * d + 1, 2):
                if (k * bp - target) % m == 0:
                    # reconstruct lift sequence
                    ts = []
                    s = sigma
                    for layer in range(len(classes), 0, -1):
                        prev, t = layers[layer][s]
                        ts.append(t)
                        s = prev
                    ts.reverse()
                    return {"cycle": cyc, "lifts": ts, "k": k, "d": d, "m": m, "b": b}
    return None


def build_L5(n, R, T, wit):
    """Construct the Hamiltonian cycle promised by lemma L5 from a witness."""
    b, d, m, k = wit["b"], wit["d"], wit["m"], wit["k"]
    ts = wit["lifts"]
    nb = len(ts)  # 2d blobs
    eps = [+1] * ((nb + k) // 2) + [-1] * ((nb - k) // 2)
    cyc = []
    i = 0        # current index within the current blob
    side = 0     # 0 = L (rotations), 1 = R (reflections)
    for blob in range(nb):
        e = eps[blob]
        for step in range(m):
            cyc.append(2 * ((i - step * e * b) % n) + side)
        x = (i + e * b) % n          # exit vertex index
        t = ts[blob]
        if side == 0:
            i, side = (x + t) % n, 1
        else:
            i, side = (x - t) % n, 0
    return cyc


# ------------------------------------------------------------- classification

def classify(n, R, T):
    """Return (tag, detail, witness). tag in {'L1','L3','L2','L5','unresolved'}."""
    R = tuple(sorted(R))
    T = tuple(sorted(T))
    d = n
    for b in R:
        d = gcd(d, b)
    if R and d == 1:
        return "L1", "rotations generate Z_n", None
    if has_unit_difference(n, T):
        return "L3", "two reflections with unit difference", None
    if not R:
        return "unresolved", "reflections only, no unit difference", None
    Tbar = sorted(set(t % d for t in T))
    if len(R) >= 4:
        if has_unit_difference(d, Tbar):
            return "L2", f"|R|>=4, d={d}, T mod d has unit difference", None
        if d <= 40 and haar_hamiltonian_cycles(d, Tbar, limit=1):
            return "L2", f"|R|>=4, d={d}, H(Z_d, T mod d) Hamiltonian by search", None
        return "unresolved", f"|R|>=4, d={d}, Haar graph H(Z_{d}, {Tbar}) not settled", None
    wit = find_L5_witness(n, R, T)
    m = n // d
    if wit is not None:
        return "L5", f"|R|=2, d={d}, m={m}, quotient cycle lifted with k={wit['k']}", wit
    return "unresolved", f"|R|=2, d={d}, m={m}: no quotient cycle lifts", None


# ---------------------------------------------------------------- enumeration

def hard_generating_sets(n, max_T=None, max_R=None):
    """Generating sets (R, T), up to Aut(D_2n), with
    - R contained in a proper subgroup dZ_n (possibly empty),
    - T without unit differences,
    - S generating, |S| >= 3.
    T is enumerated inside cosets pZ_n for primes p | n, which is exhaustive when n
    has at most two distinct prime factors (NOTES.md, Lemma 4)."""
    primes = [p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, p))]
    seen = set()
    out = []
    T_cands = set()
    for p in primes:
        base = list(range(0, n, p))
        top = len(base) if max_T is None else min(len(base), max_T)
        for k in range(1, top + 1):
            for T in combinations(base, k):
                if 0 in T:
                    T_cands.add(T)
    R_cands = {()}
    for d in range(2, n):
        if n % d:
            continue
        pos = [x for x in range(d, n, d) if x < n - x]
        top = len(pos) if max_R is None else min(len(pos), max_R // 2)
        for k in range(1, top + 1):
            for P in combinations(pos, k):
                R_cands.add(tuple(sorted(list(P) + [n - x for x in P])))
    for T in sorted(T_cands, key=lambda t: (len(t), t)):
        if has_unit_difference(n, T):
            continue
        for R in R_cands:
            if len(R) + len(T) < 3 or not is_generating(n, R, T):
                continue
            key = canonical(n, R, T)
            if key not in seen:
                seen.add(key)
                out.append(key)
    return out


# ----------------------------------------------------------------------- main

def run(n, max_T=None, max_R=None, search=True, verbose=True, check_L5=True):
    sets = hard_generating_sets(n, max_T=max_T, max_R=max_R)
    tally = {}
    unresolved, failures, lemma_bugs = [], [], []
    for R, T in sets:
        tag, detail, wit = classify(n, R, T)
        tally[tag] = tally.get(tag, 0) + 1
        if tag == "L5" and check_L5:
            adj = cayley_graph(n, R, T)
            if not verify_cycle(adj, build_L5(n, R, T, wit)):
                lemma_bugs.append((R, T))
        if tag == "unresolved":
            unresolved.append((R, T, detail))
            if search:
                adj = cayley_graph(n, R, T)
                ok = verify_cycle(adj, find_hamiltonian_cycle(adj))
                if not ok:
                    failures.append((R, T))
                if verbose:
                    print(f"  n={n} R={R} T={T}: {detail}; HC found: {ok}", flush=True)
    if verbose:
        print(f"n={n} (order {2*n}): {len(sets)} hard generating sets up to Aut; "
              + ", ".join(f"{k}={v}" for k, v in sorted(tally.items())), flush=True)
        if lemma_bugs:
            print(f"  !!! L5 construction FAILED verification on {lemma_bugs}", flush=True)
        if failures:
            print(f"  !!! search failed on {len(failures)} sets: {failures}", flush=True)
    return sets, tally, unresolved, failures, lemma_bugs


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        for n in range(9, 100, 2):
            if any(n % p == 0 for p in range(2, n)):  # composite
                run(n, max_T=4, max_R=4)
    else:
        n = int(args[0])
        mt = int(args[1]) if len(args) > 1 else None
        mr = int(args[2]) if len(args) > 2 else None
        run(n, max_T=mt, max_R=mr)
