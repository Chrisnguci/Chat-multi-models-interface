from models import ModelChain
import gradio as gr

def get_gemini_response(models,user_input, system_prompt):
    if models != "gemini-1.5-flash":
        return "Currently Unsupported"
    else:
    	print(f"bạn đang sử dụng Model {models}")
    	chain= ModelChain()
    	return chain.get_gemini_response(user_input, system_prompt)

def main():
	view = gr.Interface(
		fn= get_gemini_response,
        inputs = [ gr.Dropdown(["o3-mini","gemini-1.5-flash","claude-3-5-sonnet-20241022"], label = "Response model", value = "gemini-1.5-flash"),gr.Textbox(label = "Your input",lines = 10, placeholder = "Nhập nội dung"), gr.Textbox(label = "Nhiệm vụ của Bot", placeholder = "Vd: bạn là một chuyên gia thương mại điện tử 10 năm kinh nghiệm hãy giúp tôi trả lời các câu hỏi sau") ], 
        outputs = gr.Textbox(label ="Output", lines = 26),
        flagging_mode = "never",
        stop_btn = gr.Button("Stop",variant = "stop",visible = True),
    ).launch(share = True)

if __name__ == '__main__':
    main()