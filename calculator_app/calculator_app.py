import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Streamlit Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for better styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .calculator-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .result-container {
        background-color: #ffffff;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #e9ecef;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        font-weight: 500;
    }
    h1, h2, h3 {
        color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title("🧮 Streamlit Calculator")
st.markdown("A simple yet powerful calculator app built with Streamlit")

# Create a container for the calculator
calculator_container = st.container()

with calculator_container:
    st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
    
    # Create tabs for different calculator modes
    tab1, tab2 = st.tabs(["Basic Calculator", "Scientific Calculator"])
    
    with tab1:
        # Basic Calculator UI
        st.markdown("### Basic Calculator")
        
        # Create a container for displaying the result
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        result = st.empty()
        result.markdown("### 0")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input fields for numbers
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("First Number", value=0.0, step=1.0, key="basic_num1")
        with col2:
            num2 = st.number_input("Second Number", value=0.0, step=1.0, key="basic_num2")
        
        # Operation selection
        operation = st.selectbox(
            "Select Operation",
            ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"],
            key="basic_operation"
        )
        
        # Calculate button
        if st.button("Calculate", key="basic_calculate", use_container_width=True):
            if operation == "Addition (+)":
                calc_result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                calc_result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                calc_result = num1 * num2
                symbol = "×"
            elif operation == "Division (÷)":
                if num2 == 0:
                    result.error("Error: Division by zero!")
                else:
                    calc_result = num1 / num2
                    symbol = "÷"
            
            # Display the result with a nice formula
            if "calc_result" in locals() and not (operation == "Division (÷)" and num2 == 0):
                result_text = f"### {num1} {symbol} {num2} = {calc_result}"
                result.markdown(result_text)
    
    with tab2:
        # Scientific Calculator UI
        st.markdown("### Scientific Calculator")
        
        # Create a container for displaying the result
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        sci_result = st.empty()
        sci_result.markdown("### 0")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input field for number
        sci_num = st.number_input("Enter Number", value=0.0, step=1.0, key="sci_num")
        
        # Operation selection
        sci_operation = st.selectbox(
            "Select Operation",
            ["Square", "Square Root", "Cube", "Cube Root", "Sin", "Cos", "Tan", "Log (base 10)", "Natural Log"],
            key="sci_operation"
        )
        
        # Calculate button
        if st.button("Calculate", key="sci_calculate", use_container_width=True):
            if sci_operation == "Square":
                sci_calc_result = sci_num ** 2
                formula = f"{sci_num}²"
            elif sci_operation == "Square Root":
                if sci_num < 0:
                    sci_result.error("Error: Cannot calculate square root of a negative number!")
                else:
                    sci_calc_result = np.sqrt(sci_num)
                    formula = f"√{sci_num}"
            elif sci_operation == "Cube":
                sci_calc_result = sci_num ** 3
                formula = f"{sci_num}³"
            elif sci_operation == "Cube Root":
                sci_calc_result = np.cbrt(sci_num)
                formula = f"∛{sci_num}"
            elif sci_operation == "Sin":
                sci_calc_result = np.sin(sci_num)
                formula = f"sin({sci_num})"
            elif sci_operation == "Cos":
                sci_calc_result = np.cos(sci_num)
                formula = f"cos({sci_num})"
            elif sci_operation == "Tan":
                sci_calc_result = np.tan(sci_num)
                formula = f"tan({sci_num})"
            elif sci_operation == "Log (base 10)":
                if sci_num <= 0:
                    sci_result.error("Error: Cannot calculate log of a non-positive number!")
                else:
                    sci_calc_result = np.log10(sci_num)
                    formula = f"log₁₀({sci_num})"
            elif sci_operation == "Natural Log":
                if sci_num <= 0:
                    sci_result.error("Error: Cannot calculate natural log of a non-positive number!")
                else:
                    sci_calc_result = np.log(sci_num)
                    formula = f"ln({sci_num})"
            
            # Display the result with a nice formula
            if "sci_calc_result" in locals() and not ((sci_operation in ["Square Root", "Log (base 10)", "Natural Log"]) and sci_num <= 0):
                sci_result_text = f"### {formula} = {sci_calc_result}"
                sci_result.markdown(sci_result_text)
    
    # History Section
    st.markdown("### Calculation History")
    if "history" not in st.session_state:
        st.session_state.history = []
    
    # Display history in a table if it's not empty
    if st.session_state.history:
        history_df = pd.DataFrame(st.session_state.history)
        st.dataframe(history_df, use_container_width=True)
    else:
        st.info("No calculations performed yet.")
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
