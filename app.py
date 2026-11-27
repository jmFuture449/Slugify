import re

def slugify(text: str) -> str:
    """
    Convert *text* into a lowercase dash-separated slug.
    Keeps alphanumerics, converts spaces & punctuation to '-',
    collapses consecutive dashes.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")

def kebab_to_title_case(text: str) -> str:
    """
    Convert *text* from kebab-case to Title Case.
    """
    return " ".join(word.capitalize() for word in text.split("-"))
