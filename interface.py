from models import ModelChain
import gradio as gr


DEEPSEEK_R1_MODEL = "deepseek/deepseek-r1:free"
GEMINI_2ZERO_MODEL = "google/gemini-2.0-flash-exp:free"
QWEN_MODEL="qwen/qwen2.5-vl-72b-instruct:free"
DOLPHIN_MODEL = "cognitivecomputations/dolphin3.0-r1-mistral-24b:free"
MISTRAL_MODEL = "mistralai/mistral-small-24b-instruct-2501:free"
ROGUE_MODEL = "sophosympatheia/rogue-rose-103b-v0.2:free"
DEEPSEEK_V3_MODEL = "deepseek/deepseek-chat:free"
META_LLAMA_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
GEMINI_1DOT5_MODEL="google/gemini-flash-1.5-8b"
MYTHOMAX_L2_13B_MODEL ="gryphe/mythomax-l2-13b"

def get_models_response(models,user_input,system_prompt):
    if len(models) >1:
        return "Currently Unsupported"
    else:
        print(f"Reponse using model {models}")
        chain = ModelChain()
        if models[0]=="deepseek-r1":
            return chain.get_model_response(DEEPSEEK_R1_MODEL,user_input,system_prompt)
        elif models[0]=="gemini-2.0-flash-exp":
            return chain.get_model_response(GEMINI_2ZERO_MODEL,user_input,system_prompt)
        elif models[0]=="qwen2.5-vl-72b-instruct":
            return chain.get_model_response(QWEN_MODEL,user_input,system_prompt)
        elif models[0] =="dolphin3.0-r1-mistral-24b":
            return chain.get_model_response(DOLPHIN_MODEL,user_input,system_prompt)
        elif models[0] == "mistral-small-24b-instruct-2501":
            return chain.get_model_response(MISTRAL_MODEL,user_input,system_prompt)
        elif models[0] == "rogue-rose-103b-v0.2":
            return chain.get_model_response(ROGUE_MODEL,user_input,system_prompt)
        elif models[0] == "deepseek-chat":
            return chain.get_model_response(DEEPSEEK_V3_MODEL,user_input,system_prompt)
        elif models[0] == "llama-3.3-70b-instruct":
            return chain.get_model_response(META_LLAMA_MODEL,user_input,system_prompt)
        elif models[0] == "gemini-flash-1.5-8b":
            return chain.get_model_response(GEMINI_1DOT5_MODEL,user_input,system_prompt)
        elif models[0] == "mythomax-l2-13b":
            return chain.get_model_response(MYTHOMAX_L2_13B_MODEL,user_input,system_prompt)
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



