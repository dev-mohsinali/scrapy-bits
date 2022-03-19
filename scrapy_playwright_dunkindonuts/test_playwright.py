from playwright.sync_api import sync_playwright
import sys

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://google.com.pk')
        page.wait_for_timeout(1000)
        browser.close()

if __name__ == '__main__':
    main()