import pytest

from app import kebab_to_title_case


@pytest.mark.parametrize(
    ("kebab_text", "expected"),
    [
        ("hello-world", "Hello World"),
        ("python-is-awesome", "Python Is Awesome"),
        ("single", "Single"),
        ("mixed-CASE-text", "Mixed Case Text"),
        ("", ""),
        ("hello--world", "Hello World"),
        ("--hello-world--", "Hello World"),
    ],
)
def test_kebab_to_title_case(kebab_text: str, expected: str) -> None:
    assert kebab_to_title_case(kebab_text) == expected
