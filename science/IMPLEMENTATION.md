# The attaining hub instrument

[Star model](MODEL.md) · [Optimality proof](OPTIMALITY.md) · [Error budgets](ROBUSTNESS.md)

The hub spends one copy of every pair and sends one herald with a correction label. The filters below act on the hub register before the leaves receive that message. In particular, residual branches remain coherent between the strings being balanced.

## Choose the allocation

Compute the Schmidt weights $`p_x`$. For even $`N`$, use $`t=0`$. For odd $`N`$, index complementary pairs by their even strings and clamp a median of $`p_e-p_{\bar e}`$ to the interval in [the theorem](OPTIMALITY.md). Let $`a=\lvert t\rvert`$. If $`t>0`$, choose even parity. If $`t<0`$, choose odd parity. At $`t=0`$, skip the parity branch altogether.

## Parity branch

Make a two-outcome coherent diagonal filter. For strings of the chosen parity with $`p_x>0`$, its success operator has diagonal entry $`\sqrt{a/p_x}`$. It is zero on other strings. The other outcome has a single Kraus operator $`\sqrt{I-K_{\mathrm{par}}^\dagger K_{\mathrm{par}}}`$. The bound on $`t`$ makes both operators contractions. On this other outcome the unnormalized residual distribution $`p'_x`$ is $`p_x-a`$ on the chosen parity and $`p_x`$ off it.

On parity success, measure all hub qubits in the X basis. If the measurement label is $`y`$, the leaf state is a uniform parity state with sign $`(-1)^{x\cdot y}`$ at $`x`$. Each leaf first applies its indicated $`Z`$ and then a Hadamard. A fixed $`Z`$ at one leaf is also needed when the chosen parity was odd. This produces the target GHZ state with branch probability $`2^{N-1}a`$.

## Complementary branch

On the residual outcome, set $`b_x=\min(p'_x,p'_{\bar x})`$. A hub diagonal filter multiplies the amplitude at $`x`$ by $`\sqrt{b_x/p'_x}`$ when $`p'_x>0`$, and by zero otherwise. Apply the ordinary GHZ-basis measurement to the hub on filter success. For outcome given by the unordered pair $`x,\bar x`$ and a sign, the leaves receive

```math
\frac{\lvert x\rangle\pm\lvert\bar x\rangle}{\sqrt{2}} .
```

Apply the indicated local bit flips and, for a minus sign, one phase flip. Each pair contributes $`2b_x`$ to the total probability. Adding the parity-branch success probability gives the [optimum](OPTIMALITY.md).

A concrete alternate ordering uses $`N-1`$ CNOTs from the first hub qubit to the other hub qubits and a computational readout of those targets. This reads the pair syndrome without revealing the choice within the pair. A heralded one-qubit rotation balances the two residual amplitudes and a final X measurement reads the relative phase. Revealing the full input string before balance would destroy the required coherence.

## Implementation resources

A diagonal filter can be made by a controlled rotation on one local flag, followed by measuring that flag. For an amplitude factor $`f_x\in[0,1]`$, rotate the flag so its success amplitude is $`f_x`$ and its other amplitude is $`\sqrt{1-f_x^2}`$. Keep the failure flag coarse enough that the parity filter leaks no string information. A single flag can be reinitialized for the second filter. The star uses $`N`$ hub input qubits, $`N`$ leaf output qubits and any local workspace needed to implement the controlled rotations.

On the complementary branch, $`N`$ bits specify a pair and phase. On a parity branch, X outcomes $`y`$ and $`\bar y`$ specify the same correction up to a global phase, since the input strings have fixed parity. At most $`2^{N-1}`$ parity labels suffice. Including both branch types and failure gives at most $`2^N+2^{N-1}+1`$ distinct labels, so $`N+1`$ broadcast bits suffice for $`N\geq 2`$. Exact budget optima in calibrated regimes and lower bounds on the bits required to reach the unconstrained maximum are given in [the broadcast analysis](COMMUNICATION.md).

For identical input pairs, both diagonal rotation angles depend only on Hamming weight. They can be controlled by a reversibly computed weight register of $`\lceil\log_2(N+1)\rceil`$ bits, with at most $`N+1`$ different angles per filter. Uncompute the register after applying the controlled rotation and before reading the flag. General heterogeneous weights can be tabulated directly using $`2^N`$ entries. The exact probability theorem does not assume an efficient generic compilation of those tables.

## Three identical links

Write $`q_*=(3-\sqrt{5})/2`$. For $`0\lt q\leq q_*`$, choose the odd parity branch with $`a=q^3`$. The all-ones string then uses a filter success amplitude of one. The three Hamming-weight-one strings use the same success amplitude $`q/(1-q)`$, by substituting $`p_x=q(1-q)^2`$. All even strings have zero success amplitude in this first filter. The parity branch contributes $`4q^3`$, and the complementary branch contributes $`6q^2(1-q)`$. This gives $`6q^2-2q^3`$ and includes the critical regime of the [honeycomb protocol](NETWORK.md).

For $`q>q_*`$, set $`a=q(1-q)(1-2q)`$, so that the resulting total probability attains the cut bound $`2q`$. At $`q=1/2`$, this choice reduces to the ordinary deterministic GHZ readout.
