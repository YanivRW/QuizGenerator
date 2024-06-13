import openai
import os

def get_user_input():
    while True:
        try:
            num_questions = int(input("Enter the number of questions (1-10): "))
            if 1 <= num_questions <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    difficulty_levels = ['easy', 'medium', 'hard']
    while True:
        difficulty_level = input("Enter the difficulty level (easy, medium, hard): ").lower()
        if difficulty_level in difficulty_levels:
            break
        else: 
            print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
    

    contexts = [
        'elementary students',
        'high school students',
        'graduate students',
        'undergraduate students'
    ]
    while True:
        print("Who is this quiz for?")
        print("1. elementary students")
        print("2. high school students")
        print("3. graduate students")
        print("4. undergraduate students")
        
        try:
            context_number = int(input("Enter the number corresponding to the audience: "))
            if context_number == 1:
                audience = 'elementary students'
                print(audience)
                break

            elif context_number == 2:
                audience = 'high school students'
                print(audience)
                break
            elif context_number == 3:
                audience = 'graduate students'
                print(audience)
                break
            elif context_number == 4:
                audience = 'undergraduate students'
                print(audience)
                break
        except ValueError:
                print("Invalid input. Please choose a number between 1 and 4.")
    
    while True:
        try:
            prompt_number = int(input("""Choose prompt techniques number: 
            1. Few-shot Learning + Context-setting
            2. Role-playing + Conditional Generation + Personalization
            3. Chain-of-thought Prompting + Instructional Prompts
            4. Few-shot Learning + Question Templates + Context-setting
            5. Role-playing + Chain-of-thought Prompting + Conditional Generation + Personalization
            """))
            if 1 <= prompt_number <= 5:
                break
            else:            
                print("Invalid input. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 5.")
    
    # context = input("Enter the context of the quiz (e.g., 'graduate students studying NLP'): ") 
    return num_questions, difficulty_level, audience, prompt_number


# Create a prompt for OpenAI API

