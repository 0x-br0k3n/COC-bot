import time
import tkinter as tk
from tkinter import Tk, Toplevel
import pyautogui

# Global variables to store the coordinates and the rectangle ID
start_x = None
start_y = None
rect_id = None # Store the ID of the rectangle object

# Create the main window. This needs to be a global for all functions to access.
root = Tk()

def on_mouse_down(event):
    """
    Records the starting position and begins drawing the rectangle.
    
    Args:
        event (tk.Event): The mouse button press event.
    """
    global start_x, start_y, rect_id
    start_x = event.x
    start_y = event.y
    
    # Create an initial rectangle on the canvas.
    # The fill is semi-transparent red, and the outline is a solid red.
    rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y,
                                      outline="#ff0000", width=2,
                                      fill='#ff0000', stipple="gray25")

def on_mouse_drag(event):
    """
    Updates the rectangle's size and position in real-time as the mouse drags.

    Args:
        event (tk.Event): The mouse motion event while a button is held down.
    """
    global rect_id
    if rect_id:
        # Get the current mouse position.
        end_x = event.x
        end_y = event.y
        
        # Update the rectangle's coordinates dynamically.
        # This will redraw the rectangle as the user drags the mouse.
        canvas.coords(rect_id, start_x, start_y, end_x, end_y)

def on_mouse_up(event):
    """
    Calculates the final region's dimensions and prints them.

    Args:
        event (tk.Event): The mouse button release event.
    """
    global start_x, start_y
    
    end_x = event.x
    end_y = event.y
    
    # Calculate the region's left, top, width, and height.
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    width = abs(start_x - end_x)
    height = abs(start_y - end_y)
    
    # Print the coordinates in a format ready for pyautogui.
    print(f"Region selected: (left={left}, top={top}, width={width}, height={height})")
    print(f"You can use this in your pyautogui script like this:")
    print(f"region=({left}, {top}, {width}, {height})")
    
    # Destroy the window to exit the script.
    root.destroy()

# --- Main application window setup ---
if __name__ == "__main__":
    # Hide the main window's title bar and borders.
    root.overrideredirect(True)
    
    # Get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Set the window to full-screen using geometry, which is compatible
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    
    # Make the window transparent and topmost.
    root.attributes('-alpha', 0.1)
    root.attributes('-topmost', True)
    
    # Create a canvas that fills the window, which we will draw on.
    canvas = tk.Canvas(root, bg='white', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Bind mouse events to the canvas.
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)
    
    print("Click and drag your mouse to select a region. Release to see the coordinates.")
    
    # Start the Tkinter event loop.
    time.sleep(5)
    root.mainloop()

