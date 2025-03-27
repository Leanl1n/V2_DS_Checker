import os
import requests
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class DeepSeekTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def process_text(self, text: str, instruction: str) -> str:
        try:
            payload = {
                "model": "deepseek-chat",
                "temperature": 0,  # Added temperature parameter
                "messages": [
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": text}
                ]
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error processing text: {str(e)}")
