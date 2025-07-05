import asyncio
from playwright.async_api import async_playwright, TimeoutError

# ===================================================================
# CONFIGURABLE TEST DATA VARIABLES
# ===================================================================
# You can modify these values directly here, or use option 5 in the menu
# to update them at runtime without modifying the code.
# ===================================================================

# Standard test data used for the regular automation run
TEST_USER_NAME = "Playwright Tester One"
TEST_USER_EMAIL = "playwright-tester-1@gptviewer.com"
TEST_USER_PHONE = "1234334321"
TEST_USER_COUNTRY = "India"

# Custom test data for the custom selector mode (option 3)
CUSTOM_USER_NAME = "Playwright Tester-1"
CUSTOM_USER_EMAIL = "playwright-tester-1@gptviewer.com"
CUSTOM_USER_PHONE = "12345764321"
CUSTOM_USER_COUNTRY = "India"
# ===================================================================

async def run_registration_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set True to run headless
        page = await browser.new_page()
        
        # Enable more verbose logging
        page.on("console", lambda msg: print(f"Browser console: {msg.text}"))

        try:
            # 1. Navigate to the website
            print("Navigating to the website...")
            await page.goto("https://gptchatviewer.com/", wait_until="networkidle")
            
            # Take screenshot to see what we're working with
            await page.screenshot(path="initial_page.png")
            print("Screenshot saved as initial_page.png")

            # 2. Click "Get Started" with more robust selectors and debugging
            print("Attempting to click 'Get Started' button...")
            
            # Try multiple selector strategies
            try:
                # Option 1: By role and name
                await page.get_by_role("button", name="Get Started").click(timeout=5000)
                print("Found 'Get Started' by role and name")
            except TimeoutError:
                try:
                    # Option 2: By text
                    await page.get_by_text("Get Started", exact=True).click(timeout=5000)
                    print("Found 'Get Started' by exact text")
                except TimeoutError:
                    try:
                        # Option 3: By text containing
                        await page.get_by_text("Get Started", exact=False).click(timeout=5000)
                        print("Found 'Get Started' by partial text")
                    except TimeoutError:
                        # Option 4: By CSS selector (more generic)
                        print("Trying CSS selectors for 'Get Started'...")
                        # Take screenshot to analyze page structure
                        await page.screenshot(path="before_get_started.png")
                        
                        # List all buttons on page to help identify the correct one
                        buttons = await page.query_selector_all("button")
                        print(f"Found {len(buttons)} buttons on page")
                        for i, button in enumerate(buttons):
                            text = await button.text_content()
                            print(f"Button {i}: '{text}'")
                            if "start" in text.lower():
                                print(f"Clicking button {i}")
                                await button.click()
                                break
                        else:
                            # Try a more general selector if specific buttons failed
                            await page.click("text=start", timeout=5000)

            # Take screenshot after clicking to see where we are
            await asyncio.sleep(2)  # Give page time to load
            await page.screenshot(path="after_get_started.png")
            print("Screenshot saved as after_get_started.png")

            # 3. Fill registration details with improved selectors based on element inspection
            print("Filling registration form using type-based selectors...")
            
            # Since elements have no IDs, names, or labels, we'll use element type and order
            try:
                # Fill name (first text input)
                print(f"Filling Full Name field with '{TEST_USER_NAME}'...")
                await page.fill("input[type='text']", TEST_USER_NAME)
                print("✓ Successfully filled Full Name field")
                
                # For dropdown selection
                print(f"Trying to select Country: '{TEST_USER_COUNTRY}'...")
                selects = await page.query_selector_all("select")
                if selects:
                    print(f"Found {len(selects)} select elements, using the first one")
                    try:
                        await selects[0].select_option(label=TEST_USER_COUNTRY)
                        print("✓ Successfully selected country")
                    except Exception as e:
                        print(f"Country selection error: {e}")
                        # Try selecting by index as fallback
                        try:
                            await selects[0].select_option(index=1)  # Select second option as fallback
                            print("✓ Selected country by index")
                        except Exception as e2:
                            print(f"Country selection by index error: {e2}")
                else:
                    print("⚠️ No select elements found for country")
                
                # Fill email (by type)
                print(f"Filling Email field with '{TEST_USER_EMAIL}'...")
                await page.fill("input[type='email']", TEST_USER_EMAIL)
                print("✓ Successfully filled Email field")
                
                # Fill contact number (by type=tel)
                print(f"Filling Contact field with '{TEST_USER_PHONE}'...")
                await page.fill("input[type='tel']", TEST_USER_PHONE)
                print("✓ Successfully filled Contact field")
                
                print("Form filling completed with type-based selectors")
            except Exception as e:
                print(f"Form filling error: {e}")
                await page.screenshot(path="form_filling_error.png")

            # Take screenshot of filled form
            await page.screenshot(path="filled_form.png")
            print("Screenshot saved as filled_form.png")

            # 4. Click register/submit with simpler approach based on inspection
            print("Attempting to click submit button...")
            try:
                # Since element inspection showed no specific identifiers, let's try simpler approaches
                
                # First take screenshot before submitting
                await page.screenshot(path="before_submit.png")
                print("Screenshot saved as before_submit.png")
                
                # Try to find any button (since there should only be one submit button)
                buttons = await page.query_selector_all("button")
                if buttons:
                    # Try to find a button that looks like a submit button by text
                    for button in buttons:
                        text = await button.text_content()
                        print(f"Found button with text: '{text}'")
                        
                        # Check if button text contains typical submit keywords
                        if any(word.lower() in text.lower() for word in ["register", "submit", "sign", "continue", "next"]):
                            print(f"Clicking button with text: '{text}'")
                            await button.click()
                            print(f"✓ Clicked button with text: '{text}'")
                            break
                    else:
                        # If no matching button found by text, click the first button
                        print("No button with typical submit text found, clicking first button")
                        await buttons[0].click()
                        print("✓ Clicked first button found")
                else:
                    # As last resort, try to find anything clickable that might be a submit button
                    print("No buttons found, trying alternative approaches")
                    
                    try:
                        # Try any element that looks like it could be a submit button
                        for selector in ["input[type='submit']", ".submit", ".btn", "[role='button']"]:
                            try:
                                elements = await page.query_selector_all(selector)
                                if elements:
                                    await elements[0].click()
                                    print(f"✓ Clicked element using selector: {selector}")
                                    break
                            except:
                                pass
                    except Exception as e:
                        print(f"Error trying alternative submit elements: {e}")
                        await page.screenshot(path="submit_alternatives_error.png")
                        
            except Exception as e:
                print(f"Register button error: {e}")
                await page.screenshot(path="register_button_error.png")

            # 5. Wait for confirmation or next page
            print("Waiting for confirmation or next page...")
            await page.screenshot(path="after_submit.png")
            print("Screenshot saved as after_submit.png")

            # Keep browser open for manual check
            print("Keeping browser open for 10 seconds for manual verification...")
            await asyncio.sleep(10)
            
        except Exception as e:
            print(f"Test failed: {e}")
            # Take screenshot on failure
            await page.screenshot(path="error_screenshot.png")
            print("Error screenshot saved as error_screenshot.png")
        
        finally:
            await browser.close()

