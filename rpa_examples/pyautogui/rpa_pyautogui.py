import pyautogui as pag
import time
import os

def click_button(button_name):
    """
    Clicks a button on the screen by its name.
    
    Args:
        button_name (str): The name of the button to click.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    button_path = os.path.join(script_dir, f'{button_name}.png')
    
    # Check if the image file exists
    if not os.path.exists(button_path):
        print(f"ERROR: Button image file '{button_name}.png' not found at:")
        print(f"       {button_path}")
        return False
    
    try:
        # Get screen size for debugging
        screen_width, screen_height = pag.size()
        print(f"Screen resolution: {screen_width}x{screen_height}")
        
        print(f"Looking for button image: {button_path}")
        # Locate the button on the screen with confidence parameter
        button_location = pag.locateOnScreen(button_path, confidence=0.8)
        
        if button_location is not None:
            print(f"Button found at: {button_location}")
            # Calculate the center of the button
            button_center = pag.center(button_location)
            # Move the mouse to the center of the button and click
            pag.moveTo(button_center)
            pag.click()
            return True
        else:
            print(f"Button '{button_name}' not found on the screen.")
            print("Make sure the application window is visible and not minimized.")
            print("If the button is visible but not detected, try creating a clearer screenshot.")
            return False
    except Exception as e:
        print(f"Error trying to locate or click button: {str(e)}")
        if "confidence" in str(e).lower():
            print("You need to install opencv-python for confidence parameter:")
            print("pip install opencv-python")
        return False

def main():
    """
    Main function to execute RPA tasks using PyAutoGUI.
    """
    print("===== PyAutoGUI RPA Button Clicker =====")
    print("This script will locate and click buttons on your screen.")
    
    # Get the script's directory path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Looking for button images in: {script_dir}")
    
    # List all files in the directory to help with debugging
    all_files = os.listdir(script_dir)
    print(f"All files found ({len(all_files)} files):")
    for file in all_files:
        print(f"  - {file}")
    
    # List available button images in the directory
    buttons = [f[:-4] for f in all_files if f.lower().endswith('.png')]
    
    if not buttons:
        print("\nNo button images (.png files) found in the current directory.")
        print("Please add button screenshot images with .png extension.")
        print("Example: 'restart_quiz.png' would appear as 'restart_quiz' in the list.")
        return
    
    print("\nAvailable buttons:")
    for idx, button in enumerate(buttons, 1):
        print(f"{idx}. {button}")
    
    try:
        # Display input prompt and ensure proper error handling
        choice_input = input("\nSelect a button to click (enter number) or 0 to exit: ").strip()
        
        # Early validation to avoid ValueError
        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            return
            
        choice = int(choice_input)
        
        if choice == 0:
            print("Exiting...")
            return
        
        # Validate the choice is within range
        if 1 <= choice <= len(buttons):
            button_name = buttons[choice-1]
            print(f"You selected: '{button_name}'")
            # Check if the image file exists
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, f"{button_name}.png")
            if not os.path.isfile(image_path):
                print(f"ERROR: The image file '{button_name}.png' does not exist at:")
                print(f"       {image_path}")
                return
            
            print(f"\nPreparing to click '{button_name}' button...")
            print("Please ensure the target window is visible.")
            
            # Countdown to give user time to switch to the target window
            for i in range(5, 0, -1):
                print(f"Starting in {i} seconds...", end="\r")
                time.sleep(1)
            
            print("\nAttempting to locate and click the button...")
            result = click_button(button_name)
            
            if result:
                print(f"Successfully clicked the '{button_name}' button!")
            else:
                print(f"Failed to click the '{button_name}' button. Make sure the button is visible on screen.")
        else:
            print("Invalid selection.")
    
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

