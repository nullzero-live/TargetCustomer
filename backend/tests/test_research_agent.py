import json

import pytest

from backend.agents.user_input import collect_user_input


def test_collect_user_input(monkeypatch):
    # Mock user inputs for the function
    monkeypatch.setattr('builtins.input', lambda _: "Technology")
    monkeypatch.setattr('builtins.input', lambda _: "Software")
    monkeypatch.setattr('builtins.input', lambda _: "3")

    # Call the function and get the result
    result = collect_user_input()

    # Prepare the expected result
    expected_result = {
        "Industry": "Technology",
        "Business": "Software",
        "Depth": "3"
    }

    assert result == expected_result
