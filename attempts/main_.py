import os
import shutil
from dotenv import load_dotenv
import openai
from app.constants import INPUT_PATH, OUTPUT_PATH

from core.logs import logger

load_dotenv()

openai.api_key = ""
input_path = "C:\\Users\\Gaming\\Desktop\\try\\basic_files"
output_path = "C:\\Users\\Gaming\\Desktop\\try\\translated_files"


def translate_text(text):
    prompt = f"""
Take a deep breath and focus. Please translate the text below from polish into english. PRESERVE MARKDOWN FORMATTING and STYLE of the author the best you can.

{text}

Translated text:
"""


    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()


def process_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        text = input_file.read()

    translated_text = translate_text(text)

    with open(output_path, 'w') as output_file:
        output_file.write(translated_text)

    logger.info(f"Translated {input_path} to {output_path}")


def translate_directory():
    for filename in os.listdir(INPUT_PATH):
        if filename.endswith(".md"):
            input_path = os.path.join(INPUT_PATH, filename)
            output_path = os.path.join(OUTPUT_PATH, filename.replace(".md", "_en.md"))

            process_file(input_path, output_path)


translate_directory()