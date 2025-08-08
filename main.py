import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERATIONS

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    print("Hello from mini-ai-coder!")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) == 1:
        sys.exit(1)
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for call in range(0, MAX_ITERATIONS):
        try:
            if call > MAX_ITERATIONS:
                print(f"Maximum iterations ({MAX_ITERS}) reached.")
                sys.exit(1)
            final_response = generate_content(client, messages)
            if final_response:
                return final_response
        except Exception as e:
            print(e)

def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
            
    # Add candidate content to messages
    for candidate in response.candidates:
        messages.append(candidate.content)

    if not response.function_calls:
        if '--verbose' in sys.argv:
            print(f"User prompt: {prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        function_call_result = call_function(function_call_part, '--verbose' in sys.argv)
        function_response = function_call_result.parts[0].function_response.response
        # Add function response to messages
        messages.append(types.Content(role="tool", parts=[types.Part(text=function_response)]))
        if not function_response:
            raise Exception("No function called")
        print(f"-> {function_call_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
