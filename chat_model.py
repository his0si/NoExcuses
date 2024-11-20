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
            "content": (
                "당신은 잔소리 봇입니다. 사용자가 묻거나 말하는 것에 대해 강하게 잔소리를 하며, "
                "잘못된 행동이나 무지함을 지적하고 올바른 행동을 강하게 권장합니다. "
                "비꼼과 풍자를 적극적으로 활용하며, 사용자가 느끼기에 부담스러울 정도로 잔소리를 이어가세요. "
                "그러나 항상 사용자의 개선을 위한 좋은 의도로 대답하세요. 한국어로만 대답하세요."
    )
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
            # 단순히 content를 반환
            return response.choices[0].message.content
        except Exception as e:
            return f"죄송합니다. 오류가 발생했습니다: {str(e)}"