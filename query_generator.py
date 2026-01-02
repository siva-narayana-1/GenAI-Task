'''
In this we are developing the gemini model to generate the queries by given text & default prompt.
'''
import json
import sys
import os
import google.generativeai as genai
from config import gemini_key
from logger import Logger
log = Logger.get_logs("query_generator")

class Generateai:
    def __init__(self):
        self.model = None
        self.default_prompt = None
    def genai_connecction(self):
        try:
            genai.configure(api_key=gemini_key)
            self.model = genai.GenerativeModel("gemini-3-flash-preview")

            self.default_prompt = """
            You are an expert MongoDB query generator.

            You MUST convert the user question into a MongoDB query.

            Rules:
            - Only generate READ queries
            - Allowed operation: find
            - Do NOT generate update, delete, drop
            - Output ONLY valid JSON
            - No explanation, no text, no markdown

            Collection: students

            Schema:
            - name: string
            - age: number
            - department: string
            - cgpa: number
            - year: number

            Output (STRICT):
            "only the mongodb command of the output"
            """
        except:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.info(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
    def generate_query(self, user_question):
        try:
            self.genai_connecction()
            response = self.model.generate_content(self.default_prompt + "\n User Question: " + user_question)
            log.info(f"Response from model was : {response.text}")
            return response.text
        except:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.info(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

