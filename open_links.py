import webbrowser
import sys, os

def open_links(urls, browser):
    if browser != "safari":
        browser = f"open -a {browser} %s"
        webbrowser.register('browser', None, webbrowser.BackgroundBrowser(browser))
    for url in urls:
        webbrowser.get(browser).open(url)

urls = sys.argv[1:]
browser = os.environ["browser"]

open_links(urls, browser)