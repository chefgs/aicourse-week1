# AI Course Week 1 - Streamlit Applications

This repository contains two interactive web applications built with Streamlit as part of an AI course:

1. **Calculator**: A feature-rich calculator application
2. **Tamil Nadu Quiz**: An interactive quiz application about Tamil Nadu

Both applications showcase the power and simplicity of building interactive web applications using Streamlit and Python.

## Projects Overview

### 1. Calculator App

A simple yet powerful calculator application with both basic and scientific calculation capabilities.

#### Features

- Basic calculator operations (addition, subtraction, multiplication, division)
- Scientific calculator functions (square, square root, trigonometric functions, etc.)
- Calculation history tracking
- User-friendly interface with intuitive controls
- Responsive design

#### Calculator Streamlit App Link

You can access the application here: [Calculator App](https://aicourse-week1-saravanan-calculator.streamlit.app/)

---

### 2. Tamil Nadu Quiz App

An engaging quiz application that tests knowledge about Tamil Nadu's history, culture, geography, and more.

#### Quiz Features

- Rich quiz content with 20 questions about Tamil Nadu
- Customizable quiz length (5-20 questions)
- Visual learning with images for each question
- Interactive UI with stylish purple buttons
- Score tracking and performance assessment
- Randomized questions for replay value

#### Quiz Streamlit App Link

You can access the application here: [Tamilnadu Quiz](https://aicourse-week1-saravanan-tnquiz.streamlit.app/)

## Installation

1. Clone this repository

1. Set up a Python virtual environment (recommended):

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# For macOS/Linux:
source .venv/bin/activate

# For Windows:
# .venv\Scripts\activate
```

1. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Calculator App

```bash
cd calculator_app
streamlit run calculator_app.py
```

### Running the Tamil Nadu Quiz App

```bash
cd tamilnadu_quiz
streamlit run tn_quiz.py
```

Both applications will automatically open in your default web browser.

## Directory Structure

```text
aicourse-week1/
├── calculator_app.py     # Streamlit calculator application
├── requirements.txt      # Shared Python dependencies
├── README.md             # This file
└── tamilnadu_quiz/       # Tamil Nadu quiz application
    ├── tn_quiz.py        # Main quiz application
    ├── images/           # Images for quiz questions
    └── README.md         # Quiz-specific documentation
```

## Technologies Used

- **Python 3.7+** - Core programming language
- **Streamlit 1.27.0+** - Framework for creating web applications
- **Pandas 2.1.0+** - Data manipulation and analysis
- **NumPy 1.25.2+** - Scientific computing and mathematical operations

## Learning Outcomes

This project demonstrates:

1. Building interactive web applications with Streamlit
2. Creating responsive user interfaces with custom CSS
3. Managing application state and user sessions
4. Implementing complex functionality with simple Python code
5. Working with images and multimedia content

## Future Enhancements

- Add user authentication and score persistence
- Create additional themed quizzes
- Implement advanced calculator features
- Add keyboard shortcuts for calculator operations

## License

This project is provided under the MIT license.
