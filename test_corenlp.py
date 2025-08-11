from nlplogic.corenlp import (
    summarize_wikipedia,
    get_phrases,
    search_wikipedia,
    get_textblob,
)

def test_phrases():
    """
    Test the get_phrases function.
    """
    assert "golden state" in get_phrases("Golden State Warriors")