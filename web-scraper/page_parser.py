# page_parser.py
import requests
from bs4 import BeautifulSoup

def parse(markup):
    soup = BeautifulSoup(markup, 'html.parser')
    return soup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = parse(response.text)

    # Find all parent elements (often paragraphs) containing the citation needed
    citations = soup.findAll('a')

    # Count only the citations that are not within a reference tag
    count = 0
    for link in citations:
        if 'citation needed' in link.text:       
            count += 1
    return count

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = parse(response.text)

    # Find all parent elements (often paragraphs) containing the citation needed
    citations = soup.findAll(lambda tag: tag.name == 'p' and '[citation needed]' in tag.text)

    # Generate a report string with relevant passages
    report = ""
    for citation in citations:
        report += f"{citation}\n[citation needed]\n\n"

    return report
