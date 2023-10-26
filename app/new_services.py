import os
from dotenv import load_dotenv
import openai
from app.constants import INPUT_PATH
from app.constants import OUTPUT_PATH
from app.prompts import TRANSLATE_BUSINESS_PROMPT

load_dotenv()


class Translator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def translate_text(self, chunk):
        # TODO: do x.format{input_text=input_text}
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


def process_lines(file):
    # TODO: make it faster. maybe with generators
    list_process_lines = []
    while True:
        lines = []
        count = 0
        for one_line in range(50):
            line = file.readline()
            if line.strip() == "```":  #
                count += 1
                lines.append(line)
                if count % 2 != 0 or (one_line >= -4 and one_line <= -1):
                # TODO: move to the next line command
                    break
            elif not line or line.strip() == "\n":
                break
            else:
                lines.append(line)
        if not lines:
            break
        list_process_lines.append(lines)
    return list_process_lines


def main():
    translator = Translator()


    files = os.listdir(INPUT_PATH)


    for file in files:
        input_file_path = os.path.join(INPUT_PATH, file)
        output_file_path = os.path.join(OUTPUT_PATH, f"{file[:-3]}_en.md")

        translated_text = []
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            while True:
                lines_info = process_lines(input_file)
                if not lines_info:
                    break

                for lines in lines_info:
                    chunk = ''.join(lines)
                    translation = translator.translate_text(chunk)
                    translated_text.append(translation)

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(''.join(translated_text))
