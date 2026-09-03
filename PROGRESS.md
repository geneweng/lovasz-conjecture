# Progress log

Paused on 2026-09-03. This file is the hand-off: read it first when resuming.

## Goal

Prove the Lovász conjecture (every finite connected vertex-transitive graph has a Hamiltonian path; stronger forms: a Hamiltonian cycle with five known exceptions, or a Hamiltonian cycle in every connected Cayley graph), or construct a counterexample.

## What exists

| Item | Where | State |
|---|---|---|
| Survey of the conjecture, results through September 2026, open problems | `lovasz-conjecture-survey.md`, rendered at `docs/survey.html` | done |
| Odd dihedral case: definitions, reductions, proofs, literature check | `dihedral/NOTES.md`, rendered at `docs/dihedral.html` | done |
| Enumeration and certification tools | `dihedral/dihedral.py`, `dihedral/haar.py`, `dihedral/coverage.py` | working, plain Python 3 |
| Run logs | `dihedral/*.log` | partial, see below |

## Where the dihedral case stands

Target: connected Cayley graphs on D₂ₙ with n odd (the even case is Alspach–Chen–Dean 2010).

1. **Reduction (Theorem 3 in the notes).** If the generating set contains a rotation, the graph is Hamiltonian. Proof: pair the two cosets through the reflection s into blocks that are Cayley graphs on Z_m × Z₂, Hamilton-connected by Chen–Quimpo because m is odd, and chain the blocks along a Hamiltonian cycle of a circulant on Z_d. This is Witte's Theorem 5.3 (1982).
2. **Reflection-only sets are cyclic Haar graphs H(Zₙ, A).** Trivial when two reflections differ by a unit. Otherwise n needs at least three distinct primes (Lemma 2).
3. **Three primes (Theorem H3).** The factor group lemma at the smallest prime p always works: pick two classes of A mod p whose union is non-constant mod q and mod r, mix j copies of a q-divisible difference with p − j copies of an r-divisible one. Verified mechanically on 871 sets (n = 105, 315). This is Witte's Proposition 5.5 (1982), quoted as Lemma 2.22 in Kutnar–Marušič–Morris–Morris–Šparl (2012), and rediscovered as Lemma 5.1 of Bonvicini–Pisanski–Žitnik (2025).
4. **First open case: n = 1155 = 3·5·7·11**, reflection-only sets with |A| ≥ 4 and no unit difference. Bonvicini–Pisanski–Žitnik state the same and call cyclic Haar graphs with odd m of four or more prime-power factors the prominent open cases; their 2026 paper shows these would settle all bicirculants of valence ≥ 4.

So nothing found so far is new, but the notes give self-contained proofs, and the code produces verified Hamiltonian cycles as certificates.

## Computations done

- `dihedral.py`: all generating sets with a rotation that the trivial lemmas miss, up to Aut(D₂ₙ), |T| ≤ 3, |R| ≤ 4, for odd composite n < 100: the sweep reached n = 85 (20 of 25 values) with a Hamiltonian cycle found for every set, as Theorem 3 predicts (`sweep_lt100.log`; an earlier partial run with |T| ≤ 4 reached n = 75, `sweep_lt100_T4_partial.log`).
- `haar.py`: every hard reflection set on Z₁₀₅ with |A| ≤ 6 (73 sets) and on Z₃₁₅ with |A| ≤ 5 (729 sets) is certified by the factor group lemma; the literal Theorem H3 construction verifies on all of them.
- Brute force confirmed Hamilton-connectedness of the Z_m × Z₂ blocks for m ≤ 11.
- The n = 1155 run (`haar.py 1155 4`) never got past enumeration: the clique search over raw elements is far too slow at that size (about 700 elements agree with 0). It was stopped.

## How to resume

1. **Fix the n = 1155 enumeration.** Since 1155 is squarefree, elements correspond to residue vectors in Z₃×Z₅×Z₇×Z₁₁, and the affine group acts coordinatewise. Enumerate 4-point configurations by residue pattern (pairwise agreeing in some coordinate, not constant in any) up to coordinatewise affine equivalence, instead of DFS over 700 elements. Then run `fgl_witness` on each and search on the failures.
2. **If the factor group lemma certifies everything at n = 1155**, look for the four-prime proof: where Step 1 of Theorem H3 fails (every pair of classes constant modulo a shared prime), use quotient cycles through three or more classes or the lemma at a different prime. That would extend Witte's theorem and, via Bonvicini–Pisanski–Žitnik 2026, settle more bicirculants.
3. **If some set resists**, it is a candidate counterexample: run an exact Hamiltonicity test (a SAT encoding; the graph has 2310 vertices and degree 4).
4. Their named open bicirculant B(1155; 105, {0, 33, 110}, 315) is a good stress test for the search code even though it is not a dihedral Cayley graph.
5. Other starting points from the survey's open-problem list: cubic Cayley graphs with (2, s, 3)-presentations for s ≡ 2 mod 4, vertex-transitive graphs of order 5p, imprimitive graphs of order 2pq.

## Commands

```
python3 dihedral/coverage.py          # odd n not covered by published theorems
python3 dihedral/dihedral.py 45 3 4   # one n: |T|<=3, |R|<=4
python3 dihedral/haar.py 315 4        # hard reflection sets, FGL certificates, search
```
