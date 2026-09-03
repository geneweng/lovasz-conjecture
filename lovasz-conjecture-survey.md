# The Lovász Conjecture on Hamiltonian Paths in Vertex-Transitive Graphs: A Survey

*Status as of September 2026.*

## Abstract

The Lovász conjecture (1969) asserts that every finite connected vertex-transitive graph has a Hamiltonian path. Its stronger and more commonly studied form asserts a Hamiltonian cycle, with exactly five known exceptions, and its most-studied special case asserts that every connected Cayley graph on a group of order at least three is Hamiltonian. All three statements are open. This survey collects the statements and their history, the structural facts that constrain any counterexample, the results organized by order of the graph, by class of group, and by density, the quantitative "long cycle" program that has advanced rapidly since 2023, the directed setting where the conjecture is false, and the main open problems.

## 1. The conjecture and its variants

### 1.1 Definitions

A graph $\Gamma$ is *vertex-transitive* if its automorphism group acts transitively on the vertex set. For a finite group $G$ and a subset $S \subseteq G \setminus \{1\}$ with $S = S^{-1}$, the *Cayley graph* $\mathrm{Cay}(G,S)$ has vertex set $G$ and an edge between $g$ and $gs$ for every $s \in S$. It is connected exactly when $S$ generates $G$, and left multiplication makes it vertex-transitive. By Sabidussi's theorem a vertex-transitive graph is a Cayley graph if and only if its automorphism group contains a subgroup acting regularly on the vertices. Not every vertex-transitive graph is a Cayley graph; the Petersen graph is the smallest example. The *Cayley digraph* $\overrightarrow{\mathrm{Cay}}(G,S)$ is defined the same way without the symmetry requirement on $S$.

A *Hamiltonian path* visits every vertex exactly once, and a *Hamiltonian cycle* is a closed such path. A graph with a Hamiltonian cycle is called *Hamiltonian*.

### 1.2 The statements

Four statements circulate under the name "Lovász conjecture". They are listed from weakest to strongest in the undirected case, followed by the directed variant.

**Conjecture A (Hamiltonian path).** Every finite connected vertex-transitive graph has a Hamiltonian path.

**Conjecture B (Hamiltonian cycle).** Every finite connected vertex-transitive graph has a Hamiltonian cycle, except for the five known exceptions listed in 1.3.

**Conjecture C (Cayley graphs).** Every connected Cayley graph on a finite group with at least three elements has a Hamiltonian cycle.

**Conjecture D (Cayley digraphs).** The corresponding statement for directed Cayley graphs is *false*. Rankin's theorem (Section 6.1) produces infinitely many connected Cayley digraphs on two generators with no directed Hamiltonian cycle, and Morris (2013) produced infinitely many with no directed Hamiltonian path.

Conjecture B implies A. Conjecture C is the special case of B in which the graph is a Cayley graph, and it is consistent with the five exceptions because none of them is a Cayley graph. Most of the literature since the 1980s addresses Conjecture C or Conjecture B restricted to graphs of a given order.

### 1.3 The five exceptions

The connected vertex-transitive graphs known to have no Hamiltonian cycle are:

1. the complete graph $K_2$;
2. the Petersen graph (10 vertices, cubic);
3. the Coxeter graph (28 vertices, cubic);
4. the truncation of the Petersen graph (30 vertices), obtained by replacing each vertex with a triangle;
5. the truncation of the Coxeter graph (84 vertices).

All five have Hamiltonian paths, so none contradicts Conjecture A. The Petersen and Coxeter graphs are hypohamiltonian: deleting any single vertex leaves a Hamiltonian graph. Truncation of a cubic arc-transitive graph yields a cubic vertex-transitive graph, and a Hamiltonian cycle in the truncation would force a Hamiltonian cycle in the original graph, which explains items 4 and 5. Truncating again does not produce a vertex-transitive graph, so the construction stops there. Among the generalized Petersen graphs $GP(n,2)$, Alspach (1983) showed that the non-Hamiltonian ones are exactly those with $n \equiv 5 \pmod 6$, but only $GP(5,2)$, the Petersen graph itself, is vertex-transitive.

### 1.4 History and original wording

Lovász posed the problem at the 1969 Calgary conference (published 1970 in *Combinatorial Structures and Their Applications*, Problem 11). The original wording asks for a construction in the negative direction: "Let us construct a finite, connected undirected graph, which is symmetric and has no simple path containing all the vertices." Pak and Radoičić (2009) note that the problem is therefore "misnamed" as a conjecture, since Lovász framed it as a search for a counterexample. Lovász was motivated by a question of Gallai on whether all longest paths of a connected graph share a vertex; for vertex-transitive graphs a positive answer would force every longest path to be Hamiltonian. Gallai's question was answered negatively by Walther.

The problem has older roots. Rankin (1948) studied Hamiltonian cycles in two-generated Cayley digraphs to settle a question in English change ringing (campanology): whether an extent of Grandsire Triples can be rung using only plain leads and bobs. His negative answer, now known as Rankin's campanological theorem, is the earliest general non-Hamiltonicity result for Cayley digraphs. Rapaport-Strasser (1959) asked explicitly whether every Cayley graph has a Hamiltonian cycle and proved the three-involution lemma in Section 5.6, motivated by bell ringing and the knight's tour. Knuth treats the topic in *The Art of Computer Programming* Volume 4A, Section 7.2.1.2, and the general problem is closely tied to combinatorial Gray codes, where a Hamiltonian path in a Cayley graph gives a listing of all group elements in which consecutive elements differ by one generator.

