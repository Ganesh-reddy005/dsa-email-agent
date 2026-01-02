import json
import random
import os

DIFFICULTY_ORDER = ["Easy", "Medium", "Hard"]
PROGRESS_FILE = "progress.json"
JSON_PATH = "questions.json"


def get_random_questions(json_path: str):

    # Load all questions
    with open(json_path, 'r') as f:
        questions = json.load(f)['data']

    # Load or initialize progress
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as p:
            progress = json.load(p)
    else:
        progress = {
            'current_difficulty': 'Easy',
            'sent_question_ids': []
        }

    current_difficulty = progress['current_difficulty']
    sent_ids = set(progress['sent_question_ids'])

    # Filter questions by difficulty & not sent
    available_questions = [
        q for q in questions
        if q['difficulty'] == current_difficulty and q['id'] not in sent_ids
    ]

    # If none left, move to next difficulty
    if not available_questions:
        current_index = DIFFICULTY_ORDER.index(current_difficulty)

        if current_index == len(DIFFICULTY_ORDER) - 1:
            progress['sent_question_ids'] = []
        else:
            progress['current_difficulty'] = DIFFICULTY_ORDER[current_index + 1]
            progress['sent_question_ids'] = []

        with open(PROGRESS_FILE, 'w') as p:
            json.dump(progress, p, indent=2)

        return get_random_questions(json_path)

    # Pick question
    question = random.choice(available_questions)

    # Update progress CORRECTLY
    progress['sent_question_ids'].append(question['id'])

    with open(PROGRESS_FILE, 'w') as p:
        json.dump(progress, p, indent=2)

    return {
        "title": question["title"],
        "difficulty": question["difficulty"],
        "patterns": question["pattern"],
        "companies": [c['name'] for c in question['companies']]
    }


if __name__ == "__main__":
    res = get_random_questions(JSON_PATH)
    print(res)
