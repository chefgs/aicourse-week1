import streamlit as st
import random
import os.path

# ------------- Quiz Questions ------------- #
QUIZ_QUESTIONS = [
    {
        "question": "Which city is known as the 'Manchester of South India'?",
        "options": ["Madurai", "Coimbatore", "Chennai", "Salem"],
        "answer": "Coimbatore",
        "image": "images/coimbatore.jpg"
    },
    {
        "question": "Which river flows through the city of Tiruchirappalli?",
        "options": ["Cauvery", "Vaigai", "Palar", "Bhavani"],
        "answer": "Cauvery",
        "image": "images/cauvery.jpg"
    },
    {
        "question": "Which temple is famous for its massive Gopuram in Madurai?",
        "options": ["Meenakshi Amman Temple", "Ramanathaswamy Temple", "Kapaleeshwarar Temple", "Brihadeeswarar Temple"],
        "answer": "Meenakshi Amman Temple",
        "image": "images/meenakshi.jpg"
    },
    {
        "question": "What is the state animal of Tamil Nadu?",
        "options": ["Nilgiri Tahr", "Tiger", "Elephant", "Lion"],
        "answer": "Nilgiri Tahr",
        "image": "images/nilgiri_tahr.jpg"
    },
    {
        "question": "Which language is predominantly spoken in Tamil Nadu?",
        "options": ["Telugu", "Tamil", "Kannada", "Malayalam"],
        "answer": "Tamil",
        "image": "images/tamil.jpg"
    },
    {
        "question": "Which is the highest peak in Tamil Nadu?",
        "options": ["Doddabetta", "Anamudi", "Velliangiri", "Nilgiri Hills"],
        "answer": "Doddabetta",
        "image": "images/doddabetta.jpg"
    },
    {
        "question": "Who was the founder of Dravidian movement in Tamil Nadu?",
        "options": ["C.N. Annadurai", "Periyar E. V. Ramasamy", "K. Kamaraj", "M.G. Ramachandran"],
        "answer": "Periyar E. V. Ramasamy",
        "image": "images/periyar.jpg"
    },
    {
        "question": "Which city is known for the Marina Beach?",
        "options": ["Chennai", "Thoothukudi", "Kanyakumari", "Cuddalore"],
        "answer": "Chennai",
        "image": "images/marina_beach.jpg"
    },
    {
        "question": "Which dance form originated in Tamil Nadu?",
        "options": ["Bharatanatyam", "Kathak", "Odissi", "Mohiniyattam"],
        "answer": "Bharatanatyam",
        "image": "images/bharatanatyam.jpg"
    },
    {
        "question": "Which district in Tamil Nadu is famous for the hill station Ooty?",
        "options": ["Nilgiris", "Salem", "Coimbatore", "Erode"],
        "answer": "Nilgiris",
        "image": "images/ooty.jpg"
    },
    {
        "question": "Which port is one of the oldest artificial harbors in India?",
        "options": ["Chennai Port", "Tuticorin Port", "Ennore Port", "Nagapattinam Port"],
        "answer": "Chennai Port",
        "image": "images/chennai_port.jpg"
    },
    {
        "question": "Who was the first woman Chief Minister of Tamil Nadu?",
        "options": ["Jayalalithaa", "Janaki Ramachandran", "Indira Gandhi", "Sasikala"],
        "answer": "Janaki Ramachandran",
        "image": "images/janaki.jpg"
    },
    {
        "question": "Which dam is built across the Bhavani River in Tamil Nadu?",
        "options": ["Mettur Dam", "Vaigai Dam", "Parambikulam Dam", "Bhavanisagar Dam"],
        "answer": "Bhavanisagar Dam",
        "image": "images/bhavanisagar.jpg"
    },
    {
        "question": "Which festival marks the Tamil New Year?",
        "options": ["Pongal", "Deepavali", "Puthandu", "Aadi Perukku"],
        "answer": "Puthandu",
        "image": "images/puthandu.jpg"
    },
    {
        "question": "Which UNESCO World Heritage site is located near Chennai?",
        "options": ["Mahabalipuram", "Thanjavur", "Kanchipuram", "Madurai"],
        "answer": "Mahabalipuram",
        "image": "images/mahabalipuram.jpg"
    },
    {
        "question": "The famous Chidambaram temple is dedicated to which deity?",
        "options": ["Vishnu", "Murugan", "Shiva", "Amman"],
        "answer": "Shiva",
        "image": "images/chidambaram.jpg"
    },
    {
        "question": "Which wildlife sanctuary in Tamil Nadu is famous for elephants?",
        "options": ["Mudumalai", "Guindy", "Vandalur", "Indira Gandhi"],
        "answer": "Mudumalai",
        "image": "images/mudumalai.jpg"
    },
    {
        "question": "Which ancient Tamil literature is known as the ‘Tamil Veda’?",
        "options": ["Thirukkural", "Silappathikaram", "Tholkappiyam", "Sangam Poems"],
        "answer": "Thirukkural",
        "image": "images/thirukkural.jpg"
    },
    {
        "question": "Which is the southernmost tip of mainland India?",
        "options": ["Kanyakumari", "Rameswaram", "Thoothukudi", "Nagapattinam"],
        "answer": "Kanyakumari",
        "image": "images/kanyakumari.jpg"
    },
    {
        "question": "What is the traditional sport played during Pongal festival?",
        "options": ["Jallikattu", "Kabbadi", "Silambam", "Kho-Kho"],
        "answer": "Jallikattu",
        "image": "images/jallikattu.jpg"
    }
]


