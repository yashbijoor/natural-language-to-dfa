__all__=['gemini']

from .getExplanations import getExplanations
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def gemini(query, json):
    genai.configure(api_key=os.getenv("GEMINI_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Generate explanation stepwise for the DFA "+json+". The query for this DFA is "+query)
    return response.text
