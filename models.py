
import os
import openai
from dotenv import load_dotenv
# MOELS
DEEPSEEK_MODEL = "deepseek/deepseek-r1:free"
GEMINI_MODEL = "google/gemini-2.0-flash-exp:free"
QWEN_MODEL="qwen/qwen2.5-vl-72b-instruct:free"
OPENROUTER_API_KEY="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"
load_dotenv()
class ModelChain:
	def __init__(self):
		self.client = self.generate_client(OPENROUTER_API_KEY,"https://openrouter.ai/api/v1" )
		self.deepseek_messages = []
		self.gemini_messages = []

	def generate_client(self,api_key, url):
		return openai.OpenAI(
			api_key = api_key,
			base_url = url,
			) 
	def get_model_response(self,model,user_input,system_prompt):
		messages = [{"role":"system","content": system_prompt},
					{"role":"user","content":user_input}]
		try:
			result = self.client.chat.completions.create(
				model = model,
				messages = messages,
				)
			return result.choices[0].message.content
		except Exception as e:
			return f"Error occurred while getting response{e}"
def main():
	chain= Modelschain()

if __name__ == "__main__":
	main()