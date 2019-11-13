import os
import numpy as np
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['notebooks']
)

IGNORE = ["3_DC_Kaufman_finite_well", "5_FDEM_following_Augustin_Fig3"]

n_ignore = 3  # so we don't run over-time on travis, randomly ignore 3 notebooks
Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800)
ignore_inds = np.random.choice(len(Test._nbnames) - len(IGNORE), n_ignore)
test_nbnames = [t for t in Test._nbnames if t not in IGNORE]
Test.ignore = IGNORE + [test_nbnames[i] for i in ignore_inds]
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
