import os
import openai
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")

openai.api_key = api_key

print(api_key)