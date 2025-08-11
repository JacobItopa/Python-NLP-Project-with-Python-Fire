import wikipedia
from textblob import TextBlob

def search_wikipedia(name):
    """
    Search for a name on Wikipedia.
    
    :param name: The name to search for.
    :return: Wikipedia search.
    """
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """
    Summarize the Wikipedia page for a given name.
    
    :param name: The name to summarize.
    :return: Summary of the Wikipedia page.
    """
    try:
        page = wikipedia.page(name)
        return page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."
    except Exception as e:
        return str(e)

def get_textblob(text):
    """
    Get TextBlob object for the given text.
    
    :param text: The text to analyze.
    :return: TextBlob object.
    """
    return TextBlob(text)

def get_phrases(text):
    """
    Get noun phrases from the text.
    
    :param text: The text to analyze.
    :return: List of noun phrases.
    """
    summary = summarize_wikipedia(text)
    blob = get_textblob(summary)
    return blob.noun_phrases