async def inspect_page_elements():
    """Helper function to identify form elements on the page"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to the website
        await page.goto("https://gptchatviewer.com/", wait_until="networkidle")
        
        # Click Get Started (if needed) - try a general selector
        try:
            await page.click("text=Get Started", timeout=5000)
        except:
            print("Could not find 'Get Started' button, assuming we're on the form page")
        
        # Wait to ensure page is loaded
        await asyncio.sleep(2)
        
        # Take screenshot
        await page.screenshot(path="form_page.png")
        print("Screenshot saved as form_page.png")
        
        # Analyze form elements
        print("\n===== PAGE ANALYSIS =====")
        
        # Find all input elements
        inputs = await page.query_selector_all("input")
        print(f"Found {len(inputs)} input elements")
        
        for i, input_el in enumerate(inputs):
            try:
                input_type = await input_el.get_attribute("type") or "text"
                input_id = await input_el.get_attribute("id") or "no-id"
                input_name = await input_el.get_attribute("name") or "no-name"
                input_placeholder = await input_el.get_attribute("placeholder") or "no-placeholder"
                input_label = await input_el.get_attribute("aria-label") or "no-label"
                
                print(f"Input {i+1}: Type={input_type}, ID={input_id}, Name={input_name}")
                print(f"         Placeholder={input_placeholder}, Label={input_label}")
            except:
                print(f"Input {i+1}: Could not get attributes")
        
        # Find all select elements
        selects = await page.query_selector_all("select")
        print(f"\nFound {len(selects)} select elements")
        
        for i, select in enumerate(selects):
            try:
                select_id = await select.get_attribute("id") or "no-id"
                select_name = await select.get_attribute("name") or "no-name"
                print(f"Select {i+1}: ID={select_id}, Name={select_name}")
                
                # Get options
                options = await select.query_selector_all("option")
                print(f"  Has {len(options)} options")
                for j, option in enumerate(options[:5]):  # Show first 5 options
                    option_text = await option.text_content()
                    option_value = await option.get_attribute("value")
                    print(f"  Option {j+1}: Text={option_text}, Value={option_value}")
                if len(options) > 5:
                    print(f"  ... and {len(options) - 5} more options")
            except:
                print(f"Select {i+1}: Could not get attributes")
        
        # Find all buttons
        buttons = await page.query_selector_all("button")
        print(f"\nFound {len(buttons)} buttons")
        
        for i, button in enumerate(buttons):
            try:
                button_text = await button.text_content()
                button_type = await button.get_attribute("type") or "no-type"
                button_id = await button.get_attribute("id") or "no-id"
                print(f"Button {i+1}: Text='{button_text}', Type={button_type}, ID={button_id}")
            except:
                print(f"Button {i+1}: Could not get attributes")
        
        print("\n===== END PAGE ANALYSIS =====")
        
        print("\nKeeping browser open for 30 seconds to manually inspect elements...")
        await asyncio.sleep(30)
        await browser.close()

async def run_with_custom_selectors(selectors=None):
    """Run the test with custom selectors provided after analysis"""
    if not selectors:
        selectors = {}
        
    # Default selectors updated based on element inspection results
    default_selectors = {
        "full_name": "input[type='text']",  # First text input element
        "country": "select",                # General select element
        "email": "input[type='email']",     # Email input by type
        "contact": "input[type='tel'], input[placeholder*='123']",  # Tel input or by placeholder
        "submit": "button"                  # Any button (assuming it's for submission)
    }
    
    # Merge provided selectors with defaults
    for key, value in default_selectors.items():
        if key not in selectors:
            selectors[key] = value
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            # Navigate to the website
            await page.goto("https://gptchatviewer.com/", wait_until="networkidle")
            
            # Click Get Started
            try:
                # Try multiple options
                for selector in ["button:has-text('Get Started')", "a:has-text('Get Started')", 
                                 ".btn:has-text('Get Started')", "text=Get Started"]:
                    try:
                        await page.click(selector, timeout=2000)
                        print(f"Clicked Get Started using selector: {selector}")
                        break
                    except:
                        pass
            except:
                print("Could not find Get Started button, assuming we're already on the form")
            
            # Wait for form to load
            await asyncio.sleep(2)
            
            # Fill form using custom selectors
            print("Filling form with custom selectors...")
            
            # Full Name
            try:
                await page.fill(selectors["full_name"], CUSTOM_USER_NAME)
                print(f"✓ Filled Full Name '{CUSTOM_USER_NAME}' using {selectors['full_name']}")
            except Exception as e:
                print(f"✗ Could not fill Full Name: {e}")
            
            # Country
            try:
                await page.select_option(selectors["country"], label=CUSTOM_USER_COUNTRY)
                print(f"✓ Selected Country '{CUSTOM_USER_COUNTRY}' using {selectors['country']}")
            except Exception as e:
                print(f"✗ Could not select Country: {e}")
            
            # Email
            try:
                await page.fill(selectors["email"], CUSTOM_USER_EMAIL)
                print(f"✓ Filled Email '{CUSTOM_USER_EMAIL}' using {selectors['email']}")
            except Exception as e:
                print(f"✗ Could not fill Email: {e}")
            
            # Contact
            try:
                await page.fill(selectors["contact"], CUSTOM_USER_PHONE)
                print(f"✓ Filled Contact using {selectors['contact']}")
            except Exception as e:
                print(f"✗ Could not fill Contact: {e}")
            
            # Submit
            try:
                await page.click(selectors["submit"])
                print(f"✓ Clicked Submit using {selectors['submit']}")
            except Exception as e:
                print(f"✗ Could not click Submit: {e}")
            
            # Wait to see results
            await page.screenshot(path="custom_selectors_result.png")
            print("Screenshot saved as custom_selectors_result.png")
            
            print("Keeping browser open for 10 seconds...")
            await asyncio.sleep(10)
            
        finally:
            await browser.close()

async def restart_quiz():
    """Function to restart the quiz if needed"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        try:
            # Navigate to the website
            await page.goto("https://gptchatviewer.com/", wait_until="networkidle")
            
            # Take screenshot of initial state
            await page.screenshot(path="restart_quiz.png")
            print("Screenshot saved as restart_quiz.png")
            
            # Look for restart/reset buttons
            print("Looking for restart/reset options...")
            
            # Try common patterns for restart buttons
            restart_selectors = [
                "button:has-text('Restart')", 
                "button:has-text('Reset')", 
                "button:has-text('Try Again')",
                "a:has-text('Restart')",
                "a:has-text('Start Over')",
                ".restart-button",
                "#restart"
            ]
            
            for selector in restart_selectors:
                try:
                    element = await page.query_selector(selector)
                    if element:
                        print(f"Found restart element using selector: {selector}")
                        await element.click()
                        print("Clicked restart element")
                        await page.screenshot(path="after_restart.png")
                        print("Screenshot saved as after_restart.png")
                        break
                except Exception as e:
                    pass
            else:
                print("No specific restart button found")
                
                # Try to look for any buttons
                buttons = await page.query_selector_all("button")
                print(f"Found {len(buttons)} buttons on the page")
                
                for i, button in enumerate(buttons):
                    text = await button.text_content()
                    print(f"Button {i+1}: '{text}'")
                
                # Look for "Get Started" button as an alternative way to restart
                try:
                    start_button = await page.query_selector("text=Get Started")
                    if start_button:
                        print("Found 'Get Started' button, clicking it")
                        await start_button.click()
                        print("Clicked 'Get Started'")
                        await page.screenshot(path="after_restart_get_started.png")
                except Exception as e:
                    print(f"Error finding Get Started: {e}")
            
            # Keep browser open for manual check
            print("Keeping browser open for manual verification for 10 seconds...")
            await asyncio.sleep(10)
            
        except Exception as e:
            print(f"Error during restart: {e}")
            await page.screenshot(path="restart_error.png")
        
        finally:
            await browser.close()

