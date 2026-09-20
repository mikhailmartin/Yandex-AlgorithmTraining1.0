import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pytest
from pytest import param
from HomeWork8.J_genealogy_counting_levels import Solver


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        param(
            [
                "9",
                "Alexei Peter_I",
                "Anna Peter_I",
                "Elizabeth Peter_I",
                "Peter_II Alexei",
                "Peter_III Anna",
                "Paul_I Peter_III",
                "Alexander_I Paul_I",
                "Nicholaus_I Paul_I",
            ],
            [
                ("Alexander_I", 4),
                ("Alexei", 1),
                ("Anna", 1),
                ("Elizabeth", 1),
                ("Nicholaus_I", 4),
                ("Paul_I", 3),
                ("Peter_I", 0),
                ("Peter_II", 2),
                ("Peter_III", 2),
            ],
            id="example1",
        ),
        param(
            [
                "10",
                "AQHFYP MKFXCLZBT",
                "AYKOTYQ QIUKGHWCDC",
                "IWCGKHMFM WPLHJL",
                "MJVAURUDN QIUKGHWCDC",
                "MKFXCLZBT IWCGKHMFM",
                "PUTRIPYHNQ UQNGAXNP",
                "QIUKGHWCDC WPLHJL",
                "UQNGAXNP WPLHJL",
                "YURTPJNR QIUKGHWCDC",
            ],
            [
                ("AQHFYP", 3),
                ("AYKOTYQ", 2),
                ("IWCGKHMFM", 1),
                ("MJVAURUDN", 2),
                ("MKFXCLZBT", 2),
                ("PUTRIPYHNQ", 2),
                ("QIUKGHWCDC", 1),
                ("UQNGAXNP", 1),
                ("WPLHJL", 0),
                ("YURTPJNR", 2),
            ],
            id="example2",
        ),
        param(
            [
                "10",
                "BFNRMLH CSZMPFXBZ",
                "CSZMPFXBZ IHWBQDJ",
                "FMVQTU FUXATQUGIG",
                "FUXATQUGIG IRVAVMQKN",
                "GNVIZ IQGIGUJZ",
                "IHWBQDJ LACXYFQHSQ",
                "IQGIGUJZ JMUPNYRQD",
                "IRVAVMQKN GNVIZ",
                "JMUPNYRQD BFNRMLH",
            ],
            [
                ("BFNRMLH", 3),
                ("CSZMPFXBZ", 2),
                ("FMVQTU", 9),
                ("FUXATQUGIG", 8),
                ("GNVIZ", 6),
                ("IHWBQDJ", 1),
                ("IQGIGUJZ", 5),
                ("IRVAVMQKN", 7),
                ("JMUPNYRQD", 4),
                ("LACXYFQHSQ", 0),
            ],
            id="example3",
        ),
    ],
)
def test_solve(lines, expected):
    solver = Solver.from_strings(lines)
    assert solver.solve() == expected
