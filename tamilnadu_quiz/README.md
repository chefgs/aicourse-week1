# Tamil Nadu Quiz Application

A interactive quiz application about Tamil Nadu's history, culture, geography, and more, built with Streamlit.

## Features

- **Rich Quiz Content**: 20 questions covering various aspects of Tamil Nadu
- **Dynamic Quiz Experience**: Select the number of questions you want to answer
- **Visual Learning**: Images for each question (when available)
- **Interactive UI**: Clean, modern interface with attractive styling
- **Immediate Feedback**: Know right away if your answer is correct
- **Score Tracking**: See your final score and performance assessment
- **Randomized Questions**: Different questions each time you play

## Screenshots

(Screenshots to be added here)

## Technologies Used

- Python 3.x
- Streamlit
- Custom CSS styling

## How to Run

1. Clone this repository

1. Install the required packages:

```bash
pip install streamlit
```

1. Navigate to the project directory:

```bash
cd tamilnadu_quiz
```

1. Run the Streamlit app:

```bash
streamlit run tn_quiz.py
```

## Adding Images

The quiz uses images stored in the `images/` directory. Each image should be named according to the reference in the quiz questions array:

- coimbatore.jpg
- cauvery.jpg
- meenakshi.jpg
- nilgiri_tahr.jpg
- tamil.jpg
- doddabetta.jpg
- periyar.jpg
- marina_beach.jpg
- bharatanatyam.jpg
- ooty.jpg
- chennai_port.jpg
- janaki.jpg
- bhavanisagar.jpg
- puthandu.jpg
- mahabalipuram.jpg
- chidambaram.jpg
- mudumalai.jpg
- thirukkural.jpg
- kanyakumari.jpg
- jallikattu.jpg

## Customizing the Quiz

To add or modify questions, edit the `QUIZ_QUESTIONS` array in `tn_quiz.py`. Each question is a dictionary with the following format:

```python
{
    "question": "Question text here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct option here",
    "image": "images/image_name.jpg"
}
```

## Future Enhancements

- Timer functionality
- Different difficulty levels
- Sound effects
- Share results on social media
- Leaderboard functionality

## Contributing

Contributions to improve the quiz or add more questions are welcome. Please feel free to submit a pull request.

## License

[MIT](LICENSE)
