import pytest
from web_scraper import __version__
from scraper import get_citations_needed_report, get_citations_needed_count


def test_version():
    assert __version__ == '0.1.0'

def test_count_beer():
    URL = 'https://en.wikipedia.org/wiki/Beer'
    actual = get_citations_needed_count(URL)
    expected = 'Citation needed for 0'
    assert actual == expected

def test_count_lemmy_count():
    URL = 'https://en.wikipedia.org/wiki/Lemmy'
    actual = get_citations_needed_count(URL)
    expected = 'Citation needed for 1'
    assert actual == expected

def test_count_lemmy_report():
    URL = 'https://en.wikipedia.org/wiki/Lemmy'
    actual = get_citations_needed_report(URL)[0]
    expected = 'For the majority of his career, he used Rickenbacker basses.[83] In September 1996, his Rickenbacker bass was featured in the Bang Your Head exhibition at the Rock and Roll Hall of Fame in Cleveland, Ohio, US.[84] Rickenbacker has introduced a signature 4004LK "Lemmy Kilmister" bass.[citation needed]'
    assert actual == expected