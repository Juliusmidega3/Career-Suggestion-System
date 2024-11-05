# Career Suggestion System

This project provides the logic and algorithms for a career suggestion system that recommends career paths based on a user’s emotional intelligence (EQ), personality traits, academic background, and personal interests. The focus is on designing a recommendation framework, which can be coded and integrated with API calls for dynamic user data.

---

## Project Structure

- **main.py** - Contains the full code for the recommendation logic, including data ingestion, API mock functions, scoring functions, and recommendation calculation.
- **data** - Placeholder folder for any user or career data files (optional for future extensions).
- **README.md** - Documentation and instructions for setting up and using the project.

---

## Features

- **Personality and EQ Matching**: Calculates similarity between user traits and the personality requirements of different careers.
- **Academic and Interest Match**: Matches academic backgrounds and interests to relevant career paths.
- **User-Friendly Output**: Displays top career recommendations based on calculated match scores.
- **Modular Design**: Easily adaptable to integrate with APIs for personality and EQ testing.

---

## Prerequisites

- **Python 3.6+**
- **Libraries**: Install the following libraries if not already available:

```bash
pip install pandas numpy scikit-learn
```

---

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Juliusmidega3/career-suggestion-system.git
   cd career-suggestion-system
   ```

2. **Run the Code**

   Execute the `main.py` script to see the career recommendations based on sample user data.

   ```bash
   python main.py
   ```

---

## Code Overview

### main.py

This script performs the following steps:

1. **Data Ingestion and Preprocessing**: Loads sample user and career data, including personality traits, academic background, and interests.
  
2. **API Mock Functions**: Simulates API calls to fetch user EQ and personality data.

3. **Scoring Functions**:
   - **`calculate_personality_match`**: Uses cosine similarity to measure alignment between user traits and the personality requirements of careers.
   - **`calculate_background_match`**: Evaluates the match score based on academic background and interests.
   - **`calculate_career_score`**: Combines EQ, personality, and background match scores to compute an overall match for each career.

4. **Recommendation Calculation**: The `recommend_careers` function computes top career recommendations based on match scores.

5. **Display Recommendations**: Outputs a ranked list of career suggestions with match scores.

---

## Example Output

After running `main.py`, you should see an output like:

```plaintext
Career Recommendations:
1. Data Scientist - Match Score: 0.85
2. Product Manager - Match Score: 0.78
3. Psychologist - Match Score: 0.72
```

---

## Customization

1. **User Data**: Modify the `user_data` dictionary to include actual user inputs for EQ, personality traits, academic background, and interests.
2. **Career Data**: Update the `career_data` DataFrame with additional careers and their required traits, relevant fields, and interests.

---

## Future Development

To expand this project:

- **API Integration**: Replace mock functions with actual API calls for dynamic personality and EQ data.
- **Data Storage**: Use a database to store user profiles and career information.
- **Web Interface**: Build a web application interface to input data and view career recommendations.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with any improvements or features.

---

## Contact

For any questions or feedback, please reach out at [midegajulius3@gmail.com].
