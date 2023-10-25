import os
import openai
import concurrent.futures
from dotenv import load_dotenv
from app.constants import INPUT_PATH
from app.constants import OUTPUT_PATH
from app.prompts import TRANSLATE_BUSINESS_PROMPT
from core.logs import logger


class Translator:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv('OPENAI_API_KEY')


    @staticmethod
    def divide_text(text, chunk_size=1000):
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
            max_tokens=4000,
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

        logger.info(f"File processed: {input_path}")

    def process_all_files(self):
        os.makedirs(OUTPUT_PATH, exist_ok=True)

        for filename in os.listdir(INPUT_PATH):
            if filename.endswith(".md"):
                input_path = os.path.join(INPUT_PATH, filename)
                output_path = os.path.join(OUTPUT_PATH, f"{filename[:-3]}_en.md")
                self.process_file(input_path, output_path)


translator = Translator()
translator.process_all_files()

logger.info("All files processed")
print("Ready!")
