import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv(override=False)  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is not set in the environment variables.")
    sys.exit(1)
client = OpenAI(api_key=api_key) 
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

print("sending prompt to model...")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant.Be concise."},
            {"role": "user", "content": "What is generative AI in once sentence?"}
        ],
        temperature=0.7,
        max_tokens=100,
    )
    print("Response from model:")
    print(f"Response: {response.choices[0].message.content}")
    print(f"Tokens used: {response.usage.total_tokens}")
except AuthenticationError:
    print("Error: Authentication failed. Please check your OPENAI_API_KEY.")
    sys.exit(1)
except APIConnectionError:
    print("Error: Failed to connect to the OpenAI API. Please check your internet connection.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")