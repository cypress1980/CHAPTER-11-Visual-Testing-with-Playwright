from playwright.sync_api import sync_playwright,expect
def test_diff1_version(assert_snapshot):
    """Test with ?diff1 parameter to detect visual differences"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://applitools.com/helloworld/?diff1")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)
        assert_snapshot(
            page.screenshot(full_page=True),
            name="helloworld-full-page-diff.png",
            threshold=0.0
        )
        browser.close()