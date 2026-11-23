# From Watrous to star GHZ heralding

John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018, is the educational anchor. Section and exercise numbers below follow the standard-layout author manuscript. [Chapter downloads](https://jhwatrous.github.io/books-and-courses.html) · [Published edition](https://doi.org/10.1017/9781316848142)

| Anchor material | Translation to this project |
|---|---|
| Sections 1.1.1 and 1.1.3, complex vector spaces and operator decompositions | Use computational basis strings for the registers and Schmidt decompositions to express the individual hub–leaf pairs. Squared Schmidt amplitudes multiply across independent links. |
| Sections 2.1.2–2.1.3, states, reduction and purification | Tracing out the hub leaves a diagonal distribution $`\rho_L=\sum_x p_x\lvert x\rangle\langle x\rvert`$. The full star is the corresponding pure state on hub and leaves. |
| Sections 2.2.2 and 2.3.1–2.3.2, operator representations and measurements | A hub outcome gives a positive subnormalized operator on the leaves. Its trace is the outcome probability. Local corrections act after the hub broadcasts the label. Theorem 2.42 explains how a generalized measurement can be realized with an enlarged register and a projective readout. |
| Exercise 2.2 and Section 2.5, ensembles from purification | A hub measurement can realize an ensemble of its purified leaf state. The bibliographic remarks credit Hughston, Jozsa, and Wootters. |
| Sections 6.1.2 and 6.2.1, LOCC and pure-state entanglement transformation | Group every lab except one leaf into the other side of a bipartition. The hub and leaf labs fall within local operations and classical communication (LOCC) across that cut. Use Vidal's stochastic conversion theorem for the quantitative cut bound. |
| Sections 1.1.3 and 3.2, trace norm and fidelity | Translate conditioning and implementation error into distances between physical states. The [robustness account](../science/ROBUSTNESS.md) specifies its fidelity convention and its assumptions on errors. |

## From conditional operators to probabilities

Let $`x\in\{0,1\}^N`$ be a bitstring and write $`\bar x`$ for its bitwise complement. For a hub–leaf pair with smaller Schmidt probability $`q_i`$, the respective probabilities of a zero and one in that link's Schmidt basis are $`1-q_i`$ and $`q_i`$. A shared string $`x`$ therefore has probability $`p_x`$ given by the product of its link probabilities. Let $`D_p=\mathrm{diag}(p_x)`$.

A hub effect $`E_j`$ for outcome $`j`$ gives the unnormalized leaf operator $`D_p^{1/2} E_j^{\mathsf T}D_p^{1/2}`$. The transpose appears in the paired Schmidt bases. Summing over all outputs restores $`D_p`$ because the effects sum to the identity. The diagonal entry for string $`x`$ therefore gives a budget for all successful outcomes combined. Its total cannot exceed $`p_x`$. The trace gives the total probability spent on success. [Model and measurement rule](../science/MODEL.md)

Each corrected success must be a GHZ state. Before correction it belongs to the local-unitary orbit of GHZ. The diagonal of any such state has equal complementary entries when $`N`$ is even. When $`N`$ is odd, the even entry minus its odd complement must be a common number across all pairs. Orthogonality of the local columns makes the interference term change sign with each complemented bit. This lets the project optimize a single common shift and realize it by measuring a uniform parity sector. The [optimality proof](../science/OPTIMALITY.md) establishes both claims and gives the attainable formula.

## Worked example with three identical links

Take $`q=2/5`$ on each link. The four numbers in the second column are probabilities per string. The last column counts the strings at each Hamming weight.

| Hamming weight | Probability per string | Number of strings |
|---|---:|---:|
| 0 | $`27/125`$ | 1 |
| 1 | $`18/125`$ | 3 |
| 2 | $`12/125`$ | 3 |
| 3 | $`8/125`$ | 1 |

The four even-minus-odd complementary differences are $`19/125`$ and three copies of $`-6/125`$. The median $`-6/125`$ lies inside the allowed interval $`[-8/125,12/125]`$. The negative sign selects the odd parity. The hub diverts probability $`6/125`$ from each of its four odd strings into the parity branch. On this branch the leaf amplitude is uniform over those strings up to the announced phases. Local phase corrections and Hadamards yield a GHZ state with total probability $`24/125`$.

The complementary branch retains probabilities $`27/125,12/125,12/125,2/125`$ per string at weights zero through three. The hub balances each complementary pair down to its smaller probability. The weight-zero/three pair contributes $`4/125`$. Each of the three weight-one/two pairs contributes $`24/125`$. Those outcomes add $`76/125`$, for total success $`100/125=0.8`$. The familiar complementary protocol has success $`88/125=0.704`$ from the original probabilities. The new yield equals the maximum allowed across a leaf cut. [Hub implementation](../science/IMPLEMENTATION.md) · [Proof and scope](../science/OPTIMALITY.md)

### Charge the broadcast on the same example

Each accepted label supplies one pre-correction ket $`|\psi\rangle`$. Conjugate the steering inequality $`\lambda|\psi\rangle\langle\psi|\preceq D_p`$ by $`D_p^{-1/2}`$. The resulting rank-one effect has a single eigenvalue, $`\lambda\langle\psi|D_p^{-1}|\psi\rangle`$, which must be at most one. For a balanced cat on a middle pair this gives $`\lambda\le 2/(125/18+125/12)=72/625`$. The GHZ-orbit diagonal constraint gives this same bound for every single label at $`q=2/5`$. The three disjoint middle pairs each realize it. Use one of the codewords for failure, so one and two bits respectively give one and three successful words, with total probabilities $`72/625`$ and $`216/625`$.

With four accepted words, another complementary word increases the best complementary-basis probability to $`1944/4375`$. Choosing four rotated kets instead gives $`22979693/50000000`$. The check uses the same operator-order condition as the one-word example, now applied to the sum of four effects. At the full optimum $`4/5`$, the rank of that sum requires at least eight accepted words in addition to failure. Four bits suffice. [Broadcast budget proof](../science/COMMUNICATION.md) · [Four-label certificate](../verification/README.md#four-accepted-labels)

## From a star to a network

The honeycomb construction uses the stars centered on one color class of vertices. Source pairs for different stars are independent even when two output qubits lie in the same lab. An occupied site corresponds to a hub that successfully delivers an exact GHZ state. The occupied sites form a triangular-lattice site-percolation model. Ideal local fusion makes the occupation threshold $`1/2`$ operational. The [network account](../science/NETWORK.md) supplies this graph mapping and the matched comparison with the published complementary protocol. The [robustness account](../science/ROBUSTNESS.md) treats the effects of phase errors and implementation errors on the heralded state.

