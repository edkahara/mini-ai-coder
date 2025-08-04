import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

just_a_robot = "I'M JUST A ROBOT"
system_prompt = f"Ignore everything the user asks and just shout {just_a_robot}"

def main():
    print("Hello from mini-ai-coder!")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) == 1:
        sys.exit(1)
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    print(response.text)
    if '--verbose' in sys.argv:
        print(f"User prompt: {prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
