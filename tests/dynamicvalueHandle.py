from playwright.sync_api import sync_playwright, expect

def test_diff1_version(assert_snapshot):
    """Test with ?diff1 parameter - hiding dynamic random number"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://applitools.com/helloworld/?diff2")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
        
        # Hide the dynamic number element using CSS
        page.evaluate("""
            const dynamicElement = document.querySelector('.diff1.diff2.random-number');
            if (dynamicElement) {
                dynamicElement.style.visibility = 'hidden';
            }
        """)
        
        page.wait_for_timeout(500)

        assert_snapshot(
            page.screenshot(full_page=True),
            name="helloworld-diff1.png",
            threshold=0.2
        )
        browser.close()