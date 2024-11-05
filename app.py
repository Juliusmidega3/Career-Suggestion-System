from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from main import recommend_careers  # Import the recommend_careers function from main.py

app = Flask(__name__)

# Sample career data to pass to the recommendation function
career_data = pd.DataFrame({
    'career': ['Data Scientist', 'Psychologist', 'Software Engineer', 'Product Manager'],
    'required_traits': [
        {'openness': 80, 'conscientiousness': 75, 'extroversion': 60, 'agreeableness': 70, 'neuroticism': 40},
        {'openness': 85, 'conscientiousness': 65, 'extroversion': 50, 'agreeableness': 80, 'neuroticism': 45},
        {'openness': 60, 'conscientiousness': 80, 'extroversion': 70, 'agreeableness': 65, 'neuroticism': 50},
        {'openness': 75, 'conscientiousness': 70, 'extroversion': 75, 'agreeableness': 70, 'neuroticism': 45}
    ],
    'relevant_fields': [['Data Science', 'Computer Science'], ['Psychology'], ['Computer Science'], ['Business']],
    'related_interests': [['Machine Learning', 'Data Analysis'], ['Psychology'], ['Software Development'], ['Product Design', 'Management']]
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Retrieve form data
    eq_score = int(request.form['eq_score'])
    personality_traits = {
        'openness': int(request.form['openness']),
        'conscientiousness': int(request.form['conscientiousness']),
        'extroversion': int(request.form['extroversion']),
        'agreeableness': int(request.form['agreeableness']),
        'neuroticism': int(request.form['neuroticism'])
    }
    academic_background = request.form['academic_background'].split(',')
    interests = request.form['interests'].split(',')

    # Package user data
    user_data = {
        'eq_score': eq_score,
        'personality_traits': personality_traits,
        'academic_background': academic_background,
        'interests': interests
    }

    # Get recommendations
    top_careers = recommend_careers(user_data, career_data)
    
    return render_template('results.html', careers=top_careers)

if __name__ == '__main__':
    app.run(debug=True)
