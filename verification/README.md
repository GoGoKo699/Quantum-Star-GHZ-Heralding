# Verification

Run from the repository root with Python 3.10 or later. The script uses the standard library.

```sh
python3 verification/check.py
```

The checks use a fixed random seed and cover four parts of the calculation.

| Check | What the script verifies |
| --- | --- |
| Closed form | Exact rational arithmetic on 105 product-link examples with two to eight leaves, including product edges, Bell edges and heterogeneous links. Each example obeys the weakest-link cut bound. The two- and three-link cases also match their separate closed forms. |
| Packing and construction | An exact rational simplex solver maximizes the total occupied diagonal weight over the complementary and, for odd stars, parity generators. It agrees with the formula on 80 examples with up to five leaves, including nonproduct input diagonals. For each example, the script builds explicit hub measurement effects, checks that they can be completed to a POVM and checks every successful leaf state after correction. |
| Local-unitary diagonals | Direct complex-amplitude evaluation in 84 randomly chosen local basis configurations checks complement symmetry for even stars and constant even-to-odd excess for odd stars. |
| Honeycomb thresholds | An exact rational grid check verifies both homogeneous three-link probability polynomials. Bisection against triangular site occupation probability $1/2$ gives $q=0.3045468489842$ with the parity-adjusted hub instrument and $q=0.3263518223331$ with complementary concentration. The latter also equals the link-weight threshold obtained by filtering links independently and applying the honeycomb bond threshold. |

The rational simplex check uses the generators directly and does not use the median formula. The numerical amplitude checks use an absolute tolerance of $10^{-12}$. The verification concerns the ideal finite-star model and the resulting analytic percolation thresholds.
