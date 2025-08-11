from nlplogic.corenlp import get_phrases
    

def test_phrases():
    """
    Test the get_phrases function.
    """
    assert "golden state" in get_phrases("Golden State Warriors")