def run_personality_quiz():
    # Questions and their possible answers
    questions = {
        "What is your favorite color?": ["a. Red", "b. Blue", "c. Green"],
        "What is your preferred pet?": ["a. Dog", "b. Cat", "c. Fish"],
        "Choose a vacation destination": ["a. Beach", "b. Mountains", "c. City"],
    }

    # User's answers
    user_answers = []

    # Ask questions and get user input
    for question, options in questions.items():
        print(question)
        for option in options:
            print(option)
        user_answer = input("Your choice (enter a, b, or c): ")
        user_answers.append(user_answer)

    # Calculate personality result
    personality_type = calculate_personality(user_answers)

    # Display result and description
    display_personality_result(personality_type)


def calculate_personality(answers):
    # Simple scoring system (modify as needed)
    score_a = answers.count('a')
    score_b = answers.count('b')
    score_c = answers.count('c')

    # Determine personality type based on scores
    if score_a > score_b and score_a > score_c:
        return "Type A"
    elif score_b > score_a and score_b > score_c:
        return "Type B"
    else:
        return "Type C"


def display_personality_result(personality_type):
    # Personality types and their descriptions
    personality_descriptions = {
        "Type A": "You are ambitious, competitive, and enjoy taking charge of situations.",
        "Type B": "You are easy-going, creative, and prefer a laid-back approach to life.",
        "Type C": "You are detail-oriented, analytical, and value precision and accuracy.",
    }

    # Display result
    print("\nYour personality type is:", personality_type)
    print("Description:", personality_descriptions.get(personality_type, "No description available."))


if __name__ == "__main__":
    print("Welcome to the Personality Quiz!\n")
    run_personality_quiz()