### 1.5 The opposing conjectures

Babai (1996, *Handbook of Combinatorics*, Section 3.3) argued that belief in the conjecture "only reflects that Hamiltonicity obstacles are not well understood", and conjectured the opposite:

**Babai's conjecture.** There is a constant $c > 0$ such that infinitely many connected vertex-transitive graphs, and indeed Cayley graphs, on $n$ vertices have no cycle of length at least $(1-c)n$.

At the other extreme, Thomassen conjectured that there are only finitely many connected vertex-transitive non-Hamiltonian graphs. Mohar proposed intermediate statements: that every connected vertex-transitive graph has a 2-walk, meaning a closed walk visiting every vertex at most twice, and that every such graph has a spanning tree of maximum degree 3. Conjecture A implies the first of these, which implies the second, and no progress on distinguishing these possibilities has been made. It is not known whether a single counterexample to Conjecture A would generate infinitely many.

## 2. Structure and obstructions

Several standard obstructions to Hamiltonicity are unavailable for vertex-transitive graphs, which partly explains why no sixth exception has appeared.

- **Connectivity.** Watkins (1970) proved that a connected vertex-transitive graph of degree $d$ has vertex connectivity at least $2(d+1)/3$, and Mader proved the same for edge connectivity $d$. High connectivity rules out cut-vertex obstructions.
- **Toughness.** Babai observed that connected Cayley graphs are 1-tough: removing $k$ vertices leaves at most $k$ components. Chvátal's toughness obstruction therefore never applies, and any counterexample among Cayley graphs would also be a counterexample to the folklore expectation that tough enough graphs are Hamiltonian.
- **Bipartite parity.** A bipartite graph with unequal sides has no Hamiltonian cycle, but a vertex-transitive bipartite graph is regular and hence balanced.
- **Expansion.** Cayley graphs with many random generators are expanders (Alon and Roichman 1994), and expanders contain paths of length $(1-c)n$ (Pósa). Whether bounded-degree expansion forces Hamiltonicity is one of the questions Babai raises.

The main constructive tool is the *lifting* or *quotient* method. A semiregular automorphism $\rho$ of order $m$ with $k$ orbits, called $(k,m)$-semiregular, defines a quotient graph on the orbits. A Hamiltonian cycle in the quotient can sometimes be lifted to a Hamiltonian cycle in $\Gamma$ when the "voltage" accumulated around the quotient cycle generates $\langle \rho \rangle$. For Cayley graphs this is the Factor Group Lemma of Witte and Gallian: if $N$ is a cyclic normal subgroup of $G$ and $\mathrm{Cay}(G/N, S)$ has a Hamiltonian cycle whose product of generators generates $N$, then $\mathrm{Cay}(G,S)$ has a Hamiltonian cycle. Marušič's polycirculant conjecture (1981), that every vertex-transitive graph has a nontrivial semiregular automorphism, is what makes the quotient method broadly available; it is known for cubic graphs and for many orders but is itself open. Kutnar and Marušič (2009) survey this circle of ideas.

## 3. Vertex-transitive graphs by order

Most results on Conjecture B outside the Cayley setting classify the transitive permutation groups of a given degree, usually using the classification of finite simple groups for the primitive case and semiregular automorphisms for the imprimitive case. The table lists what is known for orders with few prime factors, where $p, q$ are distinct primes.

| Order | Hamiltonian path | Hamiltonian cycle |
|---|---|---|
| $p$ | yes (circulants) | yes |
| $2p$ | yes | yes except Petersen (Alspach 1979) |
| $3p$ | yes | yes (Marušič 1985) |
| $4p$ | yes (Marušič and Parsons 1983) | yes (Kutnar and Marušič 2008) |
| $5p$ | yes (Marušič and Parsons 1982) | open in general |
| $6p$ | yes (Kutnar and Šparl 2009) | yes except truncated Petersen (Du and Zhou 2025) |
| $10p$, $p \ne 7$ | yes (Kutnar, Marušič and Zhang 2012; Du, Luo and Yu 2024 for the remaining $\mathrm{PSL}(2,s^m)$ family) | partial |
| $pq$ | yes | yes except Petersen (Du, Kutnar and Marušič 2021) |
| $2pq$ | partial | primitive case: yes except Coxeter (Du, Tian and Yu 2022); imprimitive case partially settled (Zhou 2026) |
| $p^2$, $p^3$ | yes | yes (Marušič 1985; all such graphs are Cayley) |
| $p^4$ | yes | yes (Chen 1998) |
| $p^5$ | yes | open |
| $2p^2$ | yes | yes |

Two points deserve emphasis. First, the product-of-two-primes theorem of Du, Kutnar and Marušič, published in *Combinatorica* in 2021, was the first order result whose proof needed classical Hamiltonicity theorems of Chvátal and Jackson together with number-theoretic facts about quadratic residues, which suggests that further order results will not be purely group-theoretic. Second, the exceptions appearing in the $2p$, $6p$ and $2pq$ rows are exactly the known five, so the order program has so far confirmed Conjecture B rather than merely Conjecture A.

