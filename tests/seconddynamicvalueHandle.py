from playwright.sync_api import sync_playwright
def test_visual_hide_dynamic_text(assert_snapshot):
    """Hide elements with dynamic text (timestamps, user names, etc.)"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://applitools.com/helloworld/?diff1")
        
        # Hide the dynamic number element before taking the screenshot
        assert_snapshot(
            page.screenshot(mask=[page.locator('.diff1.diff2.random-number'),  # Mask the dynamic number
            ]),
            name="homepage-no-year.png",
            threshold=0.6
        )
        browser.close()