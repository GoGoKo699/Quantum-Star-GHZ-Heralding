# Quantum Star GHZ Heralding

From one calibrated, partially entangled qubit pair per leaf, a hub can herald an exact Greenberger–Horne–Zeilinger (GHZ) state across the leaves. It performs one joint instrument and broadcasts the result. The leaves apply local unitaries.

The optimal instrument depends on the number of leaves. On even stars, balancing the weights of complementary Schmidt strings achieves the maximum success probability. On odd stars, a second branch can coherently combine all strings of one parity. A median of the complementary weight differences determines how much probability to allocate to this branch.

For three identical links with smaller Schmidt probability $q$, the exact optimum is

```math
P_3(q)=\min\{2q,\ 6q^2-2q^3\}.
```

Standard GHZ-basis swapping followed by optimal branchwise concentration gives $6q^2-4q^3$. At $q=0.4$, its success probability is $0.704$ and the new instrument reaches $0.800$, the upper bound from cutting one leaf off the star. In the independent-star protocol on a single-layer honeycomb lattice, the new measurement lowers the critical link parameter from $0.32635$ to $0.30455$.

When the hub has one or two broadcast bits, the best probabilities at $q=0.4$ are $0.1152$ and $0.3456$. With four accepted labels and a separate failure word, a rotated instrument achieves $0.45959386$, above the complementary-basis optimum $0.44434286$. Four bits are necessary and sufficient to reach $0.800$ in the one-way model. [Broadcast budgets](science/COMMUNICATION.md)

| Read for | Start here |
| --- | --- |
| Inputs, operations and success criterion | [Star model](science/MODEL.md) |
| Exact probability, proof and three-leaf formula | [Optimality](science/OPTIMALITY.md) |
| Hub filters, broadcast and corrections | [Implementation](science/IMPLEMENTATION.md) |
| Exact low-bit optima and bounds with four accepted labels | [Broadcast budgets](science/COMMUNICATION.md) |
| Honeycomb threshold and local fusion | [Network application](science/NETWORK.md) |
| Phase errors, filter tolerances and herald loss | [Robustness](science/ROBUSTNESS.md) |
| Prior swapping and percolation protocols | [Related work](references/RELATED.md) |
| Reproduce finite checks | [Verification](verification/README.md) |
| Study the tools and work through the result | [Learning guide](learning/README.md) |

The exact star theorem uses known pure links and ideal local operations. The lattice threshold is for independent preparation followed by ideal local fusion. With noisy links, the accepted output generally has fidelity below one. The repository includes finite checks, a proof account and a learning route based on John Watrous's *The Theory of Quantum Information*.

The companion project derives a communication converse for a discarded hub and arbitrary independent pair sources. The calibrated link probabilities in this project allow sharper bounds and a direct comparison of hub instruments within the same message budget. [GHZ Communication Cost](https://github.com/GoGoKo699/GHZ-Communication-Cost)

## Purpose and contact

This repository documents the mathematical results and provides a route to reproduce and study them. For questions or corrections, contact Ruge Lin through [GitHub](https://github.com/GoGoKo699) or open an issue.
