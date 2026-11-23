# Calibration and phase noise

[Star model](MODEL.md) · [Achieving instrument](IMPLEMENTATION.md) · [Network application](NETWORK.md)

The [star optimum](OPTIMALITY.md) is for exact GHZ states from calibrated pure links and ideal operations. Two perturbation calculations quantify what the same heralding instrument delivers when those assumptions are relaxed. We use fidelity to a fixed pure target to mean the squared overlap, $`F(\rho,|\phi\rangle)=\langle\phi|\rho|\phi\rangle`$.

## Imperfect calibration and finite gate precision

Write the $`i`$th nominal Schmidt pair as $`|\psi_i(\hat\theta_i)\rangle=\cos\hat\theta_i|00\rangle+\sin\hat\theta_i|11\rangle`$, with $`q_i=\sin^2\theta_i`$ for the actual pure pair in the same calibrated Schmidt bases. If $`|\theta_i-\hat\theta_i|\le\epsilon_i`$, the trace distance between nominal and actual star input is bounded by

```math
D_{\mathrm{in}}=\sqrt{1-\prod_i\cos^2(\theta_i-\hat\theta_i)}\;\le\;\min\left\{1,\sqrt{\sum_i\epsilon_i^2}\right\}.
```

The equality is the trace distance for these two product pure states. The inequality follows from $`1-\prod_i(1-s_i)\le\sum_i s_i`$ with $`s_i=\sin^2(\theta_i-\hat\theta_i)`$. Any independently established input-state trace distance can replace this estimate, including one that covers phase or basis mismatch.

Let $`D_{\mathrm{op}}`$ bound the change in the final flagged state due to implementing the nominal instrument and corrections approximately, with the input held fixed. A sum of per-operation half diamond-distance bounds gives such a bound by telescoping channel differences. For a rotation $`R_y(\alpha)=\exp(-i\alpha Y/2)`$, including controlled applications, rounding the angle by $`\delta`$ contributes at most $`|\delta|/2`$ to this sum. This follows from $`\|R_y(\alpha+\delta)-R_y(\alpha)\|_{\mathrm{op}}=2|\sin(\delta/4)|`$ and the unitary-channel trace-distance bound. Set $`D=\min\{1,D_{\mathrm{in}}+D_{\mathrm{op}}\}`$.

Let $`P_0`$ be the designed success probability, $`P`$ the actual herald rate, and $`F_{\mathrm{acc}}`$ the fidelity of the corrected, accepted ensemble to GHZ. Treating success, and success with a projection onto the orthogonal complement of GHZ, as quantum events gives

```math
|P-P_0|\le D,\qquad P(1-F_{\mathrm{acc}})\le D.
```

The second event has probability zero in the nominal circuit. If $`P_0>D`$, these inequalities imply

```math
F_{\mathrm{acc}}\ge \max\left\{0,1-\frac{D}{P_0-D}\right\}.
```

The accepted overlap yield also obeys $`P F_{\mathrm{acc}}\ge\max\{0,P_0-D\}`$, by testing success and the GHZ projector together. The estimates refer to the accepted ensemble and can be applied to each branch by substituting its nominal probability. They quantify how rare events amplify a fixed absolute implementation error.

## Independent phase flips on leaf links

Apply an independent $`Z`$ flip to leaf $`i`$ with probability $`e_i\in[0,1/2]`$ in the Schmidt basis before the hub protocol. The figure of merit is the GHZ fidelity after known corrections for the observed herald. The flips act on separate registers from the hub and hence leave every hub record probability unchanged. They commute through the uncorrected conditional preparation and are then conjugated by the leaves' recorded corrections.

- On a complementary-GHZ branch all corrections are Pauli gates. The leaf phase flips remain phase flips, and the GHZ phase is correct exactly when their parity is even. Thus $`F_{\mathrm{comp}}=(1+\prod_i(1-2e_i))/2`$.
- On a parity branch the leaf corrections include a Hadamard on every qubit. The same phase flips become bit flips on the corrected GHZ. Only the all-zero and all-one bit-flip patterns preserve the state, giving $`F_{\mathrm{par}}=\prod_i(1-e_i)+\prod_i e_i`$.

With three leaves and identical $`e`$, these are $`1-3e+6e^2-4e^3`$ and $`1-3e+3e^2`$, respectively. Both have first-order loss $`3e`$. Here $`F_{\mathrm{comp}}-F_{\mathrm{par}}=3e^2-4e^3\ge 0`$. At a fixed per-branch target fidelity $`F_\mathrm{target}\le F_{\mathrm{par}}`$, both branch types are accepted and the herald-rate gain over complementary-basis concentration still holds. This comparison implements concentration locally at the hub in both protocols and charges all star attempts. The exact percolation statement concerns the pure ideal model.

## Endpoint fidelity on a finite path

Use the [occupied-path protocol](NETWORK.md) for $`k`$ three-leaf stars, with ideal fusion and local readout. Fix the path using the herald records before the fusion outcomes. Phase errors remain independent given the records because their distributions were independent of the hub measurements. Use the announced $`X`$ result on each unused third qubit to correct the ideal Bell phase before tracking subsequent swaps.

On a complementary branch, a phase flip on that measured qubit flips its $`X`$ result and changes the inferred Bell phase. Combining it with phase flips on the kept qubits gives a net Bell phase error equal to the parity of all three original flips. On a parity branch, $`X`$ on the discarded qubit neither changes the outcome probabilities nor adds a Bell label. The bit error is the parity of the original flips on the two kept qubits. Ideal Bell swapping adds incoming Pauli labels modulo two, after the measured swap label has been corrected. The phase and bit errors arise from disjoint sets of stars and are independent. Consequently the exact conditional fidelity of the corrected endpoint pair is

```math
F_{\mathrm{path}}=F_C F_H,
\qquad
F_C=\tfrac12\left[1+\prod_{v\in C}\prod_{i=1}^3(1-2e_{v,i})\right],
\qquad
F_H=\tfrac12\left[1+\prod_{v\in H}\prod_{i\in K_v}(1-2e_{v,i})\right],
```

where $`C`$ and $`H`$ are the complementary and parity branches along the path, and $`K_v`$ is the pair of qubits kept from star $`v`$. Empty products equal one. At equal $`e`$, the exponents of $`(1-2e)`$ in the first and second factors are $`3|C|`$ and $`2|H|`$. This formula makes separate predictions for successful routing and fidelity after routing. A positive connection probability over long distances can coexist with the accumulation of both types of Pauli errors.

## Flagged loss after exact preparation

Suppose a successful, otherwise ideal three-leaf state is independently discarded with probability $`\ell`$ and the extra discard is announced. Conditional on survival, the state is still exact GHZ. The occupation events remain independent and the [network threshold](NETWORK.md#threshold-and-matched-comparison) is reached when $`(1-\ell)P_3(q)>1/2`$.

At $`q=5/16`$, exact preparation gives $`P_3=1075/2048`$. The protocol remains supercritical for $`\ell<51/1075`$, or about $`4.74\%`$ extra loss per successful star. The baseline's occupation probability is already below one half at this link strength. This margin applies to independent flagged discards. For an unflagged gate or link error, use the fidelity measures above.
