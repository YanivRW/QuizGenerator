# QuizGenerator
Lightricks home assignment 

markdown
Copy code
# Quiz Question Generator

This script generates quiz questions on world history using OpenAI's API. Users can specify the number of questions, difficulty level, target audience, and prompting technique. The script then generates the quiz questions and optionally provides the correct answers.

## Requirements

- Python 3.6 or higher
- `openai` library
- `python-dotenv` library

## Setup

### 1. Clone the Repository

```
git clone <repository-url>
cd <repository-directory>
2. Create a Virtual Environment (Optional but Recommended)


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Required Packages


pip install openai python-dotenv
4. Set Up OpenAI API Key
Create a .env file in the root directory of the project with the following content:

OPENAI_API_KEY=your-api-key-here

Replace your-api-key-here with your actual OpenAI API key. You can obtain an API key from the OpenAI website.

Ensure your .env file is included in your .gitignore to keep your API key secret:

echo ".env" >> .gitignore
Running the Script
python your_script_name.py

How to Use the Script
Enter the Number of Questions: The script will prompt you to enter the number of questions (between 1 and 10).

Select Difficulty Level: Choose from 'easy', 'medium', or 'hard'.

Specify the Audience: Indicate who the quiz is for by selecting:

1 for elementary students
2 for high school students
3 for graduate students
4 for undergraduate students
Choose Prompt Techniques: Select a prompting technique from the following options:

1 for Few-shot Learning + Context-setting
2 for Role-playing + Conditional Generation + Personalization
3 for Chain-of-thought Prompting + Instructional Prompts
4 for Few-shot Learning + Question Templates + Context-setting
5 for Role-playing + Chain-of-thought Prompting + Conditional Generation + Personalization
Generate Quiz Questions: The script will generate the quiz questions based on your inputs.

Answer the Quiz: You will be prompted to answer the quiz questions. If you choose 'yes', the script will provide the correct answers.

Generate Another Quiz or Exit: After displaying the answers, you can choose to generate another quiz or exit the script.

Example
Enter the number of questions (1-10): 5

Enter the difficulty level (easy, medium, hard): medium

Who is this quiz for?
1. elementary students
2. high school students
3. graduate students
4. undergraduate students
Enter the number corresponding to the audience: 2

Choose prompt techniques number: 
1. Few-shot Learning + Context-setting
2. Role-playing + Conditional Generation + Personalization
3. Chain-of-thought Prompting + Instructional Prompts
4. Few-shot Learning + Question Templates + Context-setting
5. Role-playing + Chain-of-thought Prompting + Conditional Generation + Personalization
Enter the number corresponding to the prompt technique: 3

The script will then generate and display the quiz questions based on your selections.

Notes
Make sure your .env file is not shared or exposed in public repositories to keep your API key secure.
For any issues or questions, refer to the OpenAI API documentation.
