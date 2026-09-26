#!/usr/bin/env python3

from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, jsonify, request

app = Flask(__name__)


class ModelUse:

    def __init__(self) -> None:
        
        self.model_name = "Qwen/Qwen3-0.6B"

        self.tokenizer, self.model = self.load_model()
        self.messages = []

    def load_model(self):

        tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        model = AutoModelForCausalLM.from_pretrained(
                self.model_name,
                torch_dtype="auto",
                device_map="auto"
                )
        
        return tokenizer, model

    def prepare_model_input(self):
       
        prompt = self.get_prompt()
        
        self.messages.append({"role": "user", "content": prompt})
        
        text = self.tokenizer.apply_chat_template(
                self.messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
                )
        
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=32768
                )

        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

        return output_ids

    def content_parsing(self, output_ids):

    
        try:
        # rindex finding 151668 (</think>)
            index = len(output_ids) - output_ids[::-1].index(151668)
        except ValueError:
            index = 0

        # thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
        content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")
        self.messages.append({"role": "assistant", "content": content})
        return content


    def get_prompt(self):

        data = request.get_json()
        prompt = data['prompt']
        
        return prompt


model = ModelUse()

@app.post('/ask')
def ask_prompt():

    output_ids = model.prepare_model_input()    
    content = model.content_parsing(output_ids=output_ids)
    return jsonify({'content': content})


