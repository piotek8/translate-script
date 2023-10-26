import os
from dotenv import load_dotenv
import openai
from app.constants import INPUT_PATH, OUTPUT_PATH
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
            ],
            max_tokens=4000,
            temperature=1,
        )
        return response['choices'][0]['message']['content']


#def process_lines(file):
#    list_process_lines = []
#    while True:
#        lines = []
#        for one_line in range(50):
#            line = file.readline()
#            if not line:
#                break
#            lines.append(line)
#        if not lines:
#            break
#        list_process_lines.append(lines)
#    return list_process_lines

def process_lines(file):
    list_process_lines = []
    while True:
        lines = []
        count = 0  # Licznik dla znaku "```"
        for one_line in range(50):
            line = file.readline()
            if line.strip() == "```":
                count += 1
                if count % 2 != 0 and lines:  # Jeśli napotkano nieparzystą liczbę "```", zakończ blok
                    break
            if not line:
                break
            lines.append(line)
        if not lines:
            break
        list_process_lines.append(lines)
    return list_process_lines


#[
#    ['1 linijka', '2 linijka', ..., '50 linijka'],
#    ['51 linijka', '52 linijka', ..., '100 linijka'],
#    ['101 linijka', '102 linijka', ..., '150 linijka'],
#    ['151 linijka', '152 linijka', ..., '200 linijka']
#]

def main():
    translator = Translator()

    translated_text = []  # Tworzymy zmienną na przetłumaczony tekst

    with open(INPUT_PATH, 'r') as input_file:
        while True:
            lines = process_lines(input_file)
            print(lines)
            if not lines:
                break

           #translated_block = []
           #for line in lines:  # Dla każdej linii w bloku
           #    translation = translator.translate_text(line)  # Przetłumacz linię
           #    translated_text.append(translation)  # Dodaj przetłumaczona linie do listy
            for line_block in lines:  # Dla każdego bloku linii
                chunk = ''.join(line_block)
                translation = translator.translate_text(chunk)  # Przetłumacz blok linii
                translated_text.append(translation)  # Dodaj przetłumaczony blok do listy

    # Zapisz przetłumaczony tekst w odpowiednim pliku
    with open(OUTPUT_PATH, 'w') as output_file:
        output_file.write(''.join(translated_text))  # Łączymy przetłumaczone bloki

    # Zmein nazwe pliku wyjsciowego po przetlumaczeniu
    input_filename = os.path.basename(INPUT_PATH)
    output_filename = input_filename.replace(".md", "_en.md")
    os.rename(OUTPUT_PATH, os.path.join(os.path.dirname(OUTPUT_PATH), output_filename))