## 4. Long cycles in vertex-transitive graphs

Babai (1979) initiated the quantitative version of the problem: how long a cycle must a connected vertex-transitive graph on $n$ vertices contain? His argument gave $\sqrt{3n}$, and this stood for over forty years. Since 2023 the exponent has moved quickly.

| Bound on longest cycle | Reference |
|---|---|
| $\sqrt{3n}$ | Babai 1979 |
| $(1-o(1))\,n^{3/5}$ | DeVos 2023 |
| $\Omega(n^{13/21})$ | Groenland, Longbrake, Steiner, Turcotte and Yepremyan 2025 |
| $\Omega(n^{9/14})$ | Norin, Steiner, Thomassé and Wollan 2025 |
| $n^{2/3 - o(1)}$ | Bucić, Christoph, Pokrovskiy and Steiner 2026 |

DeVos's proof modifies Babai's original argument. The two 2025 papers analyze intersections of longest cycles and small transversals of them. Bucić, Christoph, Pokrovskiy and Steiner combine path embedding in sublinear expanders with expander decompositions, and they note that the exponent $2/3$ is a natural barrier for the existing approaches. The gap between $n^{2/3}$ and the linear cycles predicted by Babai's conjecture, let alone the Hamiltonian cycles predicted by Lovász, remains large.

For vertex-transitive *digraphs* the picture is different. Bucić, Hendrey, Mohar, Steiner and Yepremyan (2026) proved a lower bound of $\Omega(n^{1/3})$ for the longest directed cycle and constructed connected vertex-transitive digraphs whose longest directed cycle misses about $\log n$ vertices. Li and Methuku (2026) improved the lower bound to $\Omega(\sqrt{n})$ and constructed infinitely many connected vertex-transitive digraphs whose longest directed cycle misses at least $n/12$ vertices, answering a question of Alspach from 1981. So the directed analogue of Babai's conjecture is true.

## 5. Cayley graphs

### 5.1 Abelian groups and p-groups

Every connected Cayley graph on an abelian group with at least three elements has a Hamiltonian cycle; this is an easy induction and is folklore. Chen and Quimpo (1981) proved much more: such a graph of degree at least 3 is Hamilton-connected, or Hamilton-laceable when bipartite. Witte (1986) proved that every connected Cayley *digraph* on a $p$-group has a directed Hamiltonian cycle, so in particular Conjecture C holds for all $p$-groups.

### 5.2 Groups with small commutator subgroup

A long line of work, mostly by Dave Witte Morris and coauthors, proves Conjecture C when the commutator subgroup $[G,G]$ is small or cyclic. The proofs use the Factor Group Lemma and increasingly elaborate case analysis.

- $[G,G]$ cyclic of prime order: Marušič (1983) and Durnberger (1983).
- $[G,G]$ cyclic of prime-power order: Keating and Witte (1985).
- $G$ nilpotent and $[G,G]$ cyclic: Ghaderpour and Morris (2014).
- $|G|$ odd and $[G,G]$ cyclic of order $p^m q^n$: Morris (2015).
- $|[G,G]| = 2p$ for an odd prime $p$: Morris (2018).
- Lehner, Maghsoudi and Miraftab (2024) extended Durnberger's theorem to infinite vertex-transitive graphs whose automorphism group has a transitive subgroup with commutator subgroup of prime order.

### 5.3 Groups whose order has few prime factors

Kutnar, Marušič, Morris, Morris and Šparl (2012) organized a program of settling Conjecture C for all groups of a given small order. With later additions the list of orders for which every connected Cayley graph is Hamiltonian includes, for distinct primes $p, q, r, s$:

| Order | Reference |
|---|---|
| $kp$ with $k < 32$, $k \ne 24$ | Kutnar, Marušič, Morris, Morris and Šparl 2012; Curran, Morris and Morris 2012 ($16p$); Ghaderpour and Morris 2011 ($27p$, $30p$) |
| $kpq$ with $k < 6$ | Kutnar, Marušič, Morris, Morris and Šparl 2012 |
| $6pq$ | Morris and Wilk 2020 |
| $8pq$ | Abedi, Morris, Rezaee and Salarian 2023 (computer-assisted) |
| $pqr$ | Kutnar, Marušič, Morris, Morris and Šparl 2012 |
| $pqrs$, all odd | Morris 2021 |
| $pqrs$ | Lehner, Maghsoudi and Miraftab 2026 |
| $kp^2$ with $k < 5$ | Kutnar, Marušič, Morris, Morris and Šparl 2012 |
| $kp^3$ with $k < 3$ | Kutnar, Marušič, Morris, Morris and Šparl 2012 |

The general pattern is that a group of such an order is solvable with a normal Sylow subgroup, so the Factor Group Lemma applies to a chain of cyclic quotients, and the difficult cases are the few generating sets for which the lemma's hypothesis fails. The 2026 result of Lehner, Maghsoudi and Miraftab removes the oddness restriction from Morris's $pqrs$ theorem and is the first order result covering a family with four prime factors and even order.

### 5.4 Dihedral and generalized dihedral groups

Conjecture C is open for dihedral groups $D_{2n}$, a fact that is often cited as evidence of how little is understood. Known cases:

