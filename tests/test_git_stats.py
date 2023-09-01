import os

from git_stats import A


def test_stack_created():
    assert os.getcwd()
    assert A()
