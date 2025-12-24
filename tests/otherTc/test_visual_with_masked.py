from playwright.sync_api import sync_playwright
def test_visual_with_masked_dynamic_elements(assert_snapshot):
    """Mask dynamic elements like ads, timestamps, or user-specific content"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Mask dynamic elements to exclude from comparison
        assert_snapshot(
            page.screenshot(full_page=True, mask=[
                page.locator(".price"),  # Mask prices (can change)
                page.locator(".badge"),  # Mask badges/notifications
            ]),
            name="homepage-masked.png",
            threshold=0.1
        )
        
        browser.close()