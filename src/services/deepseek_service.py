import os
import requests
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class DeepSeekTool:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_text(self, input_text: str, instruction: str) -> Optional[str]:
        try:
            payload = {
                "model": "deepseek-reasoner",
                "messages": [
                    {"role": "system", "content": "You are an AI assistant. Use the provided text as your reference. Only use information from the provided text to answer questions or follow instructions. If the information needed is not in the reference text, state that clearly."},
                    {"role": "user", "content": f"Reference text:\n{input_text}\n\nInstructions: {instruction}"}
                ],
                "temperature": 0.0,
                "max_tokens": 2000,
                "top_p": 0.95
            }

            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
        
        except Exception as e:
            raise Exception(f"Error processing text: {str(e)}")
