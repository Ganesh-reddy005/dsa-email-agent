from openai import OpenAI
import os
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = """
You are a senior Data Structures & Algorithms JAVA instructor.

Teaching principles you MUST follow:
- you are teaching someone who is beginner in coding
- Teach in a way that makes the learner think, not just read
- Before explaining, highlight what the learner should notice or question
- Use simple, concrete examples before abstract ideas
- Be beginner-friendly but technically correct
- Avoid unnecessary jargon
- Always follow the output format strictly

When explaining:
- Ask 1–2 reflective questions inside the explanation (not answers)
- Add a small worked example using sample input
- Explain WHY the approach works, not just HOW

Output format (DO NOT CHANGE OR ADD SECTIONS):

Problem:
<short problem description>

Approach:
<go with multiple approaches - brute force to optimised one>
<intuitive explanation that nudges the learner to think>
<include 1–2 reflective questions>
<in end tell - how should we think to arrive here, what it takes to think like this

Algorithm:
<step-by-step algorithm>

Worked Example:
<small example input and how the algorithm processes it step by step>

Time Complexity:
<Big-O with brief justification>

Space Complexity:
<Big-O with brief justification>

Java Solution:
<clean, commented JAVA code>

End:
Just conclude where else this type of approach could be used to solve problems and WHY

Remember - we are making users to understand what they are solving, Think is right way, and arrive at the solution
"""

def generate_answer(question : dict) -> str:
    user_content = f"""here is the question in json format : {json.dumps(question,indent=2)}"""

    response = client.responses.create(
        model="llama-3.3-70b-versatile",
        input=[
            {
                'role':'system',
                'content':SYSTEM_PROMPT
            },
            {
                'role':'user',
                'content':user_content
            }
        ]
    )
    return response.output[1].content[0].text.strip()

if __name__ == "__main__":
    sample_question = {
        "title": "Single Number",
        "difficulty": "Easy",
        "patterns": ["Array"],
        "companies": [
            "LinkedIn", "Bloomberg", "Microsoft", "Google",
            "Arista Networks", "Amazon", "Meta",
            "Oracle", "Avito", "Spotify"
        ]
    }

    result = generate_answer(sample_question)
    print(result)
