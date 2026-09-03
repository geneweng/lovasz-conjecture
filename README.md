# Lovász conjecture

Work toward settling the Lovász conjecture: prove it, or construct a counterexample.

## The problem

**Conjecture (Lovász, 1969).** Every finite connected vertex-transitive graph has a Hamiltonian path.

Two stronger forms are studied alongside it:

- Every finite connected vertex-transitive graph has a Hamiltonian cycle, except for five known graphs: K2, the Petersen graph, the Coxeter graph, and the truncations of the last two.
- Every connected Cayley graph on a group with at least three elements has a Hamiltonian cycle.

All three statements are open. Babai conjectured the opposite: that infinitely many vertex-transitive graphs have no cycle longer than (1 − c)n for some fixed c > 0.

## Goal

Either

1. a proof of one of the statements above (the Cayley graph form, or a substantial new class of groups or orders, would already be significant), or
2. a sixth connected vertex-transitive graph with no Hamiltonian cycle, or a connected vertex-transitive graph with no Hamiltonian path.

## Contents

- [lovasz-conjecture-survey.md](lovasz-conjecture-survey.md): a survey of the conjecture, its variants, known results by graph order, group class and density, long-cycle bounds, the directed setting, and open problems, with references through September 2026. Read this first.
- [dihedral/](dihedral/): work on Cayley graphs of dihedral groups D₂ₙ with n odd. `NOTES.md` has the reductions and proofs: the prism theorem (any generating set containing a rotation gives a Hamiltonian cycle) reduces the case to Haar graphs of odd cyclic groups, and the factor group lemma at the smallest prime settles those when n has at most three distinct prime factors. Together: every connected Cayley graph on D₂ₙ with n odd having at most three distinct prime factors is Hamiltonian. The first open case is n = 1155. `dihedral.py`, `haar.py` and `coverage.py` are the enumeration, certification and search tools; `*.log` files are their outputs.

## Starting points

The survey's open-problem list identifies the smallest unresolved cases. The ones most amenable to direct attack:

- Cayley graphs on dihedral groups of order 2n with n odd.
- Cubic Cayley graphs with a (2, s, 3)-presentation where s ≡ 2 (mod 4) and the group order is divisible by 4.
- Vertex-transitive graphs of order 5p and imprimitive graphs of order 2pq.
- Computational search for counterexamples beyond the existing censuses (cubic vertex-transitive graphs up to 1280 vertices contain none).