- Alspach and Zhang (1989): every cubic Cayley graph on a dihedral group is Hamiltonian, via brick products.
- Alspach, Chen and Dean (2010): every connected Cayley graph on a generalized dihedral group has a Hamiltonian path; when the order is divisible by 4 and the degree is at least 3 the graph is Hamilton-connected or, if bipartite, Hamilton-laceable. In particular Conjecture C holds for $D_{2n}$ with $n$ even.
- The case $n$ odd remains open. A 2018 preprint claiming the general generalized dihedral case was withdrawn by its authors because of an error.
- Miraftab (2022) treated generalized quasi-dihedral groups.

### 5.5 Symmetric groups and combinatorial generation

Cayley graphs on $S_n$ are the natural home of permutation generation algorithms, and results here usually come with efficient listing algorithms.

- Adjacent transpositions $(i, i+1)$: the Steinhaus–Johnson–Trotter algorithm produces a Hamiltonian cycle in the permutohedron. Conway, Sloane and Wilks (1989) extended this to Coxeter generators of any finite reflection group.
- Any set of transpositions forming a tree on $\{1, \dots, n\}$: Kompel'makher and Liskovets (1975) proved Hamiltonicity, and Tchuente (1982) proved Hamilton-laceability for any connected set of transpositions.
- A long cycle $\sigma = (1\,2\,\cdots\,n)$ and a transposition $\tau = (1\,2)$: the undirected graph is Hamiltonian (Compton and Williamson 1993). The *directed* sigma–tau digraph, generated by $\sigma$ and $\tau$ without inverses, was Knuth's problem rated 48 out of 50 in difficulty. Rankin's theorem shows it has no directed Hamiltonian cycle for even $n$. Sawada and Williams (2018, 2020) gave a directed Hamiltonian path for every $n$ and a directed Hamiltonian cycle for every odd $n$, with an $O(n)$-time successor rule, settling a problem of Nijenhuis and Wilf open since the 1970s.
- The involutions $(1\,2)$, $(1\,2)(3\,4)\cdots$ and $(2\,3)(4\,5)\cdots$: Hamiltonian by the Rapaport-Strasser lemma.

Beyond these special generating sets, Conjecture C is open for $S_n$ even with two generators.

### 5.6 Generating sets with prescribed relations

A few lemmas prove Hamiltonicity from relations among the generators alone, for every finite group.

- **Rankin.** If $S = \{a, b\}$ (with inverses) and $(ab)^2 = 1$, then $\mathrm{Cay}(G,S)$ is Hamiltonian.
- **Rapaport-Strasser (1959).** If $S = \{a, b, c\}$ consists of three involutions with $ab = ba$, then $\mathrm{Cay}(G,S)$ is Hamiltonian.
- **Pak and Radoičić (2009).** If $S = \{a, b, c\}$ with $a^2 = 1$ and $c = a^{-1} b a$, then $\mathrm{Cay}(G,S)$ is Hamiltonian.
- **Glover and Marušič (2007).** Let $G$ have a $(2,s,3)$-presentation, meaning $G = \langle a, b \rangle$ with $a^2 = b^s = (ab)^3 = 1$, and let $X = \mathrm{Cay}(G, \{a, b, b^{-1}\})$. If $|G| \equiv 2 \pmod 4$ then $X$ is Hamiltonian; if $|G| \equiv 0 \pmod 4$ then $X$ has a cycle through all but two vertices and hence a Hamiltonian path. Glover, Kutnar and Marušič (2009) obtained Hamiltonian cycles when $s \equiv 0 \pmod 4$, and Glover, Kutnar, Malnič and Marušič (2012) when $s$ is odd, leaving open only $s \equiv 2 \pmod 4$ with $|G| \equiv 0 \pmod 4$. The proofs build a Cayley map of $X$ on a surface and find a "tree of faces" whose boundary is the required cycle.
- **Stong (1987).** The Cayley graph of the wreath product $\mathbb{Z}_m \wr \mathbb{Z}_n$ with its natural generating set is Hamiltonian when $m$ is even or $m = 3$. The case $m = 2$ is the cube-connected cycles network.

Using the classification of finite simple groups, Pak and Radoičić proved that every finite group $G$ with $|G| \ge 3$ has a generating set $S$ with $|S| \le \log_2 |G|$ for which $\mathrm{Cay}(G,S)$ is Hamiltonian, and more precisely one with $|S| \le r(G) + 2m(G)$ where $r(G)$ and $m(G)$ count the abelian and nonabelian composition factors. The bound is sharp for elementary abelian 2-groups and for simple groups. They also constructed explicit cubic Hamiltonian expanders as Cayley graphs of $\mathrm{PSL}(2,p)$ on three involutions. Babai's question of whether every finite group has a *minimum* generating set whose Cayley graph is Hamiltonian is open.

### 5.7 Dense and pseudo-random Cayley graphs

The results in this subsection come from extremal and probabilistic combinatorics rather than group theory, and they are the only ones that apply to arbitrary groups with large generating sets.

