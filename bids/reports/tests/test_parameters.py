import pytest

from os.path import join

from bids.layout import BIDSLayout
from bids.reports import parameters
from bids.tests import get_test_data_path


@pytest.fixture
def testlayout():
    """A BIDSLayout for testing."""
    data_dir = join(get_test_data_path(), "synthetic")
    return BIDSLayout(data_dir)


def test_bval_smoke(testlayout):
    """Smoke test for parsing _dwi.bval

    It should return a str description when provided valid inputs.
    """
    bval_file = testlayout.get(
        subject="01",
        session="01",
        suffix="dwi",
        extension=[".bval"],
    )

    bval_str = parameters.describe_bvals(bval_file[0])
    assert isinstance(bval_str, str)


def test_describe_echo_times_smoke(testlayout):
    """Smoke test for parsing echo time

    It should return a str description when provided valid inputs.
    """
    anat_file = testlayout.get(
        subject="01",
        session="01",
        suffix="T1w",
        extension=[".nii.gz"],
    )

    te_str, me_str = parameters.describe_echo_times(anat_file)
    assert isinstance(te_str, str)


def test_describe_double_echo_times_smoke(testlayout):
    """Smoke test for parsing echo time

    It should return a str description when provided valid inputs.
    """
    fmap_file = testlayout.get(
        subject="01",
        session="01",
        suffix="phasediff",
        extension=[".nii.gz"],
    )

    te_str = parameters.describe_echo_times_fmap(fmap_file)
    assert isinstance(te_str, str)
