import pyautogui
import time

def find_coordinates():
    """Display current mouse coordinates in real time"""
    print("\n===== CURRENT MOUSE COORDINATES =====")
    print("Move your mouse to desired position...")
    print("Press Ctrl+C to exit coordinate finder")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            # Clear previous line and print new coordinates
            print(f"Current position: x: {x}, y: {y}", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nLast recorded position: x: {x}, y: {y}")
        return x, y

def enter_and_click_coordinates():
    """Allow user to manually enter coordinates and click at that position"""
    try:
        x = int(input("\nEnter X coordinate: "))
        y = int(input("Enter Y coordinate: "))
        print(f'New coordinates set to x: {x}, y: {y}')
        
        # Countdown before clicking
        print("Clicking at the coordinates in:")
        for i in range(3, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(0.5)
        print("Click!")
        
        # Perform the click
        pyautogui.click(x, y)
        print("Click completed at coordinates x: {0}, y: {1}".format(x, y))
    except ValueError:
        print("Error: Please enter valid numbers for coordinates.")
    
def main():
    while True:
        # Display menu
        print("\n===== COORDINATE TOOL =====")
        print("1. Find current mouse coordinates")
        print("2. Enter coordinates and click")
        print("3. Find coordinates, then click")
        print("4. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            find_coordinates()
        
        elif choice == '2':
            enter_and_click_coordinates()
            
        elif choice == '3':
            print("\nMove your mouse to desired position and press Ctrl+C to capture it")
            x, y = find_coordinates()
            print(f"\nCoordinates captured: x: {x}, y: {y}")
            
            confirm = input("Do you want to click at these coordinates? (y/n): ").lower()
            if confirm == 'y':
                print("Clicking at the coordinates in:")
                for i in range(3, 0, -1):
                    print(f"{i}...", end=" ", flush=True)
                    time.sleep(0.5)
                print("Click!")
                pyautogui.click(x, y)
                print("Click completed at coordinates x: {0}, y: {1}".format(x, y))
        
        elif choice == '4':
            print("Exiting coordinate tool. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    print("=== PyAutoGUI Coordinate Tool ===")
    print("This tool helps you work with screen coordinates")
    main()