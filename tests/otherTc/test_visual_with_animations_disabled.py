from playwright.sync_api import sync_playwright
def test_visual_with_animations_disabled(assert_snapshot):
    """Disable animations to get consistent screenshots"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Disable animations for consistent visual testing
        page.goto("https://shop.qaautomationlabs.com/index.php")
        page.evaluate("""
            const style = document.createElement('style');
            style.textContent = `
                *, *::before, *::after {
                    animation-duration: 0s !important;
                    transition-duration: 0s !important;
                }
            `;
            document.head.appendChild(style);
        """)
        
        page.wait_for_timeout(500)  # Wait for page to stabilize
        
        assert_snapshot(
            page.screenshot(full_page=True),
            name="homepage-no-animations.png",
            threshold=0.05  # Lower threshold since no animations
        )
        
        browser.close()