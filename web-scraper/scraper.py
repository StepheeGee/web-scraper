# scraper.py
from page_parser import get_citations_needed_count, get_citations_needed_report

def main():
    url = 'https://en.wikipedia.org/wiki/Social_intelligence'

    count = get_citations_needed_count(url)
    report = get_citations_needed_report(url)

    print(f"Number of citations needed: {count}")
    print("Citations report:\n", report)

if __name__ == "__main__":
    main()
