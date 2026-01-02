import google.generativeai as genai
from config import gemini_key

genai.configure(api_key=gemini_key)

models = genai.list_models()

for m in models:
    print(m.name)
