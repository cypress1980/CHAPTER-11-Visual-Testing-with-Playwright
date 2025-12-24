from playwright.sync_api import sync_playwright
def test_visual_element_level_with_mask(assert_snapshot):
    """Test specific element with masking of dynamic parts"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Screenshot specific section, masking dynamic content within it
        product_section = page.locator(".container-fluid").nth(2)
        
        assert_snapshot(
            product_section.screenshot(mask=[
                page.locator(".product-price"),  # Mask all prices in section
            ]),
            name="products-section-masked.png",
            threshold=0.1
        )
        
        browser.close()