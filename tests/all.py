#!/usr/bin/env python

if __name__ == "__main__":
    import pytest

    # run tests with code coverage
    pytest.main(["-s", "--tb=native", "--cov=portformer"])
