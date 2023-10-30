import pytest
from agents.compose_strategy import compose_strategy


def test_compose_strategy():
    # Mock input
    res_output = {
        "Industry": "Tech",
        "Business": "Software",
        "Summary": "Potential for growth."
    }

    # Expected output
    expected_output = "Focus on scaling your Software in the Tech sector."

    assert compose_strategy(res_output) == expected_output
