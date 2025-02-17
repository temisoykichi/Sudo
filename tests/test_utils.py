# test_utils.py

import pytest
from sdk.utils import validate_email, convert_to_json, format_date


def test_validate_email_valid():
    """
    Test that the validate_email function returns True for valid emails.
    """
    valid_email = "test@example.com"
    result = validate_email(valid_email)

    # Assert that the result is True for a valid email
    assert result is True


def test_validate_email_invalid():
    """
    Test that the validate_email function returns False for invalid emails.
    """
    invalid_email = "invalid-email"
    result = validate_email(invalid_email)

    # Assert that the result is False for an invalid email
    assert result is False


def test_convert_to_json_valid():
    """
    Test that the convert_to_json function correctly converts a dictionary to JSON.
    """
    sample_dict = {"name": "John", "age": 30}
    result = convert_to_json(sample_dict)

    # Assert that the result is the expected JSON string
    expected_json = '{"name": "John", "age": 30}'
    assert result == expected_json


def test_convert_to_json_invalid():
    """
    Test that the convert_to_json function raises a TypeError for non-serializable objects.
    """
    sample_object = object()  # An object that can't be serialized to JSON
    with pytest.raises(TypeError):
        convert_to_json(sample_object)


def test_format_date_valid():
    """
    Test that the format_date function correctly formats a valid date.
    """
    valid_date = "2025-02-16"
    result = format_date(valid_date)

    # Assert that the formatted date matches the expected output
    expected_date = "16-Feb-2025"
    assert result == expected_date


def test_format_date_invalid():
    """
    Test that the format_date function returns an error for an invalid date.
    """
    invalid_date = "16-02-2025"  # Invalid format, expecting 'YYYY-MM-DD'
    result = format_date(invalid_date)

    # Assert that the result is None (or some other error handling value)
    assert result is None


def test_format_date_edge_case():
    """
    Test that the format_date function handles edge cases like leap years correctly.
    """
    leap_year_date = "2024-02-29"  # A valid leap year date
    result = format_date(leap_year_date)

    # Assert that the result is correctly formatted
    expected_date = "29-Feb-2024"
    assert result == expected_date


def test_format_date_non_date_input():
    """
    Test that the format_date function returns None or raises an error for non-date inputs.
    """
    non_date_input = "not-a-date"
    result = format_date(non_date_input)

    # Assert that the result is None or an error is raised
    assert result is None
