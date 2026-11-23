# Exact GHZ heralding with a broadcast budget

[Star model](MODEL.md) · [Optimality proof](OPTIMALITY.md) · [Hub implementation](IMPLEMENTATION.md)

One known pure qubit pair per edge supplies the star. The hub makes a joint measurement and broadcasts a label. Each leaf applies a unitary fixed by that label. An accepted label includes the information required to deliver the exact GHZ state in the specified output bases. Write $`M_{\mathrm{acc}}`$ for the maximum number of accepted labels and $`c`$ for the maximum number of broadcast bits per attempt. The words identifying every possible outcome, including failure, form a prefix-free code. One bit broadcast to all leaves costs one bit.

## One accepted label

Let $`D=\mathrm{diag}(p_x)`$ be the leaf marginal in the joint Schmidt basis. For a normalized pre-correction state $`|\psi\rangle`$ in the local-unitary GHZ orbit, the highest single-label probability is

```math
\lambda(\psi)=\frac{1}{\langle\psi|D^{-1}|\psi\rangle}.
```

The inverse is on the support of $`D`$. A state with a component outside that support has zero attainable probability. The steering rule gives $`\lambda|\psi\rangle\langle\psi|\preceq D`$. Conjugating by $`D^{-1/2}`$ bounds the only nonzero eigenvalue by one. Conversely, for any $`\lambda`$ obeying this condition, the transposed conjugate by $`D^{-1/2}`$ is a valid hub effect and its complement is a valid failure effect. [Model and measurement rule](MODEL.md#conditional-states)

The reciprocal of $`\lambda(\psi)`$ is linear in the computational diagonal of $`|\psi\rangle\langle\psi|`$. The [orbit diagonal constraint](OPTIMALITY.md#the-computational-diagonal-of-a-corrected-success-state) puts that diagonal in the convex hull of uniform complementary pairs and, when $`N`$ is odd, uniform even and odd parity sectors. For even $`N`$, pair equal entries to obtain the decomposition. For odd $`N`$, remove the common excess on its favored parity, then pair the complement-symmetric remainder. Each generator is the diagonal of a GHZ-orbit state. A balanced cat represents a complementary pair, while local Hadamards and a possible phase flip give a uniformly occupied parity sector. Thus the exact one-label cap $`\beta`$ is the greatest of the harmonic means

```math
\frac{2}{1/p_x+1/p_{\bar x}}
\quad\text{and, for odd }N,\quad
\frac{2^{N-1}}{\displaystyle\sum_{x\in S}1/p_x},\qquad
S\in\{\text{even strings},\text{odd strings}\}.
```

Assign value zero to a generator containing a zero-weight string. Summing the label bound and using the unconstrained optimum $`P_\star`$ gives $`P\le\min\{P_\star,M_{\mathrm{acc}}\beta\}`$. Whether several individually optimal labels can be used together depends on the sum of their effects.

## One or two bits on three identical links

For three links with the same $`0\lt q\lt 1/2`$, put $`a_j=(1-q)^{3-j}q^j`$ for the weight of one string with Hamming weight $`j`$. Set $`K=a_0a_3=a_1a_2`$. The middle complementary pairs have a smaller sum $`a_1+a_2=q(1-q)\le a_0+a_3`$ and therefore give the largest complementary cap $`2K/(a_1+a_2)`$. The two parity caps are $`4K/(3a_1+a_3)`$ and $`4K/(a_0+3a_2)`$. The respective denominators exceed or equal $`2(a_1+a_2)`$ by $`q(1-2q)^2`$ and $`(1-q)(1-2q)^2`$. It follows that $`\beta=2q^2(1-q)^2`$.

The three middle pairs have disjoint support. A hub can use one individually maximal rank-one effect on each selected pair, with its leftover effect as failure. The leaf-cut bound $`P\le 2q<1`$ requires a positive-probability failure word. A worst-case budget $`c`$ gives at most $`2^c-1`$ accepted words. For $`c=1,2`$, the number fits on the three pairs, so the optimum is

```math
P_c(q)=(2^c-1)\,2q^2(1-q)^2,\qquad c=1,2.
```

At $`q=2/5`$ this is $`0.1152`$ and $`0.3456`$, respectively.

## Four accepted labels at the same calibration

Use $`q=2/5`$ and allow four accepted labels and a separate failure word. For corrections using only complementary GHZ-basis states, each pair supplies one label up to its harmonic-mean cap and two labels up to twice its smaller Schmidt weight. Both caps are attainable for the respective label counts. The three middle pairs each contribute up to $`72/625`$ for their first label, and the extreme pair first contributes up to $`432/4375`$. The incremental yields for a second label are $`48/625`$ and $`128/4375`$, respectively. The four largest increments are the four first labels. The complementary-basis optimum is therefore $`1944/4375\approx0.44434286`$.

An instrument with rotated local bases achieves $`22979693/50000000=0.45959386`$. For each label $`j`$, the pre-correction ket is $`\bigotimes_i U_{ji}(|000\rangle+s_j|111\rangle)/\sqrt{2}`$, where each $`U_{ji}`$ is a real two-dimensional rotation and $`s_j\in\{-1,1\}`$. The leaves can undo the rotations and remove the relative sign with a phase flip. The [exact rational certificate](../verification/check_four_labels.py) gives the rotations and probabilities $`\lambda_j`$. It bounds the largest eigenvalue of the Gram matrix of the whitened kets $`\sqrt{\lambda_j}D^{-1/2}|\psi_j\rangle`$ by one. The corresponding success effects therefore sum to at most the identity and the residual effect supplies failure. [How to run the certificate](../verification/README.md#four-accepted-labels)

### Why the bound from one label is strict here

At this calibration only the three middle generators attain $`\beta=72/625`$. If four labels attained $`4\beta`$, each would have weight $`\beta`$. Each whitened success effect would be a rank-one projector and the four projectors would be mutually orthogonal. Each underlying GHZ-orbit state would have zero amplitudes at $`000`$ and $`111`$, since its diagonal could use only the middle generators.

To characterize such a state, write the two orthonormal columns at leaf $`i`$ as $`(a_i,b_i)`$ and $`e^{i\theta_i}(-\overline{b_i},\overline{a_i})`$. Set $`A=\prod_i a_i`$, $`B=\prod_i b_i`$ and $`\theta=\sum_i\theta_i`$. The vanishing amplitudes give $`A-e^{i\theta}\overline B=0`$ and $`B+e^{i\theta}\overline A=0`$, so $`A=B=0`$. At least two distinct leaves use computational bases with opposite orientations. The resulting state occupies at most two of the three middle pair indices. On a two-index support, its weight-two amplitudes, indexed by their weight-one complements, are the conjugates of its weight-one amplitudes with a common phase and opposite signs on the two indices. This follows by expanding the two terms after fixing the two computational columns. Complementary entries have equal modulus, and each weight sector carries half the probability.

Consider any two such kets. The magnitudes of their unwhitened overlaps on the two weight sectors are equal. For equal two-index supports, the common phase and opposite signs imply this by conjugation. If their supports intersect at a single index, equality follows from equal complementary moduli there. The overlaps both vanish on disjoint supports. Whitening scales the sector overlaps by $`1/a_1`$ and $`1/a_2`$, respectively. These scales differ, so two whitened kets can be orthogonal only if their weight-one parts are orthogonal. Four nonzero mutually orthogonal weight-one vectors cannot fit in a three-dimensional space. The four-label feasible set is compact because the weights and local unitaries range over compact sets and the operator constraint is closed. Its maximum therefore satisfies

```math
\frac{22979693}{50000000}\ \le P_{M_{\mathrm{acc}}=4}(2/5)<\frac{288}{625}=0.4608.
```

Four accepted words and one failure word fit in three bits. A three-bit code can use as many as seven accepted words. The exact four-label value and the full three-bit optimum remain open here.

## Bits needed to reach the unconstrained optimum

For $`q_*=(3-\sqrt5)/2\lt q\lt 1/2`$ on three identical links, the unconstrained optimum is $`P_\star=2q`$. Every accepted state has one-leaf marginal $`I/2`$. The sum of the success operators therefore exhausts the input population $`q`$ of bit 1 at each leaf. Positivity confines the aggregate failure operator to $`(1-2q)|000\rangle\langle000|`$. The remaining success operator is diagonal and has rank eight. Its adjusted $`000`$ entry is $`q(-1+3q-q^2)>0`$, and every other entry is positive as well. Each accepted label contributes rank one, so at least eight accepted words and a separate failure word are necessary. The existing hub instrument uses at most thirteen words and attains the optimum with four bits. This argument uses the fixed one-way hub and leaf-unitary model. [Achieving instrument](IMPLEMENTATION.md#implementation-resources)

An analogous minimum holds for every even $`N`$ with full-support input and a partial link. An optimal success diagonal must take the smaller weight in each complementary pair. The failure operator is supported on the set of strictly larger pair members. In addition, each successful GHZ-orbit projector is invariant under $`\Theta=(iY)^{\otimes N}K_0`$, where $`K_0`$ conjugates in the computational basis. The even-$`N`$ GHZ projector is invariant directly, and the one-qubit spin flip commutes with special unitary basis changes. Every off-diagonal entry of the success operator could only lie inside the support of failure. Its complementary entry must also be present by $`\Theta`$ invariance, but the failure support contains no complementary pair. Thus the success operator is diagonal and has full rank $`2^N`$. A partial link makes failure positive, so $`N+1`$ bits are necessary. Complementary balancing attains this budget. [Even-star optimum](OPTIMALITY.md#optimize-the-capped-success-diagonal)

## Bell links and the adaptive converse

With Bell links the familiar GHZ basis has $`2^N`$ equiprobable correction words. A selected subset gives success probability $`M_{\mathrm{acc}}/2^N`$ up to $`2^N`$ words. On this endpoint the exact cap follows from the single-label formula. The companion project proves the same $`2^{-N}`$ cap per accepted transcript even for arbitrary independent bipartite resources and adaptive LOCC when no source joins two outputs. Its result also applies to $`d`$-level targets. The fixed calibrated input and the rotated partial-link instrument are the complementary contribution here. [GHZ Communication Cost](https://github.com/GoGoKo699/GHZ-Communication-Cost) · [Companion converse](https://github.com/GoGoKo699/GHZ-Communication-Cost/blob/1549e98fc8740266012bd143dc5e7189274229a5/science/expected-and-heralded.md#exact-heralding-without-sources-between-outputs)
