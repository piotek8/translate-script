import os
from dotenv import load_dotenv
import openai
from app.constants import INPUT_PATH
from app.constants import OUTPUT_PATH
from app.prompts import TRANSLATE_BUSINESS_PROMPT

load_dotenv()


def check_text(text):
    return text.count("```") % 2 == 0


class Translator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def translate_text(self, input_text):
        prompt = TRANSLATE_BUSINESS_PROMPT.format(input_text=input_text)
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
            ]
        )
        return response['choices'][0]['message']['content']


class FileTranslator:
    def __init__(self, translator):
        self.translator = translator

    def read_markdown(self, input_file_path):
        print("Markdown file found. Reading...")
        whole_file = ""
        with open(input_file_path, 'r', encoding='utf-8') as file:
            print("Opened file")
            while True:
                lines = []
                for _ in range(50):
                    line = file.readline()
                    lines.append(line)
                text = ''.join(lines)
                print(lines)
                if not lines or ("" in lines and lines[1] == ""):
                    response = self.translator.translate_text(text)
                if "" not in lines:
                    is_newline_and_not_splitted = text.count("```") % 2 == 0 and (lines[-1] in {"\n", ""})
                    print(f"Line is not splitted? {is_newline_and_not_splitted}")
                    while not is_newline_and_not_splitted:
                        print("reading next line")
                        next_line = file.readline()
                        text += next_line
                        is_newline_and_not_splitted = check_text(text)
                        print(f"Line is not splitted? {is_newline_and_not_splitted}")
                    response = self.translator.translate_text(text)
                whole_file += response
        return whole_file

    def translate_file(self, input_file_path, output_file_path):
        translated_text = []
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            while True:
                lines_info = self.read_markdown(input_file)
                if not lines_info:
                    break

                for lines in lines_info:
                    chunk = ''.join(lines)
                    translation = self.translator.translate_text(chunk)
                    translated_text.append(translation)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(''.join(translated_text))


def main():
    translator = Translator()

    files = os.listdir(INPUT_PATH)

    for file in files:
        input_file_path = os.path.join(INPUT_PATH, file)
        output_file_path = os.path.join(OUTPUT_PATH, f"{file[:-3]}_en.md")

        file_translator = FileTranslator(translator)
        file_translator.translate_file(input_file_path, output_file_path)

