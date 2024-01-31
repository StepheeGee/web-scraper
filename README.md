# LAB - Class 17

## Project: Web-Scraper

## Author: Stephanie G. Johnson

## Date: 01-30-2024

### Overview

Web scraping is a data extraction technique used to gather information from websites automatically. This project focuses on creating a web scraper that automates the process of extracting valuable data from web pages. The key components employed are:

#### 1. BeautifulSoup Library

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library designed for pulling data out of HTML and XML files. In the context of this web scraper, it serves as a powerful tool for parsing HTML content, navigating the parse tree, and searching for specific elements, making it an ideal choice for extracting structured information from websites.

#### 2. Playwright - Headless Browser Automation

[Playwright](https://playwright.dev/docs/api/class-browser) is a headless browser automation library that simplifies web scraping tasks. With its robust set of APIs, Playwright allows easy manipulation of browser actions, enabling automated interactions with web pages. Its headless nature makes it suitable for running in environments without a graphical user interface.

By combining the capabilities of BeautifulSoup and Playwright, this web scraper aims to streamline the process of collecting data from target websites efficiently. Whether extracting text, images, or other relevant information, the scraper automates repetitive tasks, saving time and effort in data retrieval.

### Links and Resources

- [Wikipedia: Common Misconceptions](https://en.wikipedia.org/wiki/List_of_common_misconceptions)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)

**TA's:** Tammy and Brandon

### Virtual Environment Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install requests library: `pip install requests`

### Dependencies

- Beautiful Soup
- Playwright
- Requests

### How to Run

1. Activate the virtual environment (if not already activated).
2. Run `python web-scraper/scraper.py`