- **Dense vertex-transitive graphs.** Christofides, Hladký and Máthé (2014) proved that for every $\varepsilon > 0$ there is $n_0$ such that every connected vertex-transitive graph on $n \ge n_0$ vertices with degree at least $\varepsilon n$ has a Hamiltonian cycle, and gave a polynomial-time algorithm to find one. The proof uses Szemerédi's regularity lemma.
- **Moderately dense Cayley graphs.** Bedert, Draganić, Müyesser and Pavez-Signé (2026) proved that there is an absolute constant $c > 0$ such that every large connected Cayley graph on $n$ vertices with degree at least $n^{1-c}$ is Hamiltonian. They replace the regularity lemma by an arithmetic regularity lemma specialized to Cayley graphs together with mild spectral expansion.
- **Random generating sets.** Krivelevich and Sudakov (2003) proved that $(n,d,\lambda)$-graphs with $d/\lambda \ge (\log n)^{1+o(1)}$ are Hamiltonian, and deduced that a Cayley graph on $G$ with $\Omega(\log^5 |G|)$ random generators is Hamiltonian with high probability. Draganić, Montgomery, Munhá Correia, Pokrovskiy and Sudakov (2024) proved that $d/\lambda \ge C$ suffices for an absolute constant $C$. Combined with the Alon–Roichman theorem that $C' \log |G|$ random generators give a spectral gap, this shows that a Cayley graph on any finite group with $O(\log |G|)$ random generators is Hamiltonian with high probability, which is the conjecture Pak and Radoičić formulated as a plausible weakening of Conjecture C.

### 5.8 Semisymmetric and other symmetric graphs

Du and Yuan (2026) asked whether edge-transitivity alone forces Hamiltonicity. They proved that every connected semisymmetric graph, meaning regular, edge-transitive and not vertex-transitive, of order $2pq$ is Hamiltonian, as is every connected cubic semisymmetric graph on fewer than 3000 vertices, and posed the construction of a non-Hamiltonian semisymmetric graph as an open problem.

## 6. Cayley digraphs

### 6.1 Rankin's theorem and non-Hamiltonian digraphs

For abelian $G = \langle a, b \rangle$, Rankin (1948) proved that $\overrightarrow{\mathrm{Cay}}(G; a, b)$ has a directed Hamiltonian cycle if and only if there are $k, \ell \ge 0$ with $k + \ell = |G : \langle ab^{-1} \rangle|$ and $\langle a^k b^\ell \rangle = \langle ab^{-1} \rangle$. A consequence for general groups is that if $ab^{-1}$ has odd order and generates a subgroup of even index, there is no directed Hamiltonian cycle; this is the form that rules out an extent of Grandsire Triples and the even-$n$ sigma–tau cycle. A concrete family: $\overrightarrow{\mathrm{Cay}}(\mathbb{Z}_n; a, a+1)$ is non-Hamiltonian whenever $\gcd(a,n) > 1$ and $\gcd(a+1,n) > 1$, for example $\mathbb{Z}_6$ with generators 2 and 3. Trotter and Erdős (1978) characterized the Hamiltonian Cartesian products of two directed cycles: $\overrightarrow{\mathrm{Cay}}(\mathbb{Z}_m \times \mathbb{Z}_n; (1,0),(0,1))$ is Hamiltonian if and only if $\gcd(m,n) = d_1 + d_2$ for positive integers with $\gcd(m, d_1) = \gcd(n, d_2) = 1$.

### 6.2 Positive results for digraphs

- Holsztyński and Strube (1978): every connected Cayley digraph on an abelian group has a directed Hamiltonian path, but every cyclic group whose order is not a prime power has a connected Cayley digraph with no directed Hamiltonian cycle.
- Witte (1986): every connected Cayley digraph on a $p$-group has a directed Hamiltonian cycle.
- Morris (2012): every two-generated Cayley digraph on a nilpotent group has a directed Hamiltonian path.
- Morris (2013): if $|[G,G]| < 4$ then every connected Cayley digraph on $G$ has a directed Hamiltonian path, and this fails for some groups with $|[G,G]| \in \{4, 5\}$. The same paper constructs infinitely many connected two-generated Cayley digraphs with no directed Hamiltonian path in which both generators have arbitrarily large order.
- Curran and Witte (1985) settled Hamiltonian paths in Cartesian products of directed cycles.

The directed setting therefore behaves like the digraph analogue of Babai's conjecture, and its main open question is a characterization of the Hamiltonian two-generated Cayley digraphs on nonabelian groups.

## 7. Related and stronger notions

- **Hamilton-connectedness.** Chen and Quimpo's theorem for abelian groups and Alspach, Chen and Dean's theorem for generalized dihedral groups of order divisible by 4 show that in the settled cases one usually gets Hamiltonian paths between any two prescribed vertices, not merely one Hamiltonian cycle.
- **Hamilton decompositions.** Alspach asked in 1984 whether every connected Cayley graph of even degree on an abelian group decomposes into Hamiltonian cycles; this is open. Alspach, Bryant and Dyer proved it for vertex-transitive graphs of order $p^2$. Bryant and Dean (2015) showed that the analogous statement for vertex-transitive graphs is false: there are infinitely many connected vertex-transitive graphs, including Cayley graphs of arbitrarily large degree, with no Hamilton decomposition. Their examples generalize the triangle-replacement construction behind the known non-Hamiltonian examples.
- **Unique Hamiltonian cycles.** Miraftab and Morris (2025) determined all vertex-transitive graphs with finitely many ends that have exactly one Hamiltonian cycle (or Hamiltonian circle, in the infinite case).
- **Symmetric Hamiltonian cycles.** The Hamilton compression of a graph, introduced by Gregor, Merino and Mütze, measures the largest rotational symmetry a Hamiltonian cycle can have. Infinite families of vertex-transitive graphs with prescribed compression were constructed in 2024, and Baligács and coauthors (2025) studied symmetry classes of Hamiltonian cycles from a computational viewpoint.
- **Infinite graphs.** For infinite Cayley graphs the analogue of a Hamiltonian cycle is a Hamiltonian circle in the Freudenthal compactification. Several of the finite results above, including Durnberger's theorem, have been extended to this setting.

