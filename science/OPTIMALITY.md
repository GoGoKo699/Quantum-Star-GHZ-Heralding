# Exact heralding probability

[Star model](MODEL.md) · [Achieving instrument](IMPLEMENTATION.md) · [Verification](../verification/README.md)

Let $C$ run over the unordered complementary pairs of strings. The optimal probability on an even star is

```math
P_{\mathrm{even}}=2\sum_{C=\{x,\bar x\}}\min(p_x,p_{\bar x}).
```

On an odd star, each pair has one even representative $e$. Let $d_e=p_e-p_{\bar e}$ and define $I=[-\min_{\mathrm{odd}}\ p_x,\min_{\mathrm{even}}\ p_x]$. Then

```math
P_{\mathrm{odd}}=1-\min_{t\in I}\sum_{\mathrm{even}\ e}\lvert d_e-t\rvert .
```

To obtain an optimizer, take any median of the numbers $d_e$ and clamp it to $I$. The optimum includes the complementary baseline by choosing $t=0$.

## The computational diagonal of a corrected-success state

Every pre-correction pure success state has the form

```math
\frac{\bigotimes_i u_i+\bigotimes_i v_i}{\sqrt{2}},
\qquad
\langle u_i,v_i\rangle=0 ,
```

where $u_i$ and $v_i$ are the columns of a two-dimensional unitary. At a string $x$, its probability is the sum of a squared-amplitude term and an interference term:

```math
\frac12\left(\prod_i\lvert u_i(x_i)\rvert^2+
             \prod_i\lvert v_i(x_i)\rvert^2\right)
+\mathrm{Re}\prod_i\left(u_i(x_i)\overline{v_i(x_i)}\right).
```

The first term is complement symmetric because swapping the bit at every leaf interchanges the two column probabilities. The interference factor at bit $0$ is the negative of the factor at bit $1$ by column orthogonality. Thus the interference term depends only on parity and changes by a factor of $(-1)^N$ under complement.

Write $r_x$ for the sum of all successful branch probabilities at string $x$, each weighted by its herald probability. The conditional-state relation in the [model](MODEL.md#conditional-states) gives $0\leq r_x\leq p_x$, and the parity calculation gives

```math
\begin{cases}
r_x=r_{\bar x}, & N\text{ even},\\
r_e-r_{\bar e}=t\text{ common to every even }e, & N\text{ odd}.
\end{cases}
```

This conclusion uses the measurement outcome only through its local corrections. It applies to arbitrary hub instruments.

## Optimize the capped success diagonal

For even $N$, set each pair's common success weight to the smaller probability of its two strings. For odd $N$, nonnegativity and the caps make $t\in I$ necessary. Fix such a $t$. If $t\geq 0$, reserve $t$ in the even entry of each pair and then fill both remaining entries up to their shared minimum. If $t<0$, reserve $-t$ in the odd entry instead. In either case the pair total is

```math
p_e+p_{\bar e}-\lvert p_e-p_{\bar e}-t\rvert.
```

No diagonal with that $t$ can do better termwise. Summation reduces the problem to a scalar absolute-deviation minimization. Its unconstrained minimizers form the median set, and clamping any median gives a constrained minimizer.

This diagonal bound is tight for a quantum instrument. A uniformly weighted state on even strings is obtained by applying a Hadamard on every qubit of $\lvert G_N\rangle$. For odd strings, put a minus phase between the two GHZ components before those Hadamards. A hub filter and X measurements realize the reserved parity mass, while the residual balanced pairs are realized by the complementary branch of the [explicit instrument](IMPLEMENTATION.md). In particular, the proof only used diagonal constraints for the converse and the attaining protocol is physical without needing an assumption about off-diagonal feasibility.

## Three leaves

For independent link probabilities $q_1\leq q_2\leq q_3$, define $B=q_1q_2q_3$ and $\Delta=p_{100}-p_{011}$. The optimal probability is

```math
P_3=2q_1-2\max\{0,\Delta-B\}
=2\min\{q_1,q_2,q_3,\ q_1q_2+q_1q_3+q_2q_3-q_1q_2q_3\}.
```

To see the correction explicitly, compare the four even–odd differences. The difference for the pair $000,111$ is nonnegative. The differences for even $101$ and $110$ are nonpositive. The remaining difference, for even $011$, equals $-\Delta$ and is at least the differences for $101$ and $110$. For example $p_{011}-p_{100}-(p_{101}-p_{010})=q_2-q_1$. Thus if $\Delta\leq 0$, zero is a median and the bound $2q_1$ is already achieved by complementary swapping. If $\Delta>0$, the median nearest zero is $-\Delta$, and the allowed negative shift has magnitude at most $p_{111}=B$. The complementary protocol yields $`2q_1-2\max\{0,\Delta\}`$ by summing the four smaller pair weights. The gain is $`2\min\{B,\max(0,\Delta)\}`$, yielding the formula.

For identical links this simplifies to

```math
P_3(q)=\min\{2q,6q^2-2q^3\},\qquad
P_{\mathrm{comp}}(q)=6q^2-4q^3 .
```

For $q\geq(3-\sqrt{5})/2$, the protocol attains the weakest-leaf cut bound $2q$, so it is also optimal among all LOCC protocols for that regime. Below this value, general LOCC and the one-way hub model can be distinguished by their allowable operations. The upper bound $2q$ alone does not settle whether leaf filtering or feedback can improve the one-way optimum there.

At $q=0$, the state contains no entanglement and both rates vanish. At $q=1/2$, complementary swapping is deterministic. At $q=5/16$, the probability rises from $475/1024$ to $1075/2048$ and crosses $1/2$, which is the relevant [site-percolation threshold](NETWORK.md).