#Few-shot Learning + Context-setting
def create_prompt(num_questions, difficulty_level, audience, prompt_number):
    if prompt_number == 1:
        system_prompt = f"""You are an expert in educational content creation and a specialist in developing high-quality quiz questions. You will generate quiz questions on world history for a course aimed at {audience}. you are to only print the questions and nothing else. """
        user_prompt = f"""
       Below are a few examples of well-crafted quiz questions on world history. Your task is to generate additional quiz questions that are similarly structured and appropriate {audience}. Ensure the questions cover different periods, important figures and significant events in world history.

            Examples:
            1. Which empire was known for its extensive road network and advanced engineering, and was centered in modern-day Italy?
                a) The Roman Empire
                b) The Byzantine Empire
                c) The Ottoman Empire
                d) The Persian Empire

            2. Who was the first President of the United States, serving from 1789 to 1797?
                a) Thomas Jefferson
                b) Abraham Lincoln
                c) George Washington
                d) John Adams

            3. The fall of the Berlin Wall in 1989 symbolized the end of which global conflict?
                a) World War I
                b) World War II
                c) The Cold War
                d) The Korean War


        Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. 
        """
        return user_prompt, system_prompt
    
    # Role-playing + Conditional Generation + Personalization

    elif prompt_number == 2:
        system_prompt = f"ou are an expert in educational content creation and a specialist in developing high-quality quiz questions. You will generate quiz questions on world history tailored to the interests and learning needs of {audience}. you are to only print the questions and nothing else."
        user_prompt = f"""
       Assume the role of a knowledgeable and engaging history teacher. Your task is to create quiz questions on world history that cater to high school students. Focus on different periods and significant events, and ensure the questions are tailored to their interests and learning levels.

            Examples:
            1. How did the construction of the Great Wall of China benefit the Chinese empire during ancient times?
                a) It promoted trade with neighboring countries
                b) It protected against invasions from northern tribes
                c) It served as a religious monument
                d) It was used for agricultural development

            2. Which event marked the beginning of the Renaissance period in Europe?
                a) The fall of Constantinople
                b) The discovery of the Americas
                c) The signing of the Magna Carta
                d) The start of the Hundred Years' War

            3. What was the primary cause of World War I?
                a) The assassination of Archduke Franz Ferdinand
                b) The rise of Adolf Hitler
                c) The bombing of Pearl Harbor
                d) The Russian Revolution

        Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. 
        """
        return user_prompt, system_prompt
    
    # Chain-of-thought Prompting + Instructional Prompts

    elif prompt_number == 3:
        system_prompt = f"""You are an expert in educational content creation and a specialist in developing high-quality quiz questions. You will generate quiz questions on world history for a course aimed at {audience}. you are to only print the questions and nothing else."""
        user_prompt = f"""Your task is to create quiz questions on world history. Use chain-of-thought prompting to break down the reasoning process for complex questions. Additionally, follow the instructional prompts to ensure clarity, relevance, and appropriate difficulty for {audience}.

            Instructions:
            - Provide a brief explanation or context for each question to guide the reasoning process.
            - Ensure each question covers significant events, figures, or periods in world history.
            - Maintain a balance between different difficulty levels to engage students with varying knowledge.

            Examples:
            1. Question: Which empire was known for its extensive road network and advanced engineering, and was centered in modern-day Italy?
               a) The Roman Empire
               b) The Byzantine Empire
               c) The Ottoman Empire
               d) The Persian Empire

            2. Question: Who was the first President of the United States, serving from 1789 to 1797?
               a) Thomas Jefferson
               b) Abraham Lincoln
               c) George Washington
               d) John Adams

            3. Question: The fall of the Berlin Wall in 1989 symbolized the end of which global conflict?
               a) World War I
               b) World War II
               c) The Cold War
               d) The Korean War
               
                Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. """
        return user_prompt, system_prompt
    
    # Few-shot Learning + Question Templates + Context-setting

    elif prompt_number == 4:
        system_prompt = f"You are an expert in educational content creation and a specialist in developing high-quality quiz questions. You will generate quiz questions on world history for a course aimed at {audience}. you are to only print the questions and nothing else."
        user_prompt = f"""Below are a few examples of well-crafted quiz questions on world history. Your task is to generate additional quiz questions that are similarly structured and appropriate for {audience}. Use the provided question templates to ensure consistency, and set the context clearly to match the educational level and interests of {audience}.

            Examples:
            1. Which empire was known for its extensive road network and advanced engineering, and was centered in modern-day Italy?
               a) The Roman Empire
               b) The Byzantine Empire
               c) The Ottoman Empire
               d) The Persian Empire

            2. Who was the first President of the United States, serving from 1789 to 1797?
               a) Thomas Jefferson
               b) Abraham Lincoln
               c) George Washington
               d) John Adams

            3. he fall of the Berlin Wall in 1989 symbolized the end of which global conflict?
               a) World War I
               b) World War II
               c) The Cold War
               d) The Korean War
               
             Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. """

        return user_prompt, system_prompt
    
    # Role-playing + Chain-of-thought Prompting + Conditional Generation + Personalization

    elif prompt_number == 5:
        system_prompt = f"You are an expert in educational content creation and a specialist in developing high-quality quiz questions. You will generate quiz questions on world history tailored to the interests and learning needs of {audience}. you are to only print the questions and nothing else."
        user_prompt = f"""Assume the role of an engaging and knowledgeable history teacher. Your task is to create quiz questions on world history that cater to {audience}. Use chain-of-thought prompting to break down the reasoning process for complex questions. Apply conditional generation to ensure the questions cover specific periods and significant events. Personalize the questions to make them relevant and interesting for {audience}.

            Examples:
            1. Which empire was known for its extensive road network and advanced engineering, and was centered in modern-day Italy?
               a) The Roman Empire
               b) The Byzantine Empire
               c) The Ottoman Empire
               d) The Persian Empire

            2. Who was the first President of the United States, serving from 1789 to 1797?
               a) Thomas Jefferson
               b) Abraham Lincoln
               c) George Washington
               d) John Adams

            3. The fall of the Berlin Wall in 1989 symbolized the end of which global conflict?
               a) World War I
               b) World War II
               c) The Cold War
               d) The Korean War
               
                Now, generate {num_questions} additional quiz questions at {difficulty_level} difficulty level on world history. """
        return user_prompt, system_prompt
    
    else:
        raise ValueError("Invalid prompt number")


def get_quiz_questions(user_prompt, system_prompt):
    # Setup OpenAI API call
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = openai.Client()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
       messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
         max_tokens=1000,
         temperature=0.2  # Control the creativity of the output
    )


    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def get_answers_to_quiz(questions):
    system_prompt = "You are an expert in educational content creation. Provide the correct answers to the following quiz questions:"
    user_prompt = f"Quiz Questions:\n{questions}\n"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = openai.Client()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1000,
        temperature=0.2
    )
    
    return completion.choices[0].message.content


def prompt_user_to_answer(questions):
    while True:
        answer_prompt = input("Do you want to answer the quiz questions? (yes/no): ").lower()
        if answer_prompt == 'yes':
            answers = get_answers_to_quiz(questions)
            print("Answers to the quiz questions:\n")
            print(answers)
            
            while True:
                new_quiz_prompt = input("Do you want to generate another quiz? (yes/no): ").lower()
                if new_quiz_prompt == 'yes':
                    main()
                    break
                elif new_quiz_prompt == 'no':
                    print("Exiting the script.")
                    exit()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            break
        elif answer_prompt == 'no':
            while True:
                new_quiz_prompt = input("Do you want to generate another quiz? (yes/no): ").lower()
                if new_quiz_prompt == 'yes':
                    main()
                    break
                elif new_quiz_prompt == 'no':
                    print("Exiting the script.")
                    exit()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



def main():
    num_questions, difficulty_level, promt_number,context  = get_user_input()
    user_prompt, system_prompt = create_prompt(num_questions, difficulty_level,promt_number, context)
    questions = get_quiz_questions(user_prompt, system_prompt)
    prompt_user_to_answer(questions)
    

if __name__ == "__main__":
    main()
