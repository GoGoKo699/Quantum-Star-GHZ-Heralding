# Learn star GHZ heralding

A hub shares one known qubit pair with each leaf. It measures its own qubits, announces the outcome and lets the leaves correct their state with local unitaries. The goal is an exact Greenberger–Horne–Zeilinger (GHZ) state on the leaves whenever the hub announces success.

Start with the [Watrous bridge](WATROUS_BRIDGE.md), which includes a three-link example from the input probabilities through both branches of the measurement. Follow the [30-milestone map](MILESTONES.md) for the complete study route. The [scientific model](../science/MODEL.md), [optimality proof](../science/OPTIMALITY.md) and [implementation](../science/IMPLEMENTATION.md) give the formal account.

The educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018). Its treatment of Schmidt decomposition, purification, ensembles and quantum measurements explains why a hub measurement can realize a conditional leaf ensemble. The project supplies the GHZ parity constraint, the optimal filter and the lattice application. [Author's manuscript and chapter links](https://jhwatrous.github.io/books-and-courses.html) · [Published edition](https://doi.org/10.1017/9781316848142)

| Route | What it explains |
|---|---|
| [M01–M12](MILESTONES.md#m01-qubit-bases-and-bitstrings) | How independent qubit pairs, hub measurements and local corrections define the task |
| [M13–M24](MILESTONES.md#m13-the-complementary-cat-branches) | How the target's diagonal constrains the yield and how the hub attains it |
| [M25–M30](MILESTONES.md#m25-three-unequal-links) | Three-link examples, the weakest-link bound, the honeycomb threshold and the scope of the result |

For the literature and the numerical checks, see [related work](../references/RELATED.md) and [verification](../verification/README.md).

