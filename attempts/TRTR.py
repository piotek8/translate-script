import os
import openai
import concurrent.futures
from dotenv import load_dotenv
from app.constants import INPUT_PATH, OUTPUT_PATH
from app.prompts import TRANSLATE_BUSINESS_PROMPT

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Translator:
    def __init__(self, api_key, input_dir, output_dir):
        openai.api_key = api_key
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def divide_text(self, text, chunk_size=1000):
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        return chunks

    def translate_text(self, chunk):
        prompt = f"{TRANSLATE_BUSINESS_PROMPT}\n\n{chunk}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=2000,
            temperature=1,
        )
        return response['choices'][0]['message']['content']

    def process_file(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        chunks = self.divide_text(text)

        translated_chunks = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            translated_chunks = list(executor.map(self.translate_text, chunks))

        translated_text = "".join(translated_chunks)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_text)

    def translate_files(self):
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".md"):
                input_path = os.path.join(self.input_dir, filename)
                output_path = os.path.join(self.output_dir, f"{filename[:-3]}_en.md")
                self.process_file(input_path, output_path)

translator = Translator(api_key, INPUT_PATH, OUTPUT_PATH)
translator.translate_files()
