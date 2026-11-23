#!/usr/bin/env python3
"""Verify ideal star GHZ heralding with exact arithmetic and explicit amplitudes."""

from fractions import Fraction as Q
from math import isclose, pi, prod, sin, sqrt
from random import Random


def parity(x):
    return x.bit_count() % 2


def complement_pairs(n):
    mask = (1 << n) - 1
    if n % 2:
        return [(x, x ^ mask) for x in range(mask + 1) if not parity(x)]
    return [(x, x ^ mask) for x in range((mask + 1) // 2)]


def product_probabilities(weights):
    return [
        prod(q if (x >> k) & 1 else 1 - q for k, q in enumerate(weights))
        for x in range(1 << len(weights))
    ]


def optimal_probability(p, n):
    pairs = complement_pairs(n)
    differences = sorted(p[x] - p[y] for x, y in pairs)
    shift = Q(0)
    if n % 2:
        lower = -min(p[y] for _, y in pairs)
        upper = min(p[x] for x, _ in pairs)
        shift = min(upper, max(lower, differences[len(pairs) // 2]))
    probability = 1 - sum(abs(d - shift) for d in differences)
    return probability, shift


def packing_probability(p, n):
    """Solve an independent rational packing LP by primal simplex.

    Each column is the componentwise budget consumed by one unit of
    an allowed success diagonal. The right-hand side is the input diagonal.
    Slack variables give an immediate feasible starting point.
    """
    size = len(p)
    columns = [(x, y) for x, y in complement_pairs(n)]
    if n % 2:
        columns.extend(tuple(x for x in range(size) if parity(x) == i) for i in (0, 1))
    support = [set(column) for column in columns]
    table = [
        [Q(x in column) for column in support]
        + [Q(x == y) for y in range(size)]
        + [p[x]]
        for x in range(size)
    ]
    table.append([-Q(len(column)) for column in columns] + [Q(0)] * (size + 1))
    basis = list(range(len(columns), len(columns) + size))

    while True:
        entering = next((j for j, value in enumerate(table[-1][:-1]) if value < 0), None)
        if entering is None:
            return table[-1][-1]
        ratios = [
            (row[-1] / row[entering], basis[i], i)
            for i, row in enumerate(table[:-1])
            if row[entering] > 0
        ]
        _, _, leaving = min(ratios)
        pivot = table[leaving][entering]
        new_row = [value / pivot for value in table[leaving]]
        for i, row in enumerate(table):
            if i != leaving and row[entering]:
                coefficient = row[entering]
                table[i] = [value - coefficient * update for value, update in zip(row, new_row)]
        table[leaving] = new_row
        basis[leaving] = entering


def construct_allocations(p, n, shift):
    favored = int(shift < 0)
    parity_allocation = [
        abs(shift) if parity(x) == favored else Q(0) for x in range(len(p))
    ]
    residual = [value - allocated for value, allocated in zip(p, parity_allocation)]
    cats = [(x, y, min(residual[x], residual[y])) for x, y in complement_pairs(n)]
    assert all(value >= 0 for value in residual)
    return favored, parity_allocation, cats


def check_amplitudes(p, n, probability, shift):
    """Construct the rank-one success effects and correct every nonzero branch."""
    size = len(p)
    mask = size - 1
    favored, allocation, cats = construct_allocations(p, n, shift)

    def root_ratio(numerator, denominator):
        return sqrt(numerator / denominator) if denominator else 0.0

    effects = []
    if shift:
        for outcome in range(size):
            effect = [
                (-1) ** parity(outcome & x) * root_ratio(allocation[x], p[x]) / sqrt(size)
                for x in range(size)
            ]
            effects.append((effect, "parity", outcome, favored))
    for x, y, mass in cats:
        if not mass:
            continue
        for phase in (0, 1):
            effect = [0.0] * size
            effect[x] = root_ratio(mass, p[x]) / sqrt(2)
            effect[y] = (-1) ** phase * root_ratio(mass, p[y]) / sqrt(2)
            effects.append((effect, "cat", x, phase))

    total = 0.0
    for effect, kind, outcome, phase in effects:
        state = [sqrt(p[x]) * effect[x] for x in range(size)]
        mass = sum(value * value for value in state)
        total += mass
        if kind == "parity":
            corrected = [state[x] * (-1) ** parity(x & outcome) for x in range(size)]
            corrected = [
                sum(value * (-1) ** parity(x & y) for x, value in enumerate(corrected))
                / sqrt(size)
                * (-1) ** (phase * (y & 1))
                for y in range(size)
            ]
        else:
            corrected = [
                state[x ^ outcome] * (-1) ** (phase * (x & 1)) for x in range(size)
            ]
        expected_amplitude = sqrt(mass / 2)
        for x, value in enumerate(corrected):
            expected = expected_amplitude if x in (0, mask) else 0.0
            assert isclose(value, expected, rel_tol=1e-12, abs_tol=1e-12)

    for x in range(size):
        for y in range(size):
            entry = sum(effect[x] * effect[y] for effect, *_ in effects)
            if x == y:
                assert -1e-12 <= entry <= 1 + 1e-12
            else:
                assert isclose(entry, 0.0, abs_tol=1e-12)
    assert isclose(total, probability, rel_tol=1e-12, abs_tol=1e-12)


def check_lu_diagonals(rng):
    """Evaluate LU-GHZ amplitudes directly in independent random local bases."""
    count = 0
    for n in range(2, 9):
        for _ in range(12):
            bases = []
            for _ in range(n):
                a = complex(rng.gauss(0, 1), rng.gauss(0, 1))
                b = complex(rng.gauss(0, 1), rng.gauss(0, 1))
                norm = sqrt(abs(a) ** 2 + abs(b) ** 2)
                a, b = a / norm, b / norm
                bases.append(((a, b), (-b.conjugate(), a.conjugate())))
            diagonal = []
            for x in range(1 << n):
                first = prod(basis[0][(x >> k) & 1] for k, basis in enumerate(bases))
                second = prod(basis[1][(x >> k) & 1] for k, basis in enumerate(bases))
                diagonal.append(abs(first + second) ** 2 / 2)
            assert isclose(sum(diagonal), 1.0, abs_tol=1e-12)
            differences = [diagonal[x] - diagonal[y] for x, y in complement_pairs(n)]
            expected = differences[0] if n % 2 else 0.0
            assert all(isclose(value, expected, abs_tol=1e-12) for value in differences)
            count += 1
    return count


def check_ideal_cases(rng):
    counts = dict(product=0, exact_lp=0, explicit_povm=0)
    shift_signs = set()

    def check(p, n, expected=None):
        probability, shift = optimal_probability(p, n)
        _, allocation, cats = construct_allocations(p, n, shift)
        assert sum(allocation) + 2 * sum(mass for _, _, mass in cats) == probability
        assert 0 <= probability <= 1
        for x, y, mass in cats:
            assert 0 <= allocation[x] + mass <= p[x]
            assert 0 <= allocation[y] + mass <= p[y]
        if expected is not None:
            assert probability == expected
        if n <= 5:
            assert packing_probability(p, n) == probability
            counts["exact_lp"] += 1
            check_amplitudes(p, n, probability, shift)
            counts["explicit_povm"] += 1
        shift_signs.add((shift > 0) - (shift < 0))
        return probability

    for n in range(2, 9):
        cases = [[Q(rng.randint(0, 20), 40) for _ in range(n)] for _ in range(12)]
        cases.extend([[Q(0)] + [Q(1, 2)] * (n - 1), [Q(1, 2)] * n, [Q(2, 5)] * n])
        for weights in cases:
            probability = check(product_probabilities(weights), n)
            assert probability <= 2 * min(weights)
            if n == 2:
                assert probability == 2 * min(weights)
            if n == 3:
                a, b, c = weights
                assert probability == 2 * min(a, b, c, a * b + a * c + b * c - a * b * c)
            counts["product"] += 1

    for n in (2, 3, 4, 5):
        size = 1 << n
        for _ in range(4):
            counts_by_string = [rng.randint(0, 12) for _ in range(size)]
            total = sum(counts_by_string)
            p = [Q(count, total) for count in counts_by_string]
            check(p, n)
    for favored in (0, 1):
        check([Q(1, 4) if parity(x) == favored else Q(0) for x in range(8)], 3, Q(1))
    check([Q(1, 2) if x in (0, 15) else Q(0) for x in range(16)], 4, Q(1))
    check([Q(1) if x == 0 else Q(0) for x in range(8)], 3, Q(0))
    assert shift_signs == {-1, 0, 1}
    return counts


def bisect_threshold(probability):
    lower, upper = Q(0), Q(1, 2)
    for _ in range(80):
        mid = (lower + upper) / 2
        if probability(mid) < Q(1, 2):
            lower = mid
        else:
            upper = mid
    return float((lower + upper) / 2)


def check_honeycomb():
    def balanced(q):
        return 6 * q**2 - 4 * q**3

    def parity_adjusted(q):
        return min(2 * q, 6 * q**2 - 2 * q**3)

    for step in range(51):
        q = Q(step, 100)
        p = product_probabilities([q] * 3)
        assert sum(2 * min(p[x], p[y]) for x, y in complement_pairs(3)) == balanced(q)
        assert optimal_probability(p, 3)[0] == parity_adjusted(q)
    assert balanced(Q(2, 5)) == Q(88, 125)
    assert parity_adjusted(Q(2, 5)) == Q(4, 5)
    assert balanced(Q(31, 100)) < Q(1, 2) < parity_adjusted(Q(31, 100))

    threshold = bisect_threshold(parity_adjusted)
    complement_threshold = bisect_threshold(balanced)
    bond_threshold = (1 - 2 * sin(pi / 18)) / 2
    assert isclose(threshold, 0.3045468489842, abs_tol=1e-12)
    assert isclose(complement_threshold, 0.3263518223331, abs_tol=1e-12)
    assert isclose(complement_threshold, bond_threshold, abs_tol=1e-12)
    return threshold, complement_threshold, bond_threshold


def main():
    if not __debug__:
        raise SystemExit("Run without optimization so the assertions execute.")
    rng = Random(20261123)
    counts = check_ideal_cases(rng)
    lu_count = check_lu_diagonals(rng)
    threshold, complement_threshold, bond_threshold = check_honeycomb()
    print(f"Product-link examples with exact arithmetic: {counts['product']}")
    print(f"Independent exact packing LPs: {counts['exact_lp']}")
    print(f"Explicit hub POVMs checked: {counts['explicit_povm']}")
    print(f"Random local-unitary GHZ diagonal checks: {lu_count}")
    print("Homogeneous three-link comparison at q = 0.4: 0.800 vs. 0.704")
    print(f"Honeycomb threshold with parity-adjusted hub POVM: {threshold:.13f}")
    print(f"Honeycomb threshold with complementary concentration: {complement_threshold:.13f}")
    print(f"Honeycomb threshold with independent edge filtering: {bond_threshold:.13f}")
    print("All checks passed.")


if __name__ == "__main__":
    main()
