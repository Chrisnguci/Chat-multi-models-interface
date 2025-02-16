from models import ModelChain
import gradio as gr

DEEPSEEK_MODEL = "deepseek/deepseek-r1:free"
GEMINI_MODEL = "google/gemini-2.0-flash-exp:free"
QWEN_MODEL="qwen/qwen2.5-vl-72b-instruct:free"

def get_models_response(models,user_input,system_prompt):
    if len(models) >1:
        return "Currently Unsupported"
    else:
        print(f"Reponse using model {models}")
        chain = ModelChain()
        if models[0]=="deepseek-r1":
            return chain.get_model_response(DEEPSEEK_MODEL,user_input,system_prompt)
        elif models[0]=="gemini-2.0-flash-exp":
            return chain.get_model_response(GEMINI_MODEL,user_input,system_prompt)
        elif models[0]=="qwen2.5-vl-72b-instruct":
            return chain.get_model_response(QWEN_MODEL,user_input,system_prompt)
        else:
            return "Current Unsupported"

def main():
	view = gr.Interface(
		fn= get_models_response,
        inputs = [gr.CheckboxGroup(["gemini-2.0-flash-exp","deepseek-r1","qwen2.5-vl-72b-instruct"], label = "Response model", value = "deepseek-r1"),gr.Textbox(label = "Your input",lines = 10, placeholder = "Nhập nội dung"), gr.Textbox(label = "Nhiệm vụ của Bot", placeholder = "Vd: bạn là một chuyên gia thương mại điện tử 10 năm kinh nghiệm hãy giúp tôi trả lời các câu hỏi sau")], 
        outputs = gr.Textbox(label ="Output", lines = 26),
        flagging_mode = "never",
        stop_btn = gr.Button("Stop",variant = "stop",visible = True),
    ).launch(share = True)

if __name__ == '__main__':
    main()



