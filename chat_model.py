from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

class ChatModel:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"
        self.system_message = {
            "role": "system",
            "content": "You are a nagging assistant. You like to remind users of the right way to do things and often give extra advice, even if it's not asked for. You can be a bit sarcastic but always with good intentions. Please respond in Korean."
        }

    def get_response(self, user_message):
        messages = [
            self.system_message,
            {
                "role": "user",
                "content": user_message
            }
        ]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"죄송합니다. 오류가 발생했습니다: {str(e)}"