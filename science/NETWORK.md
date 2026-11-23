# Lowering the threshold on a single-layer honeycomb network

[Star model](MODEL.md) · [Achieving instrument](IMPLEMENTATION.md) · [Related work](../references/RELATED.md)

The three-leaf [hub instrument](IMPLEMENTATION.md) lowers the minority Schmidt weight required for Bell-pair percolation in the single-layer honeycomb architecture of [Khanna, Halder, and Sen, Sec. III.A](https://doi.org/10.1103/PhysRevA.109.012419). The comparison uses the same edge states, local ports, and fusion operations. The change occurs at the hub, before routing. The critical weight is approximately **0.304546849**, down from **0.326351822** with complementary-GHZ measurements and branch concentration.

## Independent site process from the same edge states

Use the two vertex classes $A$ and $B$ of the honeycomb lattice. Each edge supplies one independent copy of $\sqrt{1-q}\,|00\rangle+\sqrt q\,|11\rangle$, with $0\le q\le 1/2$. Three qubits meet at each vertex. A vertex of class $A$ acts as a hub and its three neighboring $B$ vertices are the leaves of that star. Each $B$ vertex keeps separate leaf qubits for its three incident $A$ stars.

All hubs apply the same independent instrument and broadcast their records. Apply the local corrections from each record. Keep the three-leaf GHZ state for every success and discard the associated leaf qubits for every failure. The edge inputs factor over $A$ stars because every edge has exactly one endpoint in $A$. Hub measurement instruments act on distinct factors, even when the corresponding stars share a physical $B$ station. The heralds are therefore independent Bernoulli variables with parameter $p=P(q)$, the single-star success probability.

Declare two $A$ vertices adjacent whenever they share a $B$ neighbor. This is the triangular lattice. For example, label the vertices so $B_{i,j}$ has neighbors $A_{i,j}$, $A_{i-1,j}$ and $A_{i,j-1}$. The induced steps on $A$ are $\pm(1,0)$, $\pm(0,1)$ and $\pm(1,-1)$. The shared $B$ neighbor for a pair of adjacent $A$ vertices is unique and holds two distinct qubits, one from each star. Successful hubs are the occupied sites of independent triangular site percolation.

## Bell-pair delivery on an occupied path

For two distinct terminal $B$ stations $u,v$, take a shortest occupied path between their sets of incident $A$ vertices. The first and last stars reserve their qubit at $u$ and $v$, respectively. If both stations are incident to one successful hub, the path consists of that one hub. Consecutive path edges use distinct intermediate stations. Otherwise three successive hubs share a $B$ station and admit a shortcut. Two nonconsecutive steps also cannot share a $B$ station, since that station has only three incident hubs and a shortest path has distinct vertices. A shortest path between the endpoint sets leaves the terminals free of fusion measurements, since stepping through either terminal would allow starting later or ending earlier within its incident set.

In every star on the path, measure its unused third qubit in the $X$ basis. On outcome $(-1)^s$, the remaining two qubits are in $(|00\rangle+(-1)^s|11\rangle)/\sqrt 2$. The record gives a known $Z^s$ correction. At each internal $B$ station perform a Bell measurement on the two path qubits from its incident path stars. With Bell basis $|\beta_{r,s}\rangle=(|0,r\rangle+(-1)^s|1,1\oplus r\rangle)/\sqrt 2$, the ideal swap produces an endpoint Bell state with Pauli label $(r,s)$, up to known incoming labels and a global phase. Each outcome has probability $1/4$. Tracking the labels and applying the endpoint Pauli correction produces $|\Phi^+\rangle$. A path of $k$ stars uses $k$ single-qubit measurements and $k-1$ Bell measurements, after the hub instruments and local corrections. These measurements add no probabilistic loss in the ideal model.

Conditioned on all herald records, the retained resource states are a tensor product across occupied components. A $B$ station with retained qubits from several hubs can only connect hubs in the same component, by definition of adjacency. If the terminal incident sets do not meet a common occupied component, the conditional resource is separable across the corresponding partition of stations. Local operations and classical communication on these retained qubits cannot generate a Bell pair across this partition. Thus connectivity is necessary and sufficient in this scheme, including when routing adapts to the herald records.

## Threshold and matched comparison

The open probability for the published complementary-GHZ basis followed by optimal branch concentration is

```math
p_{\mathrm{comp}}(q)=2q^3+6q^2(1-q)=6q^2-4q^3.
```

For each complementary pair of strings $\{x,\bar x\}$, concentration contributes exactly $2\min(p_x,p_{\bar x})$, by the bipartite cut through any one leaf of that branch. The comparison gives this whole probability to the baseline. It can be implemented either by the published local concentration or by the hub filter in [Implementation](IMPLEMENTATION.md).

The [three-leaf optimum](OPTIMALITY.md) yields

```math
p_{\mathrm{hub}}(q)=\min\{6q^2-2q^3,\,2q\}.
```

The triangular-lattice site threshold is [exactly $1/2$](https://people.math.harvard.edu/~ctm/home/text/class/harvard/219/21/html/home/sources/smirnov_long.pdf). Above it the occupied graph has a [unique infinite component](https://sites.math.northwestern.edu/~auffing/papers/BurtonKeane.pdf) and the probability of connecting two fixed stations remains bounded away from zero as they separate. Choose one incident hub in advance at each terminal. Both hubs belong to the infinite component with probability at least $\theta(p)^2$ by positive association of the two increasing membership events, where $\theta(p)$ is the site probability of belonging to the infinite component. At and below the critical point all occupied clusters are finite almost surely, so the probability that an incident hub of the first terminal connects to one arbitrarily far away tends to zero. These statements use the infinite-lattice connection event, which is the increasing limit of corresponding finite-patch events for each fixed pair of terminals.

| Hub preparation | Critical $q$ | Equation at the threshold |
| --- | ---: | --- |
| Complementary-GHZ basis and concentration | $\frac12-\sin(\pi/18)\approx 0.326351822$ | $6q^2-4q^3=1/2$ |
| Optimized hub instrument | $0.304546849\ldots$ | $6q^2-2q^3=1/2$ |

Independent edge filtering gives open honeycomb bonds with probability $2q$. The honeycomb bond threshold is $1-2\sin(\pi/18)$, so this baseline has the same critical $q$ as complementary preparation. The new interval therefore improves both same-lattice benchmarks.

Both critical weights are the unique roots in $(0,1/2)$ of the displayed equations. The optimized root is on the cubic branch since $1/2<2(3-\sqrt5)/2$, the site probability at the switch to the linear branch. At the exact test point $q=5/16$, the baseline has $p=475/1024<1/2$, whereas the optimized instrument has $p=1075/2048>1/2$. The resource requirements still include one calibrated pure pair per edge and ideal local operations. The improved instrument uses a local meter and calibrated rotations at each hub. The critical weights describe independent exact-GHZ preparation followed by routing on retained states. A protocol that keeps failed fragments or processes neighboring stars jointly before declaring their heralds has a different optimization problem.

The local probability theorem is in [Optimality](OPTIMALITY.md), the circuit in [Implementation](IMPLEMENTATION.md), and the finite-path noise calculation in [Robustness](ROBUSTNESS.md).