## 8. Computational evidence

The census of Potočnik, Spiga and Verret of all connected cubic vertex-transitive graphs on at most 1280 vertices contains 111,360 graphs. Its tabulated Hamiltonicity data list no non-Hamiltonian graphs other than the four cubic exceptions of Section 1.3. Similar checks on censuses of Cayley graphs and of small vertex-transitive graphs of higher degree have produced no new exceptions. Pak and Radoičić report that the two-generated Cayley graph on $A_5^2$ with one generator an involution was verified Hamiltonian by Cook and Ruskey, and they single out Hall's two-generated group $A_5^{19}$ as a "beautiful but computationally unapproachable" potential counterexample. A 2024 arXiv preprint claims a proof of Conjecture B for all graphs of odd order; it has not appeared in a refereed venue and is not cited by the subsequent literature, so it should be regarded as unverified.

## 9. Open problems

1. Conjectures A, B and C in full generality, and whether one counterexample to A would generate infinitely many.
2. Decide between Babai's conjecture and Thomassen's conjecture; more modestly, prove or disprove Mohar's 2-walk conjecture.
3. Raise the longest-cycle exponent above $2/3$, which is a barrier for the current methods, and prove a linear lower bound $cn$ for some fixed $c > 0$.
4. Conjecture C for dihedral groups $D_{2n}$ with $n$ odd.
5. Conjecture C for cubic Cayley graphs, including the $(2,s,3)$ case with $s \equiv 2 \pmod 4$ and $|G| \equiv 0 \pmod 4$, and for two-generated Cayley graphs of $S_n$.
6. Babai's question: does every finite group have a minimum generating set whose Cayley graph is Hamiltonian?
7. Lower the degree threshold $n^{1-c}$ for Cayley graphs, and extend the moderately dense result from Cayley graphs to all vertex-transitive graphs.
8. Complete the order program: Hamiltonian cycles in vertex-transitive graphs of order $5p$, $p^5$ and imprimitive $2pq$, and Cayley graphs of the orders excluded in Section 5.3, such as $24p$.
9. Conjecture C for all solvable groups, or at least for groups with cyclic commutator subgroup.
10. Characterize the Hamiltonian two-generated Cayley digraphs on nonabelian groups.

## References

Surveys and background:

- L. Babai, Automorphism groups, isomorphism, reconstruction, in *Handbook of Combinatorics* vol. 2, Elsevier, 1996, pp. 1447–1540.
- S. J. Curran and J. A. Gallian, Hamiltonian cycles and paths in Cayley graphs and digraphs: a survey, *Discrete Math.* 156 (1996) 1–18.
- D. Knuth, *The Art of Computer Programming*, vol. 4A, Section 7.2.1.2, Addison-Wesley, 2011.
- K. Kutnar and D. Marušič, Hamilton cycles and paths in vertex-transitive graphs: current directions, *Discrete Math.* 309 (2009) 5491–5500.
- G. H. J. Lanel et al., A survey on Hamiltonicity in Cayley graphs and digraphs on different groups, *Discrete Math. Algorithms Appl.* 11 (2019).
- L. Lovász, Problem 11, in *Combinatorial Structures and Their Applications*, Gordon and Breach, 1970.
- T. Mütze, Combinatorial Gray codes: an updated survey, *Electron. J. Combin.* DS26 (2023).
- I. Pak and R. Radoičić, Hamiltonian paths in Cayley graphs, *Discrete Math.* 309 (2009) 5501–5508.
- D. Witte and J. A. Gallian, A survey: Hamiltonian cycles in Cayley graphs, *Discrete Math.* 51 (1984) 293–304.
- Open Problem Garden, Hamiltonicity of Cayley graphs; B. Mohar, 2-walks in vertex-transitive graphs (problem page).

Vertex-transitive graphs by order:

