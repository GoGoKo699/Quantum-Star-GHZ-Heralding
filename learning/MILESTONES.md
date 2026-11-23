# Project understanding map

The 30 milestones follow the science from independent qubit pairs to the success law, broadcast budgets and the honeycomb application. Twelve background milestones build the operating model from its individual quantum objects. Eighteen narrative milestones cover the diagonal constraint, a constructive measurement, the exact three-leaf consequences and the network interpretation.

Use the [Watrous bridge](WATROUS_BRIDGE.md) to locate sections in the educational anchor and follow a complete example. The scientific sources carry the full arguments. A target marks what the reader should be able to explain after studying that milestone.

| Phase | Milestones | Connection established |
|---|---|---|
| Background | [M01](#m01-qubit-bases-and-bitstrings)–[M05](#m05-the-leaf-marginal) | Product Schmidt amplitudes determine the leaf marginal |
| Background | [M06](#m06-the-ghz-target)–[M12](#m12-the-one-way-star-task) | The exact target, measurement records and scope define the success objective |
| Narrative | [M13](#m13-the-complementary-cat-branches)–[M20](#m20-the-clipped-median) | Complementary-pair budgets give the even and odd optima |
| Narrative | [M21](#m21-coherent-probability-allocation)–[M27](#m27-the-weakest-link-cut) | The hub instrument attains the formula, and counting broadcast labels constrains the success probability |
| Narrative | [M28](#m28-independent-star-occupations)–[M30](#m30-the-complete-scientific-story) | The local gain shifts a lattice threshold under the specified model |

## Phase I · Background and preliminaries

### M01 Qubit bases and bitstrings

**Central question.** How are qubits and joint basis configurations represented?

**Understanding target.** Read a computational-basis string as one outcome label for a tensor product of two-dimensional registers.

**Dependencies and story role.** Starting point.

**Conceptual connection.** The hub and leaves each have one register for each source, so a single string labels matched configurations across the star.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 1.1.1 and 2.1.2 · [Model](../science/MODEL.md)

### M02 Amplitudes and outcome probabilities

**Central question.** How does a measurement read a superposition?

**Understanding target.** Relate the amplitude of a basis component to its squared-modulus measurement probability and explain when amplitudes can interfere.

**Dependencies and story role.** M01. Connects basis labels to measurement statistics.

**Conceptual connection.** The phase of a component can cancel or reinforce another component after a change of basis.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 1.1.1 and 2.3.1

### M03 One pure entangled link

**Central question.** What does the smaller Schmidt probability tell us about a link?

**Understanding target.** Write the two terms of a qubit pair in its Schmidt bases and recognize the product and maximally entangled endpoints.

**Dependencies and story role.** M01–M02. Identifies the resource at one edge.

**Conceptual connection.** The smaller probability sets the cost of balancing the two Schmidt components of a pure pair.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Section 1.1.3 · [Model](../science/MODEL.md)

### M04 Independent links in a star

**Central question.** How do separately prepared pairs form a single bipartite state?

**Understanding target.** Group the hub registers and the leaf registers, then explain why the distributions on strings factor over edges.

**Dependencies and story role.** M01–M03. Builds the complete input from edge resources.

**Conceptual connection.** The hub and all leaves share the same string label in their respective Schmidt bases.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 1.1.1 and 2.1.2–2.1.3 · [Model](../science/MODEL.md)

### M05 The leaf marginal

**Central question.** What can the leaves see before the hub sends any information?

**Understanding target.** Trace out the hub and recover the diagonal leaf operator. Explain how discarding the hub removes the coherence between different string labels.

**Dependencies and story role.** M03–M04. Identifies the unconditioned operator of the output subsystem.

**Conceptual connection.** This operator is the fixed average over every possible hub outcome and sets the later probability budgets.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Section 2.1.3 · [Model](../science/MODEL.md)

### M06 The GHZ target

**Central question.** What does it mean to have prepared an exact GHZ state?

**Understanding target.** Identify the two coherent terms of GHZ, its local one-qubit marginals and the missing phase coherence in the corresponding classical mixture.

**Dependencies and story role.** M01–M02 and M05. Specifies what the hub aims to deliver.

**Conceptual connection.** The target has one ebit across any single-leaf cut, a fact that later bounds the success probability.

**Sources.** [Model](../science/MODEL.md) · [Optimality](../science/OPTIMALITY.md)

### M07 The local-unitary GHZ orbit

**Central question.** How much freedom do the leaves have once the hub announces a label?

**Understanding target.** Express a correctable GHZ state using two orthonormal columns at each leaf. Account for local basis changes and a relative phase correction.

**Dependencies and story role.** M01, M03 and M06. Converts the output rule into a family of success states.

**Conceptual connection.** The orthogonality of the local columns is the key relationship used to constrain the computational diagonal.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 1.1.1 and 2.1.2 · [Optimality](../science/OPTIMALITY.md)

### M08 Readout and conditional correction

**Central question.** Why does the announced label matter to the leaves?

**Understanding target.** Compute the conditioned state for a hub projection and identify how a known sign or bit pattern can be corrected locally.

**Dependencies and story role.** M02, M04 and M06–M07. Connects a quantum measurement to the one-way classical message.

**Conceptual connection.** Different hub outcomes may produce different pre-correction states within the same correctable orbit.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 2.3.1–2.3.2 · [Model](../science/MODEL.md)

### M09 Generalized measurements and a meter

**Central question.** What measurements does the model permit beyond a fixed basis measurement?

**Understanding target.** Distinguish an outcome effect from a conditional measurement operator and explain how a meter and a projective readout realize a generalized measurement.

**Dependencies and story role.** M02 and M08. Introduces the implementable hub controls.

**Conceptual connection.** Two outcomes of one coherent filter can have different diagonal attenuation profiles while preserving within-branch superpositions.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 2.2.2 and 2.3.1–2.3.2 · [Implementation](../science/IMPLEMENTATION.md)

### M10 Subnormalized leaf ensembles

**Central question.** How do probabilities and conditional states fit in one operator?

**Understanding target.** Use the trace of a subnormalized leaf operator as the branch probability and use completeness to bound the sum of the successful operators by the marginal.

**Dependencies and story role.** M05, M08 and M09. Introduces the resource inequality.

**Conceptual connection.** Every computational diagonal entry has a capacity whether the hub uses projectors, a general measurement or a sequence of local stages.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Exercise 2.2 · [Model](../science/MODEL.md)

### M11 Local operations and cut bounds

**Central question.** What upper bound survives if the labs are allowed extra local operations?

**Understanding target.** Isolate one leaf from the rest of the network and relate the pure-state stochastic conversion bound to that leaf's Schmidt probabilities.

**Dependencies and story role.** M03 and M06–M09. Establishes a more permissive comparison model.

**Conceptual connection.** The bound applies even if leaves can filter or send feedback, provided operations remain local across the cut.

**Sources.** [Watrous bridge](WATROUS_BRIDGE.md), Sections 6.1.2 and 6.2.1 · [Related work](../references/RELATED.md)

### M12 The one-way star task

**Central question.** What counts as a trial, a success and an admissible operation?

**Understanding target.** State all parts of the task together: a supply of calibrated pure links, a hub instrument, an announced outcome, local unitaries and exact conditional GHZ output.

**Dependencies and story role.** M01–M11. Integrates the prerequisites into the operational problem.

**Conceptual connection.** The objective is single-attempt success probability with one pair per edge. Network percolation and approximate-state performance have separate assumptions.

**Sources.** [Model](../science/MODEL.md)

## Phase II · Narrative and innovation

### M13 The complementary cat branches

**Central question.** What does a fixed GHZ-basis measurement produce?

**Understanding target.** Track the two amplitudes for a pair of complementary strings and see how the original Schmidt weights carry into the conditional leaf state.

**Dependencies and story role.** M04, M06, M08 and M12. Establishes the experimental baseline.

**Conceptual connection.** The outcome label identifies a correctable pair and a phase, while imbalance may require a probabilistic filter.

**Sources.** [Implementation](../science/IMPLEMENTATION.md) · [Related work](../references/RELATED.md)

### M14 The best complementary protocol

**Central question.** How much probability can one complementary pair supply?

**Understanding target.** Explain why balancing to the smaller entry gives twice that entry as the combined probability for both phase outcomes.

**Dependencies and story role.** M09–M10 and M13. Builds a matched benchmark from all pairs.

**Conceptual connection.** Early hub filtering and optimal concentration after a fixed complementary measurement give the same benchmark yield.

**Sources.** [Optimality](../science/OPTIMALITY.md) · [Implementation](../science/IMPLEMENTATION.md)

### M15 The local interference sign

**Central question.** How does complementing a basis bit affect the diagonal of a rotated GHZ state?

**Understanding target.** Expand a local-unitary GHZ diagonal into two product terms and an interference term. Use orthogonality of the two local columns to see the sign change.

**Dependencies and story role.** M02 and M07. Finds the local identity behind the global constraint.

**Conceptual connection.** Complementing every bit swaps the two product terms and contributes one interference sign change per leaf.

**Sources.** [Optimality](../science/OPTIMALITY.md)

### M16 Even-star optimality

**Central question.** Why can a more general hub measurement offer no greater even-star yield?

**Understanding target.** Combine the even-star complementary equality for every success with the marginal capacities and recover the upper bound that complementary balancing attains.

**Dependencies and story role.** M10 and M14–M15. Converts the symmetry into a sharp converse.

**Conceptual connection.** Every successful outcome must use paired diagonal entries in equal amounts, regardless of the hub measurement and local basis choices.

**Sources.** [Optimality](../science/OPTIMALITY.md)

### M17 The odd-star excess

**Central question.** What form can the complementary mismatch take for an odd number of leaves?

**Understanding target.** Show why the difference between the even member of a pair and its odd complement is the same for every pair of an odd-star success diagonal.

**Dependencies and story role.** M07, M10 and M15. Identifies the one extra degree of freedom.

**Conceptual connection.** Adding successful branch operators preserves this common excess, giving one scalar for the whole success ensemble.

**Sources.** [Optimality](../science/OPTIMALITY.md)

### M18 The two attainable diagonal parts

**Central question.** How can a nonnegative success diagonal with common excess be realized?

**Understanding target.** Remove the uniform mass on the favored parity and identify a nonnegative, complement-symmetric remainder.

**Dependencies and story role.** M14 and M17. Links the converse to a construction.

**Conceptual connection.** Balanced cats realize the symmetric part and locally rotated GHZ states span the uniform chosen parity contribution.

**Sources.** [Optimality](../science/OPTIMALITY.md) · [Implementation](../science/IMPLEMENTATION.md)

### M19 Capacities for the common excess

**Central question.** How much weight can the hub allocate to one parity?

**Understanding target.** Determine the shift interval from the smallest available probability on each parity and identify the smaller residual budget in each pair.

**Dependencies and story role.** M10 and M17–M18. Builds the finite optimization domain.

**Conceptual connection.** The most depleted basis string limits a uniform shift across its entire parity sector.

**Sources.** [Optimality](../science/OPTIMALITY.md)

### M20 The clipped median

**Central question.** Why does the optimum reduce to one constrained median?

**Understanding target.** Write the lost mass as a sum of absolute deviations of complementary differences from the shift. Explain why a median minimizes the unconstrained sum and why clipping handles the interval.

**Dependencies and story role.** M14 and M17–M19. Solves the odd-star success optimization.

**Conceptual connection.** One scalar allocation determines both the parity yield and every remaining balanced pair.

**Sources.** [Optimality](../science/OPTIMALITY.md) · [Watrous bridge example](WATROUS_BRIDGE.md#worked-example-with-three-identical-links)

### M21 Coherent probability allocation

**Central question.** How does the hub reserve uniform mass without measuring the input string?

**Understanding target.** Describe the two-outcome diagonal filter and explain how its single residual outcome maintains the coherence needed for the next stage.

**Dependencies and story role.** M09–M10 and M18–M20. Begins the optimal instrument.

**Conceptual connection.** Each diagonal amplitude attenuation spends probability while preserving superpositions within its announced branch.

**Sources.** [Implementation](../science/IMPLEMENTATION.md)

### M22 Correcting the parity branch

**Central question.** How does uniform support on one parity become a GHZ state?

**Understanding target.** Track the phases arising from hub X-basis outcomes, remove them locally and use Hadamards to map the uniform parity superposition to GHZ.

**Dependencies and story role.** M07–M08 and M18–M21. Completes the extra successful branch.

**Conceptual connection.** The Fourier transform of a parity-sector indicator has support on the two complementary strings of GHZ.

**Sources.** [Implementation](../science/IMPLEMENTATION.md)

### M23 Balancing the residual branch

**Central question.** How is complementary concentration reused after moving probability to the parity branch?

**Understanding target.** Use the residual capacities to choose a coherent pair-balancing step, then explain how a complementary label and relative sign permit leaf corrections.

**Dependencies and story role.** M13–M14 and M19–M21. Completes the complementary branch of the optimal design.

**Conceptual connection.** The residual calculation must use probabilities left by the first filter, so the two branches never spend the same input probability.

**Sources.** [Implementation](../science/IMPLEMENTATION.md)

### M24 One instrument and one announcement

**Central question.** How do the two branches fit into an allowed star protocol?

**Understanding target.** Account for the hub meter, conditional basis readout, classical label and final leaf unitaries. Explain why the hub can perform its own feed-forward before sending a single message and how to count outcome words, including failure.

**Dependencies and story role.** M09, M12 and M21–M23. Synthesizes the optimal construction.

**Conceptual connection.** Homogeneous links yield weight-based filter tables. The theorem fixes success probability even when table preparation and controlled rotations are costly.

**Sources.** [Model](../science/MODEL.md) · [Implementation](../science/IMPLEMENTATION.md) · [Broadcast budgets](../science/COMMUNICATION.md)

### M25 Three unequal links

**Central question.** What determines whether a three-leaf star benefits from parity?

**Understanding target.** Relate the ordering of complementary probabilities to the weakest link and the two stronger links. Use the three-link formula to identify the active constraint.

**Dependencies and story role.** M14 and M17–M20. Specializes the theorem to the smallest odd network.

**Conceptual connection.** In a strongly unbalanced star, complementary branches can already attain the weakest-link cut. Other stars can use extra odd-sector probability.

**Sources.** [Optimality](../science/OPTIMALITY.md)

### M26 Three equal links worked through

**Central question.** How do the parity and complementary success contributions add at a particular calibration?

**Understanding target.** Trace the calculation at smaller Schmidt probability 2/5, including capacities, selected shift, branch yields and the final probability 4/5. Recover the one-label probability from the rank-one effect and explain why it multiplies by three at two bits.

**Dependencies and story role.** M20–M25. Makes the resource allocation concrete before the lattice application.

**Conceptual connection.** The matched complementary yield is 0.704 because it balances the original four pairs without a parity assignment.

**Sources.** [Watrous bridge example](WATROUS_BRIDGE.md#worked-example-with-three-identical-links) · [Broadcast example](WATROUS_BRIDGE.md#charge-the-broadcast-on-the-same-example) · [Verification](../verification/README.md)

### M27 The weakest-link cut

**Central question.** When is the one-way optimum also optimal with unrestricted LOCC?

**Understanding target.** Use the cut bound to justify global LOCC optimality where the one-way yield reaches twice the weakest Schmidt probability. Identify what the bound says when there is a gap.

**Dependencies and story role.** M11 and M25–M26. Compares the theorem with a broader operational class.

**Conceptual connection.** For three equal links the cut is attained from the calibrated crossover up to perfect Bell links. In weaker regimes the one-way theorem still applies.

**Sources.** [Optimality](../science/OPTIMALITY.md) · [Related work](../references/RELATED.md)

### M28 Independent star occupations

**Central question.** How does a honeycomb network produce a triangular site-percolation process?

**Understanding target.** Identify the hub color class, show that its stars consume independent link registers, and explain how neighboring successful stars meet and fuse at a shared lab.

**Dependencies and story role.** M04, M12 and M24–M26. Transfers the local success law to a lattice construction.

**Conceptual connection.** Two neighboring stars can use separate qubits at the same leaf. Their success indicators remain independent before fusion.

**Sources.** [Network](../science/NETWORK.md)

### M29 From local probability to link threshold

**Central question.** How does the parity measurement change the minimum link strength for this lattice construction?

**Understanding target.** Compare the two three-link success curves against site occupation probability one half and interpret the two critical Schmidt probabilities.

**Dependencies and story role.** M14, M25–M26 and M28. Connects a finite-star advantage to a large-scale consequence.

**Conceptual connection.** Exact ideal GHZ production and local fusion support the site-percolation inference. Finite error requires a separate fidelity calculation.

**Sources.** [Network](../science/NETWORK.md) · [Robustness](../science/ROBUSTNESS.md)

### M30 The complete scientific story

**Central question.** Which parts of the result survive as the physical model changes?

**Understanding target.** Summarize the exact even and odd optima, reconstruct how the hub attains them, and distinguish finite-star optimality, broadcast-limited heralding, the lattice protocol threshold and noisy-output guarantees.

**Dependencies and story role.** M12, M16, M20, M24 and M27–M29. Integrates the full contribution.

**Conceptual connection.** The input marginal constrains every success. Orthogonal local GHZ columns determine what its diagonal can spend. The same argument guides the constructive instrument and tells where its assumptions matter.

**Sources.** [Model](../science/MODEL.md) · [Optimality](../science/OPTIMALITY.md) · [Implementation](../science/IMPLEMENTATION.md) · [Broadcast budgets](../science/COMMUNICATION.md) · [Network](../science/NETWORK.md) · [Robustness](../science/ROBUSTNESS.md) · [Verification](../verification/README.md)
