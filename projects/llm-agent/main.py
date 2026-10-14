import argparse
import os
from tabnanny import process_tokens
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("api key was not found")

def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    p_tokens = 0
    c_tokens = 0
    message = ""

    if response != None:
        p_tokens = response.usage.prompt_tokens
        c_tokens = response.usage.completion_tokens

    else:
        raise RuntimeError("no response returned. API request likely failed.")

    if args.verbose:
        print(f"User prompt: {messages[0]["content"]}")
        print(f"Prompt tokens: {p_tokens}")
        print(f"Response tokens: {c_tokens}")

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
