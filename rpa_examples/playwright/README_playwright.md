# Playwright Test Automation

This tool demonstrates web automation using Playwright, a powerful browser automation library, with special handling for forms that lack proper labels, IDs, or names.

## Features

1. **Robust Element Selection**: Multiple selection strategies to handle various web page structures
2. **Debugging Tools**: Screenshots at each step and detailed logging
3. **Form Filling**: Automatically fills out registration forms
4. **Page Analysis**: Inspect page elements to find the correct selectors
5. **Custom Selectors**: Run tests with your own custom CSS selectors
6. **Type-Based Selection**: Specialized handling for forms without proper labels
7. **Quiz Restart**: Option to restart the quiz or form process
8. **Test Data Update**: Easily change the test data without modifying the code

## Installation

Make sure you have the required packages installed:

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install
```

## Usage Options

The script now offers five modes of operation:

### 1. Standard Test Mode

Runs the automated test with type-based selectors optimized for forms without proper labels:

```bash
python playwright-testautomation.py
# Then select option 1 or just press Enter
```

This mode now:

- Uses input types to find form elements (`input[type='text']`, `input[type='email']`, etc.)
- Works even when forms lack proper labels, IDs, or names
- Provides detailed logging about what's happening
- Takes screenshots at each step

### 2. Element Inspector Mode

Analyzes the page structure and helps you identify the correct selectors for each form element:

```bash
python playwright-testautomation.py
# Then select option 2
```

This mode will:

- Take screenshots of the page
- List all input fields with their attributes
- List all select/dropdown elements with their options
- List all buttons with their text and attributes
- Keep the browser open for 30 seconds so you can manually inspect elements

### 3. Custom Selector Mode

Run the test with your own CSS selectors (useful after using the inspector):

```bash
python playwright-testautomation.py
# Then select option 3 and enter your custom selectors
```

### 4. Quiz Restart Mode

Attempts to restart the quiz or form process:

```bash
python playwright-testautomation.py
# Then select option 4
```

This mode will:

- Search for restart/reset buttons
- Try common patterns for restart buttons
- Look for "Get Started" buttons as an alternative
- Take screenshots throughout the process

### 5. Update Test Data Mode

Easily change the test data without modifying the code:

```bash
python playwright-testautomation.py
# Then select option 5
```

This mode will:

- Show current values for name, email, phone, and country
- Allow you to enter new values or keep existing ones by pressing Enter
- Run the automated test with your updated data
- Can be used to quickly test different form inputs without editing the code

## Troubleshooting Selector Issues

If elements aren't being found correctly:

1. Run the script in inspector mode (option 2)
2. Look at the attributes of the problematic elements
3. Pay special attention to the element types when labels/IDs are missing

### Handling Forms Without Labels or IDs

When forms lack proper labels, IDs, or names (as shown by element inspection):

```text
Found 3 input elements
Input 1: Type=text, ID=no-id, Name=no-name
Input 2: Type=email, ID=no-id, Name=no-name
Input 3: Type=tel, ID=no-id, Name=no-name
```

In these cases:

1. Use element types as your primary selector strategy:
   - `input[type='text']` - For text inputs like name fields
   - `input[type='email']` - For email fields
   - `input[type='tel']` - For phone number fields
   - `select` - For dropdown menus

2. Use element order when multiple elements have the same type:
   - First text input: `document.querySelectorAll('input[type="text"]')[0]`
   - Second text input: `document.querySelectorAll('input[type="text"]')[1]`

3. Use browser developer tools to verify your selectors:
   - Open DevTools (F12)
   - In the Console tab, try: `document.querySelector('your-selector')`
   - If it returns an element, your selector is working

## Interpreting Element Inspection Results

The element inspection mode (option 2) provides valuable information about the page structure. Here's how to interpret the results:

### Input Elements

When you see output like this:

```text
Input 1: Type=text, ID=no-id, Name=no-name
```

This means:

- The input has type="text"
- The input doesn't have an ID attribute
- The input doesn't have a name attribute
- You should target it using `input[type='text']`

### Select Elements

When inspecting select elements, look at:

- The ID and name attributes
- The available options
- Whether any options are selected by default

### Buttons

Button inspection shows:

- The button text content
- Any type attributes (like "submit")
- Any ID or class attributes for targeting

### Using Inspection Results

1. Identify the element types and their order on the page
2. Choose selectors based on what attributes are available
3. If minimal attributes are available, use type-based selectors
4. For multiple similar elements, use positional selectors

## Screenshots

The script automatically takes screenshots at key points:

- `initial_page.png` - The page when first loaded
- `before_get_started.png` - Before clicking the Get Started button
- `after_get_started.png` - After clicking the Get Started button
- `form_field_*.png` - When trying to fill specific form fields
- `filled_form.png` - After filling all form fields
- `before_submit.png` - Before clicking the submit button
- `after_submit.png` - After submitting the form
- `restart_quiz.png` - When attempting to restart the quiz

## Example Custom Selectors

### For Forms Without Labels/IDs

```css
Full Name field: input[type='text']
Country dropdown: select
Email field: input[type='email']
Contact field: input[type='tel']
Submit button: button
```

### For Forms With Standard Attributes

```css
Full Name field: input[name="fullName"]
Country dropdown: select#country
Email field: input[type="email"]
Contact field: input[name="phone"]
Submit button: button[type="submit"]
```