if __name__ == "__main__":
    print("=== Playwright Test Automation ===")
    print("What would you like to do?")
    print("1. Run automated test (default)")
    print("2. Inspect page elements to find correct selectors")
    print("3. Run test with custom selectors")
    print("4. Restart quiz")
    print("5. Update test data and run test")
    
    choice = input("Enter your choice (1-5), or press Enter for default: ")
    
    if choice == "2":
        print("Running inspector to analyze page elements...")
        asyncio.run(inspect_page_elements())
    elif choice == "3":
        print("Enter custom CSS selectors (press Enter to use defaults):")
        selectors = {}
        selectors["full_name"] = input("Full Name field selector: ").strip() or None
        selectors["country"] = input("Country dropdown selector: ").strip() or None
        selectors["email"] = input("Email field selector: ").strip() or None
        selectors["contact"] = input("Contact field selector: ").strip() or None
        selectors["submit"] = input("Submit button selector: ").strip() or None
        
        # Remove None values
        selectors = {k: v for k, v in selectors.items() if v}
        
        print("\nRunning test with custom selectors...")
        asyncio.run(run_with_custom_selectors(selectors))
    elif choice == "4":
        print("Attempting to restart the quiz...")
        asyncio.run(restart_quiz())
    elif choice == "5":
        print("Update test data for the automation run")
        print("(Press Enter to keep current values)")
        
        # These variables are already in the global scope, no need to redeclare
        
        # Show current values and get new ones
        new_name = input(f"Name [{TEST_USER_NAME}]: ").strip()
        new_email = input(f"Email [{TEST_USER_EMAIL}]: ").strip()
        new_phone = input(f"Phone [{TEST_USER_PHONE}]: ").strip()
        new_country = input(f"Country [{TEST_USER_COUNTRY}]: ").strip()
        
        # Only update if new values were provided
        if new_name:
            TEST_USER_NAME = new_name
        if new_email:
            TEST_USER_EMAIL = new_email
        if new_phone:
            TEST_USER_PHONE = new_phone
        if new_country:
            TEST_USER_COUNTRY = new_country
            
        print(f"\nUpdated test data:")
        print(f"Name: {TEST_USER_NAME}")
        print(f"Email: {TEST_USER_EMAIL}")
        print(f"Phone: {TEST_USER_PHONE}")
        print(f"Country: {TEST_USER_COUNTRY}")
        
        print("\nRunning automated test with updated data...")
        asyncio.run(run_registration_test())
    else:
        print("Running standard automated test...")
        print("\nBased on element inspection, we know the form has:")
        print("- text input for name (no ID/label)")
        print("- select dropdown for country (no ID/label)")
        print("- email input (type='email')")
        print("- tel input for phone number (type='tel')")
        print("\nUsing selectors based on element types...")
        asyncio.run(run_registration_test())
