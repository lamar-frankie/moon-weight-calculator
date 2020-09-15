#!/usr/bin/env python3
"""tests for moon weight calc"""

import os
from subprocess import getstatusoutput, getoutput

script = './test_moon_weight_clac.py'

#----------------------------------------------------------------------
def test_exists():
    """script exists"""

    assert os.path.isfile(script)

#----------------------------------------------------------------------
def test_runnable():
    """Runs using python3"""

    output = getoutput(f'python3 {script} 100')
    assert output.lower().startswith('moon fact:')