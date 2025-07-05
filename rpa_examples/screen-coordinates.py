import streamlit as st

# Configuration
st.set_page_config(
    page_title="Mouse Coordinates Tracker",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state for showing/hiding overlay
if 'show_overlay' not in st.session_state:
    st.session_state.show_overlay = True

# Title and description
st.title("🎯 Mouse Coordinates Tracker")
st.markdown("""
<div style="background-color:#f8f9fa; padding:10px; border-radius:5px; margin-bottom:20px;">
<h2 style="margin-top:0; color:#FF5722;">Where to See Coordinates:</h2>
<p style="font-size:18px;">The coordinates appear in an <strong style="color:#FF5722;">ORANGE BOX</strong> at the top of your screen like this:</p>

<div style="text-align:center; margin:20px 0; position:relative;">
    <div style="border:2px dashed #FF5722; padding:30px; display:inline-block;">
        Your browser window content
        <div style="position:relative; width:100%; height:40px;"></div>
        <div style="position:absolute; top:20px; left:50%; transform:translateX(-50%); background:#FF5722; color:white; padding:10px 20px; border-radius:5px; font-family:monospace;">
            <strong>X: 483 | Y: 127</strong> | (Click to hide)
        </div>
    </div>
    <div style="position:absolute; top:-20px; left:50%; transform:translateX(-50%);">
        <span style="font-size:30px; color:#FF5722;">⬇️</span>
    </div>
</div>

<p>Track your mouse coordinates in real-time as you move around the screen</p>
</div>
""", unsafe_allow_html=True)

# Show/Hide button using Streamlit components
if not st.session_state.show_overlay:
    st.error("❌ The coordinate display is currently HIDDEN")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("📊 SHOW COORDINATES", use_container_width=True):
            st.session_state.show_overlay = True
            st.experimental_rerun()
    with col2:
        st.info("👆 Click this button to show the coordinate overlay")
else:
    # Very prominent notice that coordinates should be visible
    st.success("✅ COORDINATES ARE DISPLAYED IN THE ORANGE BOX")
    
    # Add a large arrow pointing up
    st.markdown("""
    <div style="text-align:center; font-size:30px; margin:10px 0;">
        ⬆️ LOOK FOR THE ORANGE BOX ABOVE ⬆️
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Option to hide via Streamlit button (alternative to clicking overlay)
        if st.button("🚫 HIDE COORDINATES", use_container_width=True):
            st.session_state.show_overlay = False
            st.experimental_rerun()
    with col2:
        st.info("👆 Click this button (or click the orange box) to hide the overlay")

# Only inject the overlay if it should be shown
if st.session_state.show_overlay:
    # Create a very simple but reliable coordinate tracker
    st.markdown("""
    <style>
    /* Styling for coordinate display - made more prominent */
    #coord-box {
        position: fixed;
        top: 80px;  /* Position lower to avoid header */
        left: 50%;  /* Center horizontally */
        transform: translateX(-50%);  /* Center trick */
        background: #FF5722;  /* Bright orange background */
        color: white;
        padding: 15px 25px;
        font-family: monospace;
        font-size: 20px;  /* Larger text */
        font-weight: bold;  /* Bold text */
        border-radius: 10px;
        z-index: 999999;  /* Very high z-index */
        cursor: pointer;
        border: 3px solid yellow;  /* Yellow border */
        box-shadow: 0 0 20px rgba(0,0,0,0.5);  /* Stronger shadow */
        animation: pulse 2s infinite;  /* Pulsing animation */
    }
    
    /* Pulsing animation to draw attention */
    @keyframes pulse {
        0% { transform: translateX(-50%) scale(1); }
        50% { transform: translateX(-50%) scale(1.05); }
        100% { transform: translateX(-50%) scale(1); }
    }
    </style>
    
    <!-- Simple coordinate display element -->
    <div id="coord-box">⬆️ MOVE MOUSE TO SEE COORDINATES ⬆️</div>
    
    <script>
    // Wait for page to fully load
    window.addEventListener('load', function() {
        // Get the coordinate box
        const coordBox = document.getElementById('coord-box');
        
        if (coordBox) {
            // Make sure it's visible
            coordBox.style.display = 'block';
            
            // Track mouse movement
            document.addEventListener('mousemove', function(e) {
                // Update with bold formatting
                coordBox.innerHTML = `<span style="color:yellow">X: ${e.pageX}</span> | <span style="color:yellow">Y: ${e.pageY}</span> | (Click to hide)`;
            });
            
            // Click to hide - uses Streamlit's session state via component communication
            coordBox.addEventListener('click', function() {
                // Send message to Streamlit to update session state
                window.parent.postMessage({
                    type: "streamlit:setComponentValue",
                    value: false
                }, "*");
            });
        } else {
            // If box not found, try to create it
            const newBox = document.createElement('div');
            newBox.id = 'coord-box';
            newBox.textContent = '⬆️ MOVE MOUSE TO SEE COORDINATES ⬆️';
            document.body.appendChild(newBox);
            console.log('Created new coordinate box');
            
            // Retry setup
            setTimeout(() => {
                const coordBox = document.getElementById('coord-box');
                if (coordBox) {
                    // Same event listeners as above
                    document.addEventListener('mousemove', function(e) {
                        coordBox.innerHTML = `<span style="color:yellow">X: ${e.pageX}</span> | <span style="color:yellow">Y: ${e.pageY}</span> | (Click to hide)`;
                    });
                    
                    coordBox.addEventListener('click', function() {
                        window.parent.postMessage({
                            type: "streamlit:setComponentValue",
                            value: false
                        }, "*");
                    });
                }
            }, 1000);
        }
    });
    </script>
    """, unsafe_allow_html=True)

# Instructions with visual emphasis
st.markdown("""
### 📋 How to use this tool:

<div style="padding: 15px; border: 2px solid #FF5722; border-radius: 5px; margin: 10px 0;">
<strong style="color:#FF5722; font-size:18px;">WHERE TO SEE THE COORDINATES:</strong>
<ul>
<li>Look for the <strong style="background-color:#FF5722; color:white; padding:2px 5px;">ORANGE BOX</strong> that appears in the center top area of your screen</li>
<li>Move your mouse anywhere in the browser window</li>
<li>The coordinates (X and Y values) will update in real-time inside the orange box</li>
</ul>
</div>

<ol>
<li>Move your mouse anywhere - coordinates appear in the orange box</li>
<li>Click on the orange box when you want to hide it</li>
<li>Use the "SHOW COORDINATES" button to make it appear again</li>
</ol>
""", unsafe_allow_html=True)

# Usage tips
with st.expander("Usage Tips"):
    st.markdown("""
    - **For RPA:** These coordinates can help you identify target positions
    - **Accuracy:** The coordinates show the position within the browser window
    - **Best practice:** Use these positions as reference for PyAutoGUI scripts
    - **Example code:** `pyautogui.click(x, y)`
    
    Note: For applications outside the browser, use the `pyautogui.position()` 
    function to get screen coordinates directly.
    """)

# Technical details in an expander
with st.expander("Technical Details"):
    st.markdown("""
    **How it works:**
    
    This app uses JavaScript to track mouse position within the browser and 
    displays the coordinates in a floating overlay. When you click the overlay,
    it communicates with Streamlit to update the session state and hide the overlay.
    
    **Limitations:**
    
    - The coordinates shown are relative to the browser window, not the screen
    - For RPA automation that needs screen coordinates, use PyAutoGUI directly
    
    **PyAutoGUI equivalent:**
    ```python
    import pyautogui
    # Get current mouse position
    x, y = pyautogui.position()
    print(f"X: {x} Y: {y}")
    ```
    """)