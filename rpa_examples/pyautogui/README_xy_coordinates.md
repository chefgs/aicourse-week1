# PyAutoGUI Coordinate Tool

This tool helps you work with screen coordinates for RPA (Robotic Process Automation) tasks. It offers multiple ways to identify and use screen coordinates.

## Features

1. **Find Coordinates**: Track your mouse in real-time to find coordinates of screen elements
2. **Enter Coordinates**: Manually enter coordinates to click at specific positions
3. **Find and Click**: Find coordinates by moving your mouse, then click at that position
4. **Safe Execution**: Includes countdown timers before clicking to give you time to prepare

## How to Use

### Prerequisites
Make sure you have the required packages installed:
```bash
pip install -r requirements.txt
```

### Running the Tool
```bash
python x_y_coordinates.py
```

### Using the Tool

When you run the tool, you'll see a menu with four options:

1. **Find current mouse coordinates**
   - Shows real-time coordinates as you move your mouse
   - Press Ctrl+C to stop and record the last position
   
2. **Enter coordinates and click**
   - Manually enter X and Y coordinates
   - Tool will click at those coordinates after a countdown
   
3. **Find coordinates, then click**
   - Combines options 1 and 2
   - Find coordinates with your mouse, then click at those exact coordinates
   
4. **Exit**
   - Exit the application

## Tips for Using Coordinates in RPA

- For most accurate results, ensure the target application window is in the same position each time
- Consider adding a small offset to click positions to account for variations
- Use this tool in conjunction with `screen-coordinates.py` to help identify UI elements

## Example Use Cases

- Automating repetitive clicks in applications
- Setting up RPA workflows that interact with specific UI elements
- Testing click positions before incorporating them into larger scripts
