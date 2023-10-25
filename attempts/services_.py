import os
import shutil
from dotenv import load_dotenv
import openai
from app.constants import INPUT_PATH, OUTPUT_PATH
from app.prompts import TRANSLATE_BUSINESS_PROMPT

from core.logs import logger

load_dotenv()

class Translator:
    def __init__(self):
        #openai.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = ""

    def read_md_files(self):
        if not os.path.exists(INPUT_PATH):
            raise Exception(f"The input path '{INPUT_PATH}' does not exist.")

        md_files = []
        for file in os.listdir(INPUT_PATH):
            if file.endswith(".md"):
                md_files.append(file)

        return md_files

    def save_md_files(self, md_files):
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)

        for file in md_files:
            input_file = os.path.join(INPUT_PATH, file)
            output_filename = file[:-3] + "_en.md"
            output_file = os.path.join(OUTPUT_PATH, output_filename)

            if os.path.exists(output_file):
                continue

            try:
                shutil.copy(input_file, output_file)
                logger.info(f"Translated '{file}' to '{output_filename}' in '{OUTPUT_PATH}'")
            except Exception as e:
                logger.error(f"Failed to translate '{file}': {str(e)}")

#   def translate_text(self, text):
#       prompt = f"""{TRANSLATE_BUSINESS_PROMPT}\n{text}\n"""
#       response = openai.ChatCompletion.create(
#           model="davinci",
#           prompt=prompt,
#           max_tokens=100,
#           stop=["\n"]
#       )
#       return response.choices[0].text.strip()

    def translate_text(self, text):
        prompt = f"""
Take a deep breath and focus. Please translate the text below from polish into english. PRESERVE MARKDOWN FORMATTING and STYLE of the author the best you can.
"""
       # prompt = f"""{TRANSLATE_BUSINESS_PROMPT}\n{text}\n"""
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100,
            stop=["\n"]
        )
        return response.choices[0].text.strip()



    def split_text(self, text, max_length=4000):
        chunks = []
        current_chunk = ""
        code_block = False
        for line in text.split('\n'):
            if "```" in line:
                code_block = not code_block
            if len(current_chunk) + len(line) <= max_length and not code_block:
                current_chunk += line + '\n'
            else:
                chunks.append(current_chunk)
                current_chunk = line + '\n'
        chunks.append(current_chunk)
        return chunks

    def process_md_file(self, input_path):
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        chunks = self.split_text(text)

        translated_text = ""
        for chunk in chunks:
            print(chunk)
            try:
                translated_chunk = self.translate_text(chunk)
                print(translated_chunk)
                translated_text += translated_chunk
            except Exception as e:
                raise Exception(f"Translation failed. Error: {str(e)}")

        return translated_text

    def translate_directory(self):
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)

        for filename in os.listdir(INPUT_PATH):
            if filename.endswith(".md"):
                input_path = os.path.join(INPUT_PATH, filename)
                output_path = os.path.join(OUTPUT_PATH, filename.replace('.md', '_en.md'))

                try:
                    translated_text = self.process_md_file(input_path)

                    with open(output_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(translated_text)
                        logger.info(f"Translated '{filename}' to '{output_path}'")
                except Exception as e:
                    logger.error(f"Translation failed for '{filename}': {str(e)}")



if __name__ == "__main__":
    translator = Translator()
    translator.translate_directory()