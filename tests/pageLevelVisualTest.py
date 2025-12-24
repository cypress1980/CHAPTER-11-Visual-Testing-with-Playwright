from playwright.sync_api import sync_playwright

def test_page_level(assert_snapshot):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        assert_snapshot(
            page.screenshot(full_page=True),
            name="homepage-full.png",  # Custom name (optional)
            threshold=0.1)  # Pixel difference tolerance (0-1)
        
        browser.close()