- B. Alspach, Hamiltonian cycles in vertex-transitive graphs of order 2p, *Congr. Numer.* 23 (1979) 131–139.
- D. Marušič and T. D. Parsons, Hamiltonian paths in vertex-symmetric graphs of order 5p, *Discrete Math.* 42 (1982) 227–242; order 4p, *Discrete Math.* 43 (1983) 91–96.
- D. Marušič, Vertex transitive graphs and digraphs of order $p^k$, *Ann. Discrete Math.* 27 (1985) 115–128.
- Y.-Q. Chen, On Hamiltonicity of vertex-transitive graphs and digraphs of order $p^4$, *J. Combin. Theory Ser. B* 72 (1998) 110–121.
- K. Kutnar and D. Marušič, Hamiltonicity of vertex-transitive graphs of order 4p, *European J. Combin.* 29 (2008) 423–438.
- K. Kutnar and P. Šparl, Hamilton paths and cycles in vertex-transitive graphs of order 6p, *Discrete Math.* 309 (2009) 5444–5460.
- K. Kutnar, D. Marušič and C. Zhang, Hamilton paths in vertex-transitive graphs of order 10p, *European J. Combin.* 33 (2012) 1043–1077.
- S. Du, K. Kutnar and D. Marušič, Resolving the Hamiltonian problem for vertex-transitive graphs of order a product of two primes, *Combinatorica* 41 (2021) 507–543; arXiv:1808.08553.
- S. Du, Y. Tian and H. Yu, Hamilton cycles in primitive graphs of order 2rs, arXiv:2203.13460 (2022).
- S. Du, W. Luo and H. Yu, On Hamilton paths in vertex-transitive graphs of order 10p, arXiv:2411.17780 (2024).
- S. Du and T. Zhou, Hamilton cycles in vertex-transitive graphs of order 6p, *Discrete Appl. Math.* 369 (2025); arXiv:2409.06138.
- T. Zhou, On Hamilton cycles in connected vertex-transitive graphs of order 2pq, arXiv:2608.02349 (2026).

Long cycles:

- L. Babai, Long cycles in vertex-transitive graphs, *J. Graph Theory* 3 (1979) 301–304.
- M. DeVos, Longer cycles in vertex transitive graphs, arXiv:2302.04255 (2023).
- C. Groenland, S. Longbrake, R. Steiner, J. Turcotte and L. Yepremyan, Longest cycles in vertex-transitive and highly connected graphs, *Bull. London Math. Soc.* (2025); arXiv:2408.04618.
- S. Norin, R. Steiner, S. Thomassé and P. Wollan, Intersections of longest cycles in vertex-transitive and highly connected graphs, arXiv:2508.17438 (2025).
- M. Bucić, M. Christoph, A. Pokrovskiy and R. Steiner, Towards the Lovász conjecture via sublinear expanders, arXiv:2606.09742 (2026).
- M. Bucić, K. Hendrey, B. Mohar, R. Steiner and L. Yepremyan, Long cycles in vertex transitive digraphs, arXiv:2602.16333 (2026).
- B. Li and A. Methuku, Long directed cycles in vertex-transitive digraphs, arXiv:2607.05807 (2026).

Cayley graphs, algebraic methods:

- C. C. Chen and N. F. Quimpo, On strongly Hamiltonian abelian group graphs, *Lecture Notes in Math.* 884 (1981) 23–34.
- D. Witte, Cayley digraphs of prime-power order are Hamiltonian, *J. Combin. Theory Ser. B* 40 (1986) 107–112.
- D. Marušič, Hamiltonian circuits in Cayley graphs, *Discrete Math.* 46 (1983) 49–54.
- E. Durnberger, Connected Cayley graphs of semidirect products of cyclic groups of prime order by abelian groups are Hamiltonian, *Discrete Math.* 46 (1983) 55–68.
- K. Keating and D. Witte, On Hamilton cycles in Cayley graphs in groups with cyclic commutator subgroup, *Ann. Discrete Math.* 27 (1985) 89–102.
- E. Ghaderpour and D. W. Morris, Cayley graphs on nilpotent groups with cyclic commutator subgroup are Hamiltonian, *Ars Math. Contemp.* 7 (2014) 55–72; arXiv:1111.6216.
- D. W. Morris, Odd-order Cayley graphs with commutator subgroup of order pq are Hamiltonian, *Ars Math. Contemp.* 8 (2015) 1–28; arXiv:1205.0087.
- D. W. Morris, Cayley graphs on groups with commutator subgroup of order 2p are Hamiltonian, *Art Discrete Appl. Math.* 1 (2018); arXiv:1703.06377.
- K. Kutnar, D. Marušič, D. W. Morris, J. Morris and P. Šparl, Hamiltonian cycles in Cayley graphs whose order has few prime factors, *Ars Math. Contemp.* 5 (2012) 27–71; arXiv:1009.5795.
- E. Ghaderpour and D. W. Morris, Cayley graphs of order 27p are Hamiltonian, *Int. J. Combin.* (2011); Cayley graphs of order 30p are Hamiltonian, *Discrete Math.* 312 (2012); arXiv:1101.4322, arXiv:1102.5156.
- S. J. Curran, D. W. Morris and J. Morris, Cayley graphs of order 16p are Hamiltonian, *Ars Math. Contemp.* 5 (2012); arXiv:1104.0081.
- D. W. Morris and K. Wilk, Cayley graphs of order 6pq are Hamiltonian, arXiv:2009.10055 (2020).
- D. W. Morris, On Hamiltonian cycles in Cayley graphs of order pqrs, arXiv:2107.14787 (2021).
- F. Abedi, D. W. Morris, J. Rezaee and M. R. Salarian, Cayley graphs of order 8pq are Hamiltonian, arXiv:2304.03348 (2023).
- F. Lehner, F. Maghsoudi and B. Miraftab, Cayley graphs of order pqrs are Hamiltonian, arXiv:2607.14440 (2026).
- F. Lehner, F. Maghsoudi and B. Miraftab, Hamiltonicity of transitive graphs whose automorphism group has $\mathbb{Z}_p$ as commutator subgroup, arXiv:2412.08105 (2024).
- B. Alspach and C. Q. Zhang, Hamilton cycles in cubic Cayley graphs on dihedral groups, *Ars Combin.* 28 (1989) 101–108.
- B. Alspach, C. C. Chen and M. Dean, Hamilton paths in Cayley graphs on generalized dihedral groups, *Ars Math. Contemp.* 3 (2010) 29–47.
- B. Miraftab, Hamiltonicity in generalized quasi-dihedral groups, arXiv:2204.05484 (2022).
- H. H. Glover and D. Marušič, Hamiltonicity of cubic Cayley graphs, *J. Eur. Math. Soc.* 9 (2007) 775–787; arXiv:math/0508647.
- H. H. Glover, K. Kutnar and D. Marušič, Hamiltonian cycles in cubic Cayley graphs: the (2,4k,3) case, *J. Algebraic Combin.* 30 (2009) 447–475.
- H. H. Glover, K. Kutnar, A. Malnič and D. Marušič, Hamilton cycles in (2,odd,3)-Cayley graphs, *Proc. London Math. Soc.* 104 (2012) 1171–1197.
- E. Rapaport-Strasser, Cayley color groups and Hamilton lines, *Scripta Math.* 24 (1959) 51–58.
- R. Stong, On Hamiltonian cycles in Cayley graphs of wreath products, *Discrete Math.* 65 (1987) 75–80.
- V. L. Kompel'makher and V. A. Liskovets, Sequential generation of arrangements by means of a basis of transpositions, *Kibernetika* 3 (1975) 17–21.
- M. Tchuente, Generation of permutations by graphical exchanges, *Ars Combin.* 14 (1982) 115–122.
- J. H. Conway, N. J. A. Sloane and A. R. Wilks, Gray codes for reflection groups, *Graphs Combin.* 5 (1989) 315–325.
- R. C. Compton and S. G. Williamson, Doubly adjacent Gray codes for the symmetric group, *Linear Multilinear Algebra* 35 (1993) 237–293.
- J. Sawada and A. Williams, A Hamilton path for the sigma-tau problem, *SODA 2018*; Solving the sigma-tau problem, *ACM Trans. Algorithms* 16 (2020).

