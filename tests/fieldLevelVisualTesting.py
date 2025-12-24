from playwright.sync_api import sync_playwright,expect

def test_page_level(assert_snapshot):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Set fixed viewport size for consistent screenshots
        page.set_viewport_size({"width": 1280, "height": 720})
        page.goto("https://shop.qaautomationlabs.com/")
        
        # Use .first to select the first matching element
        login_page_continer = page.locator('.contact-form.bg-light').first
        expect(login_page_continer).to_be_visible()
        
        # Compare only a specific region of the page
        assert_snapshot(login_page_continer.screenshot(),name="contact-form.png",threshold=0.1)
        
        browser.close()