# ------------- Streamlit App ------------- #

st.set_page_config(page_title="Tamil Nadu Quiz", layout="wide")

# Custom CSS for background image and transparency
st.markdown(
    """
    <style>
    .main {
        background: url('https://www.tripsavvy.com/thmb/vOiRtOxFgQJ8mFfD_rTABn3eK8o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-534577119-57ac2a785f9b58974ae306d2.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
    }
    /* Set general text color to black, excluding buttons */
    div.stMarkdown, div.stRadio, div.stSlider, div:not(.stButton) p, h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }
    .stProgress .st-bo {
        background-color: rgba(38, 39, 48, 0.8) !important;
    }
    .stProgress .st-bp {
        background-color: #ff9900 !important;
    }
    /* Button styling */
    .stButton > button {
        background-color: #6a0dad !important;  /* Purple background */
        color: white !important;               /* White text */
        font-weight: bold !important;          /* Bold font */
        font-family: 'Arial', sans-serif !important; /* Font family */
        border: none !important;               /* No border */
        border-radius: 6px !important;         /* Rounded corners */
        padding: 8px 16px !important;          /* Padding */
        transition: all 0.3s ease !important;  /* Smooth transition */
        box-shadow: 0 4px 6px rgba(106, 13, 173, 0.3) !important; /* Shadow */
        margin: 10px 0 !important;             /* Margin */
        text-align: center !important;         /* Center alignment for text */
        display: block !important;             /* Block display for full width in container */
        width: fit-content !important;         /* Width based on content */
        min-width: 120px !important;           /* Minimum width */
    }
    
    /* Ensure button text color is white */
    .stButton > button span {
        color: white !important;
    }
    
    /* Target button label specifically */
    .stButton > button p {
        color: white !important;
    }
    
    /* Extra override for button text */
    button[kind="primary"] {
        color: white !important;
    }
    
    /* Override any other potential text elements in buttons */
    .stButton * {
        color: white !important;
    }
    /* Button hover effect */
    .stButton > button:hover {
        background-color: #8a2be2 !important;  /* Lighter purple on hover */
        box-shadow: 0 6px 8px rgba(106, 13, 173, 0.5) !important; /* Larger shadow */
        transform: translateY(-2px) !important; /* Slight raise effect */
    }
    /* Button active/click effect */
    .stButton > button:active {
        transform: translateY(0px) !important; /* Press down effect */
        box-shadow: 0 2px 4px rgba(106, 13, 173, 0.3) !important; /* Smaller shadow */
    }
    /* Radio button styling - option labels */
    .stRadio label {
        font-weight: 500 !important;
        color: black !important;
        font-family: 'Arial', sans-serif !important;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #6a0dad;'>🧑‍🎓 Tamil Nadu Quiz Challenge</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #000;'>Test your knowledge about Tamil Nadu's history, culture, and places!</h3>", unsafe_allow_html=True)

num_questions = st.slider("Select number of questions:", 5, 20, 5, step=5)

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(QUIZ_QUESTIONS, k=min(num_questions, len(QUIZ_QUESTIONS)))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = [None] * num_questions
    st.session_state.completed = False

def restart_quiz():
    st.session_state.questions = random.sample(QUIZ_QUESTIONS, k=min(num_questions, len(QUIZ_QUESTIONS)))
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = [None] * num_questions
    st.session_state.completed = False

col1, col2 = st.columns([1, 3])
with col1:
    st.button("Restart Quiz", on_click=restart_quiz, key="restart_button")

if not st.session_state.completed:
    q = st.session_state.questions[st.session_state.current]
    st.progress((st.session_state.current + 1) / num_questions)
    # if "image" in q and q["image"]:
    #     image_path = os.path.join("images", q["image"])
    #     if os.path.exists(image_path):
    #         st.image(image_path, use_column_width=True, caption="Question Image")
    #     else:
    #         # If image doesn't exist locally, display a placeholder
    #         st.info(f"Image for {q['answer']} will be displayed here.")
    st.markdown(f"### Q{st.session_state.current + 1}: {q['question']}")
    
    # Initialize the answer as None if not already in session_state
    if f"radio_answer_{st.session_state.current}" not in st.session_state:
        st.session_state[f"radio_answer_{st.session_state.current}"] = None
    
    # Create radio with index=-1 to ensure no default selection
    user_answer = st.radio(
        "Choose an option:", 
        q["options"], 
        index=None, 
        key=f"radio_button_{st.session_state.current}"
    )
    
    # Create columns for button alignment - left indented
    btn_col1, btn_col2 = st.columns([1, 3])
    with btn_col1:
        button_label = "Next" if st.session_state.current < num_questions - 1 else "Finish"
        if st.button(button_label, key=f"next_button_{st.session_state.current}"):
            if user_answer is None:
                st.warning("Please select an answer before proceeding.")
                st.stop()
                
            st.session_state.answers[st.session_state.current] = user_answer
            if user_answer == q["answer"]:
                st.session_state.score += 1
            if st.session_state.current < num_questions - 1:
                st.session_state.current += 1
            else:
                st.session_state.completed = True
else:
    st.balloons()
    st.success(f"Quiz completed! Your score: {st.session_state.score}/{num_questions}")
    
    # Display a congratulatory message based on score
    score_percentage = (st.session_state.score / num_questions) * 100
    if score_percentage >= 80:
        st.markdown("<h3 style='text-align: center; color: green;'>Excellent! You're a Tamil Nadu Expert! 🏆</h3>", unsafe_allow_html=True)
    elif score_percentage >= 60:
        st.markdown("<h3 style='text-align: center; color: blue;'>Great job! You know Tamil Nadu well! 👏</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center; color: orange;'>Good try! Learn more about beautiful Tamil Nadu! 📚</h3>", unsafe_allow_html=True)
    
    st.markdown("#### Correct Answers:")
    for idx, q in enumerate(st.session_state.questions):
        st.write(f"**Q{idx+1}: {q['question']}**")
        
        if st.session_state.answers[idx] is None:
            st.markdown(f"⚠️ You did not provide an answer. Correct answer: **{q['answer']}**")
        elif st.session_state.answers[idx] == q['answer']:
            st.markdown(f"✅ Your answer: **{st.session_state.answers[idx]}** (Correct)")
        else:
            st.markdown(f"❌ Your answer: **{st.session_state.answers[idx]}** | Correct answer: **{q['answer']}**")
        
        # Display image for each question result if available
        if "image" in q and q["image"]:
            image_path = os.path.join("images", q["image"])
            if os.path.exists(image_path):
                st.image(image_path, width=300, caption=f"{q['answer']}")

