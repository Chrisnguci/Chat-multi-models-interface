
import os
import openai
from dotenv import load_dotenv
# MOELS
DEEPSEEK_MODEL = "deepseek-reasoner"
GEMINI_MODEL = "gemini-1.5-flash"

load_dotenv()
class ModelChain:
	def __init__(self):
		self.gemini_client = openai.OpenAI(
			api_key = os.getenv("GEMINI_API_KEY"),
			base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
			)
		self.deepseek_client = openai.OpenAI(
 			api_key = os.getenv("DEEPSEEK_API_KEY"),
            base_url = "https://api.deepseek.com"
            )
		self.deepseek_messages = []
		self.gemini_messages = []
	def  get_gemini_response(self,user_input, system_prompt):
		messages = [{
			"role": "system",
			"content": system_prompt
					},
					{
			"role": "user",
			"content": user_input
		}
		]
		try:
			stream = self.gemini_client.chat.completions.create(
				model = GEMINI_MODEL,
				messages= messages,
				stream = True)
			full_response = ""
			for chunk in stream :
				full_response += chunk.choices[0].delta.content
			return full_response
		except Exception as e:
			return "Error occurred while getting response"



def main():
	chain= Modelschain()

if __name__ == "__main__":
	main()