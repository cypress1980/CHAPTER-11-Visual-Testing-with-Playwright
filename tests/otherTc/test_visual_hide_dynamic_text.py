from playwright.sync_api import sync_playwright
def test_visual_hide_dynamic_text(assert_snapshot):
    """Hide elements with dynamic text (timestamps, user names, etc.)"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Hide copyright year and other dynamic text
        assert_snapshot(
            page.screenshot(full_page=True, mask=[
                page.locator("text=/© 202[0-9]/"),  # Mask copyright year
            ]),
            name="homepage-no-year.png",
            threshold=0.1
        )
        
        browser.close()