#!/usr/bin/env python3
"""Check a four-label hub measurement on three q=2/5 links exactly."""

from fractions import Fraction
from itertools import product


DENOMINATOR = 100_000_000
# Numerators of the tangents of half the three local rotation angles.
HALF_ANGLE_TANGENTS = (
    (-88_238_396, 41_421_360, 6_248_252),
    (-1_535_885, 87_340_391, 35_796_831),
    (-47_278_825, 6_757_546, 96_974_691),
    (-8_214_126, 41_421_360, 84_818_743),
)
RELATIVE_SIGNS = (-1, -1, -1, 1)
WEIGHTS = (11_484_959, 11_497_051, 11_497_051, 11_480_325)
BITS = tuple(product(range(2), repeat=3))


def unnormalized_ket(tangents, sign):
    """Return the rational amplitudes of the rotated GHZ ket times sqrt(2)."""
    rotation_columns = []
    for numerator in tangents:
        tangent = Fraction(numerator, DENOMINATOR)
        cosine = (1 - tangent**2) / (1 + tangent**2)
        sine = 2 * tangent / (1 + tangent**2)
        rotation_columns.append(((cosine, sine), (-sine, cosine)))

    amplitudes = []
    for bits in BITS:
        zero_term = one_term = Fraction(1)
        for columns, bit in zip(rotation_columns, bits):
            zero_column, one_column = columns
            zero_term *= zero_column[bit]
            one_term *= one_column[bit]
        amplitudes.append(zero_term + sign * one_term)
    assert sum(amplitude**2 for amplitude in amplitudes) == 2
    return amplitudes


def main():
    q = Fraction(2, 5)
    diagonal = [q**sum(bits) * (1 - q)**(3 - sum(bits)) for bits in BITS]
    kets = [
        unnormalized_ket(tangents, sign)
        for tangents, sign in zip(HALF_ANGLE_TANGENTS, RELATIVE_SIGNS)
    ]
    weights = [Fraction(weight, DENOMINATOR) for weight in WEIGHTS]
    assert all(weight > 0 for weight in weights)
    overlap = [
        [sum(a * b / (2 * p) for a, b, p in zip(left, right, diagonal)) for right in kets]
        for left in kets
    ]

    # The Gram diagonal is weight[i] * overlap[i][i]. Bound each off-diagonal
    # multiplier sqrt(weight[i] * weight[j]) by their arithmetic mean.
    for i, weight in enumerate(weights):
        row_bound = weight * overlap[i][i]
        for j, other in enumerate(weights):
            if j != i:
                row_bound += (weight + other) * abs(overlap[i][j]) / 2
        assert row_bound <= 1 - Fraction(1, DENOMINATOR)

    probability = sum(weights)
    assert probability == Fraction(22_979_693, 50_000_000)
    assert Fraction(1944, 4375) < probability < Fraction(288, 625)
    print(f"Four exact-success effects fit one hub POVM with probability {probability}.")


if __name__ == "__main__":
    main()
