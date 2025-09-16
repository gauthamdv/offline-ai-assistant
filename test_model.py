from llama_cpp import Llama

# Load the model
llm = Llama(model_path="models/mistral-7b-instruct-v0.2.Q5_K_M.gguf", n_ctx=2048)

# Test prompt
prompt = "You are a helpful AI assistant. Answer in one sentence: What is the capital of France?"

output = llm(prompt, max_tokens=50, stop=["</s>"])
print(output["choices"][0]["text"])

