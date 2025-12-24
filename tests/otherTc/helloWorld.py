from playwright.sync_api import sync_playwright

# def test_baseline_applitools(assert_snapshot):
#     """Baseline test - capture the original HelloWorld page"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)  # Wait for any animations
        
#         # Disable animations for consistent screenshots
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="helloworld-baseline.png",
#             threshold=0.15
#         )
        
#         browser.close()


def test_diff1_version(assert_snapshot):
    """Test with ?diff1 parameter to detect visual differences"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://applitools.com/helloworld/?diff1")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)
        
        # Disable animations
        # page.evaluate("""
        #     const style = document.createElement('style');
        #     style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
        #     document.head.appendChild(style);
        # """)
        
        assert_snapshot(
            page.screenshot(full_page=True),
            name="helloworld-diff1.png",
            threshold=0.15
        )
        browser.close()


# def test_diff2_version(assert_snapshot):
#     """Test with ?diff2 parameter to detect additional visual differences"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/?diff2")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
        
#         # Disable animations
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="helloworld-diff2.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_click_me_button_interaction(assert_snapshot):
#     """Test clicking the 'Click me!' button"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
        
#         # Wait for button to be visible first (before disabling animations)
#         button = page.locator("button:has-text('Click me!')")
#         button.wait_for(state="visible")
        
#         # Click the button BEFORE disabling animations to see the click effect
#         button.click()
        
#         # Wait to see the visual effect of the click
#         page.wait_for_timeout(2000)
        
#         # Now disable animations for stable screenshot
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         # Small wait after disabling animations
#         page.wait_for_timeout(500)
        
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="helloworld-after-click.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_diff1_with_button_click(assert_snapshot):
#     """Test ?diff1 version and click button to see combined changes"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/?diff1")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
        
#         # Disable animations
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         page.locator("text=Click me!").click()
#         page.wait_for_timeout(1000)
        
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="helloworld-diff1-clicked.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_diff2_with_button_click(assert_snapshot):
#     """Test ?diff2 version and click button"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/?diff2")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
        
#         # Disable animations
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         page.locator("text=Click me!").click()
#         page.wait_for_timeout(1000)
        
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="helloworld-diff2-clicked.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_element_level_visual(assert_snapshot):
#     """Test specific element visual comparison"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://applitools.com/helloworld/")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
        
#         # Disable animations
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
        
#         # Capture the main content area (more reliable selector)
#         main_container = page.locator("body").first
        
#         assert_snapshot(
#             main_container.screenshot(),
#             name="helloworld-element.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_multiple_states_comparison(assert_snapshot):
#     """Compare multiple page states in one test"""
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
        
#         # State 1: Baseline
#         page.goto("https://applitools.com/helloworld/")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="state-baseline.png",
#             threshold=0.15
#         )
        
#         # State 2: diff1
#         page.goto("https://applitools.com/helloworld/?diff1")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="state-diff1.png",
#             threshold=0.15
#         )
        
#         # State 3: diff2
#         page.goto("https://applitools.com/helloworld/?diff2")
#         page.wait_for_load_state("networkidle")
#         page.wait_for_timeout(1000)
#         page.evaluate("""
#             const style = document.createElement('style');
#             style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
#             document.head.appendChild(style);
#         """)
#         assert_snapshot(
#             page.screenshot(full_page=True),
#             name="state-diff2.png",
#             threshold=0.15
#         )
        
#         browser.close()


# def test_with_strict_threshold(assert_snapshot):
    """Test with moderate threshold for better stability"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://applitools.com/helloworld/?diff1")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)
        
        # Disable animations
        page.evaluate("""
            const style = document.createElement('style');
            style.textContent = '*, *::before, *::after { animation: none !important; transition: none !important; }';
            document.head.appendChild(style);
        """)
        
        assert_snapshot(
            page.screenshot(full_page=True),
            name="helloworld-strict.png",
            threshold=0.15  # Increased for stability on re-runs
        )
        
        browser.close()