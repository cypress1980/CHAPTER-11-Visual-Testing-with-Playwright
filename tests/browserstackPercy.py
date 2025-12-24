from playwright.sync_api import sync_playwright
from percy import percy_snapshot

def test_homepage_visual():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.browserstack.com/")
        percy_snapshot(page, "Homepage Snapshot")

        browser.close()
