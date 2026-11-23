# Star model

[Project overview](../README.md) · [Optimality proof](OPTIMALITY.md) · [Measurement design](IMPLEMENTATION.md)

There is one hub, $N\geq 2$ leaves, and one fresh entangled qubit pair on each hub–leaf edge. Link $i$ has known Schmidt probability $q_i\in[0,1/2]$ and is written in its known local Schmidt bases as

```math
\sqrt{1-q_i}\lvert 00\rangle+\sqrt{q_i}\lvert 11\rangle.
```

The links are independently prepared. The joint state across the hub and leaf registers therefore has the form

```math
\lvert\Psi_p\rangle=\sum_{x\in\{0,1\}^N}\sqrt{p_x}\lvert x\rangle_H\lvert x\rangle_L,
\qquad
p_x=\prod_{i=1}^N (1-q_i)^{1-x_i}q_i^{x_i}.
```

At $q_i=0$, the product is interpreted by choosing the factor $1-q_i$ or $q_i$ according to bit $x_i$. We write $\bar x$ for the bitwise complement and $\lvert x\rvert$ for the Hamming weight. A string is even or odd according to that weight.

## Operations and task

The hub performs a general quantum instrument on its $N$ qubits, with arbitrary local ancillas as needed. It sends one classical label, including success or failure and correction information, and is discarded. Each leaf can apply an outcome-dependent unitary on its own qubit. The protocol uses no further entangled links or leaf filtering. Hub operations can adapt to intermediate observations within the same instrument.

On each declared success, the corrected leaf state must be the exact pure target

```math
\lvert G_N\rangle=\frac{\lvert 0\rangle^{\otimes N}+\lvert 1\rangle^{\otimes N}}{\sqrt{2}}.
```

The objective is the total probability of success per supplied star. One copy of every input pair is spent per attempt, regardless of the outcome. A classical correction can also be tracked in a local frame if the subsequent use permits it.

The proof and the construction use only the displayed Schmidt-correlated state and so also apply to a general distribution $p$ on the strings if that pure state is supplied. Independence is needed for the product-link interpretation, the individual link-cut bounds, and the construction on a lattice.

## Conditional states

For a hub POVM effect $E_j$, the unnormalized conditional state of the leaves is

```math
\sigma_j=D_p^{1/2}E_j^{\mathsf T}D_p^{1/2},
\qquad
D_p=\mathrm{diag}(p_x).
```

Transpose is taken in the common string basis. Therefore $\sum_j\sigma_j=D_p$. A successful outcome must have a rank-one leaf state in the local-unitary orbit of the target, with its trace giving the probability of that label. Failure outcomes can be arbitrary. This remains valid when some $p_x$ are zero because the relation is applied on the support of $D_p$.

## Benchmarks

- **Complementary swapping.** Project in the GHZ basis made of the plus and minus superpositions of $x$ and $\bar x$, then concentrate each branch using its known amplitudes. The optimal probability from this branchwise route, even with optimal leaf filtering after this fixed measurement, is $`2\sum_{\{x,\bar x\}}\min(p_x,p_{\bar x})`$. The same probability can be obtained by balancing at the hub before the GHZ readout. See [the comparison](../references/RELATED.md).
- **Leaf cut.** Across the cut separating leaf $i$ from every other laboratory, the source has Schmidt probabilities $(1-q_i,q_i)$ and the target has $(1/2,1/2)$. The single-copy stochastic conversion bound gives $P\leq 2q_i$ even for arbitrary local operations and classical communication across the star. Taking the minimum bounds every star protocol. See [Vidal and the scope of the cut bound](../references/RELATED.md).

Across the lattice, stations may also act jointly on distinct local qubits delivered by different stars in a subsequent [fusion stage](NETWORK.md). This stage is outside the definition of a single star attempt.
