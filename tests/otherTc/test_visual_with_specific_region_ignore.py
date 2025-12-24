from playwright.sync_api import sync_playwright
def test_visual_with_specific_region_ignore(assert_snapshot):
    """Ignore specific regions of the page (useful for ads, carousels, etc.)"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Take screenshot and mask carousel/slider (dynamic content)
        assert_snapshot(
            page.screenshot(full_page=True, mask=[
                page.locator("#header-carousel"),  # Mask carousel
            ]),
            name="homepage-no-carousel.png",
            threshold=0.1
        )
        
        browser.close()