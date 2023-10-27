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
            ]
        )
        return response['choices'][0]['message']['content']


def check_text(text):
    return text.count("```") % 2 == 0


def read_markdown():
    translator = Translator()
    files = os.listdir(INPUT_PATH)
    whole_file = ""  # Inicjalizuje zmienną whole_file jako pusty string, który będzie przechowywał wynik tłumaczeń.

    for one_file in files:
        input_file_path = os.path.join(INPUT_PATH,one_file)  # tworzy sciezke do pliku wejsciowego, czyli nasz katalog + file= sciezka konkretnego pliku
        print("Markdown file found. Reading...")

        with open(input_file_path, 'r', encoding='utf-8') as file:
            print("Opened file")
            while True: #for line in file: c
                lines = [file.readline() for _ in range(50)]
                text = ''.join(lines) # łączy po 50 linijek w text
                # ['line1\n', 'line2\n', 'line3\n'], to text będzie miało wartość 'line1\nline2\nline3\n'.
                print(lines)
                if not lines or ("" in lines and lines[1] == ""):
                    response = translator.translate_text(text)
                    whole_file += response
                if "" not in lines:
                    is_newline_and_not_splitted = text.count("```") % 2 == 0 and (lines[-1] in {"\n", ""})
                    print(f"Line is not splitted? {is_newline_and_not_splitted}")
                    while not is_newline_and_not_splitted:
                        print("reading next line")
                        next_line = file.readline()
                        text += next_line
                        is_newline_and_not_splitted = text.count("```") % 2 == 0
                        print(f"Line is not splitted? {is_newline_and_not_splitted}")
                    response = translator.translate_text(text)
                    whole_file += response
        output_file_path = os.path.join(OUTPUT_PATH, f"{one_file[:-3]}_en.md")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(whole_file)
    return whole_file


if __name__ == "__main__":
    read_markdown()