Dense, pseudo-random and random Cayley graphs:

- D. Christofides, J. Hladký and A. Máthé, Hamilton cycles in dense vertex-transitive graphs, *J. Combin. Theory Ser. B* 109 (2014) 34–72; arXiv:1008.2193.
- B. Bedert, N. Draganić, A. Müyesser and M. Pavez-Signé, The Lovász conjecture holds for moderately dense Cayley graphs, arXiv:2603.08675 (2026).
- M. Krivelevich and B. Sudakov, Sparse pseudo-random graphs are Hamiltonian, *J. Graph Theory* 42 (2003) 17–33.
- N. Draganić, R. Montgomery, D. Munhá Correia, A. Pokrovskiy and B. Sudakov, Hamiltonicity of expanders: optimal bounds and applications, arXiv:2402.06603 (2024).
- N. Alon and Y. Roichman, Random Cayley graphs and expanders, *Random Structures Algorithms* 5 (1994) 271–284.

Digraphs:

- R. A. Rankin, A campanological problem in group theory, *Proc. Cambridge Philos. Soc.* 44 (1948) 17–25; R. G. Swan, A simple proof of Rankin's campanological theorem, *Amer. Math. Monthly* 106 (1999) 159–161.
- W. T. Trotter and P. Erdős, When the Cartesian product of directed cycles is Hamiltonian, *J. Graph Theory* 2 (1978) 137–142.
- W. Holsztyński and R. F. E. Strube, Paths and circuits in finite groups, *Discrete Math.* 22 (1978) 263–272.
- S. J. Curran and D. Witte, Hamilton paths in Cartesian products of directed cycles, *Ann. Discrete Math.* 27 (1985) 35–74.
- D. W. Morris, 2-generated Cayley digraphs on nilpotent groups have Hamiltonian paths, *Contrib. Discrete Math.* 7 (2012) 41–47.
- D. W. Morris, On Cayley digraphs that do not have Hamiltonian paths, *Int. J. Combin.* (2013); arXiv:1306.5443.

Related notions and data:

- D. Bryant and M. Dean, Vertex-transitive graphs that have no Hamilton decomposition, *J. Combin. Theory Ser. B* 114 (2015) 237–246; arXiv:1408.5211.
- B. Miraftab and D. W. Morris, On vertex-transitive graphs with a unique Hamiltonian cycle, *J. Graph Theory* 108 (2025) 65–90.
- S. Du and K. Yuan, Hamilton cycles in semisymmetric graphs, arXiv:2602.14388 (2026).
- P. Potočnik, P. Spiga and G. Verret, Cubic vertex-transitive graphs on up to 1280 vertices, *J. Symbolic Comput.* 50 (2013) 465–477; census data on Zenodo.
- B. Alspach, The classification of Hamiltonian generalized Petersen graphs, *J. Combin. Theory Ser. B* 34 (1983) 293–312.
- M. E. Watkins, Connectivity of transitive graphs, *J. Combin. Theory* 8 (1970) 23–29.
