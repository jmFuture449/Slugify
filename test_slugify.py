from app import slugify


def test_slugify_basic_phrase():
    assert slugify("Hello World") == "hello-world", "Basic phrases should become lowercase, dash-separated slugs."


def test_slugify_multiple_punctuation():
    assert slugify("Hello, world!!! How's it going?") == "hello-world-how-s-it-going", (
        "Punctuation runs should become single dashes."
    )


def test_slugify_removes_emojis():
    assert slugify("Hello 🌍 World") == "hello-world", "Emojis should not appear in the resulting slug."
