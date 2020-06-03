import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Lemmy'

def get_citations_needed_count(URL):
    response = requests.get(URL)
    # print(dir(response))

    # extract content
    content = response.content
    # print(dir(content))

    soup = BeautifulSoup(content, 'html.parser')
    # print(dir(soup))

    # results = soup.find(id="mw-content-text")
    # print(results.prettify())

    citation_list = soup.findAll('sup', class_="noprint Inline-Template Template-Fact")
    # print(citation_list[0])



    return(f'Citation needed for {len(citation_list)}')


print(get_citations_needed_count(URL))

## citation element
# <sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">[<i><a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"><span title="This claim needs references to reliable sources. (March 2020)">citation needed</span></a></i>]</sup>



def get_citations_needed_report(URL):
    final_results = []
    response = requests.get(URL)
    # print(dir(response))



    # extract content
    content = response.content
    # print(dir(content))

    soup = BeautifulSoup(content, 'html.parser')
    # print(dir(soup))

    # results = soup.find(id="mw-content-text")
    # print(results.prettify())

    citation_list = soup.findAll('sup', class_="noprint Inline-Template Template-Fact")
    # print(citation_list[0])
    for cit in citation_list:
        # print(cit.parent)
        print(f'Relevant passage: {cit.parent.text.strip()}\n')
        final_results.append(cit.parent.text.strip())

    return final_results


get_citations_needed_report(URL)

print(get_citations_needed_report)
