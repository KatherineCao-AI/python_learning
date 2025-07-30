import time

# --- DATA ---
# This structure is similar to the JavaScript version, using a list of dictionaries.
QUESTIONS = [
    {
        "question": "When faced with a difficult problem, you...",
        "answers": {
            "a": {"text": "Face it head-on with confidence.", "type": "Lion"},
            "b": {"text": "Analyze it from all angles before acting.", "type": "Owl"},
            "c": {"text": "Collaborate and talk it through with others.", "type": "Dolphin"},
            "d": {"text": "Find a clever or unconventional solution.", "type": "Fox"}
        }
    },
    {
        "question": "Your ideal weekend involves...",
        "answers": {
            "a": {"text": "Leading a group on an adventure.", "type": "Lion"},
            "b": {"text": "Quietly reading a book or learning something new.", "type": "Owl"},
            "c": {"text": "Socializing with a large group of friends.", "type": "Dolphin"},
            "d": {"text": "Exploring a new city or place on your own terms.", "type": "Fox"}
        }
    },
    {
        "question": "In a team project, you are the one who...",
        "answers": {
            "a": {"text": "Takes charge and delegates tasks.", "type": "Lion"},
            "b": {"text": "Ensures everything is well-planned and logical.", "type": "Owl"},
            "c": {"text": "Makes sure everyone is happy and communicating.", "type": "Dolphin"},
            "d": {"text": "Comes up with the creative, out-of-the-box ideas.", "type": "Fox"}
        }
    },
    {
        "question": "How do you prefer to learn?",
        "answers": {
            "a": {"text": "By doing and taking action.", "type": "Lion"},
            "b": {"text": "Through careful study and observation.", "type": "Owl"},
            "c": {"text": "By discussing and sharing ideas with others.", "type": "Dolphin"},
            "d": {"text": "Through trial and error, adapting as I go.", "type": "Fox"}
        }
    },
    {
        "question": "What is most important to you?",
        "answers": {
            "a": {"text": "Strength and courage.", "type": "Lion"},
            "b": {"text": "Wisdom and knowledge.", "type": "Owl"},
            "c": {"text": "Community and connection.", "type": "Dolphin"},
            "d": {"text": "Independence and ingenuity.", "type": "Fox"}
        }
    }
]

PERSONALITIES = {
    "Lion": {
        "title": "Lion",
        "description": "You are a natural leader, courageous and confident . You aren't afraid to take charge and face challenges head-on. People look to you for direction and strength."
    },
    "Owl": {
        "title": "Owl",
        "description": "You are wise, analytical, and observant. You prefer to think things through and value knowledge and logic. You offer thoughtful insights and a calm perspective."
    },
    "Dolphin": {
        "title": "Dolphin",
        "description": "You are social, communicative, and playful. You thrive in groups and value connection and harmony. You are excellent at bringing people together and creating a positive atmosphere."
    },
    "Fox": {
        "title": "Fox",
        "description": "You are clever, adaptable, and resourceful. You can think on your feet and find unique solutions to problems. You are independent and navigate situations with wit and ingenuity."
    }
}

# --- FUNCTIONS ---

def ask_question(question_data):
    """Displays a single question and its answers, and returns the chosen personality type."""
    print("\n" + "="*40)
    print(f"  {question_data['question']}")
    print("="*40)

    # Display answer options
    for key, answer in question_data['answers'].items():
        print(f"  {key}) {answer['text']}")

    # Get and validate user input
    while True:
        choice = input("\nYour choice (a, b, c, d): ").lower()
        if choice in question_data['answers']:
            return question_data['answers'][choice]['type']
        else:
            print("Invalid choice. Please enter a, b, c, or d.")

def calculate_result(scores):
    """Calculates the personality with the highest score."""
    # This finds the key (personality type) with the maximum value (score)
    final_personality = max(scores, key=scores.get)
    return PERSONALITIES[final_personality]

def run_quiz():
    """Main function to run the entire personality quiz."""
    print("--- What's Your Inner Animal? ---")
    print("Answer the following five questions to find out!")

    # Initialize scores
    scores = {"Lion": 0, "Owl": 0, "Dolphin": 0, "Fox": 0}

    # Loop through all questions
    for question_data in QUESTIONS:
        chosen_type = ask_question(question_data)
        scores[chosen_type] += 1

    print("\nCalculating your result...")
    time.sleep(2) # Add a little dramatic pause

    # Get and display the final result
    result = calculate_result(scores)

    print("\n" + "*"*40)
    print("  Your personality is the...".center(38))
    print(f"  🎉 {result['title'].upper()} 🎉".center(40))
    print("*"*40)
    print(f"\n  {result['description']}")
    print("\n" + "*"*40)


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    run_quiz()
