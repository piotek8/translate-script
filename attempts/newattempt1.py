import os
import openai

openai.api_key = ""
INPUT_PATH = "C:\\Users\\Gaming\\Desktop\\try\\basic_files"
OUTPUT_PATH = "C:\\Users\\Gaming\\Desktop\\try\\translated_files"


def translate_text(text):
    prompt = f"""
    Take a deep breath and focus. Please translate the text below from polish into english. PRESERVE MARKDOWN FORMATTING and STYLE of the author the best you can.

    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        prompt=prompt,
        max_tokens=500,
        temperature= 1.0
    )
    return response.choices[0].text.strip()


def process_file(file_name):
    with open(os.path.join(INPUT_PATH, file_name), 'r', encoding='utf-8') as file:
        content = file.read()
        chunks = [content[i:i + 500] for i in range(0, len(content), 500)]
        translated_chunks = [translate_text(chunk) for chunk in chunks]
        return ' '.join(translated_chunks)


def main():
    for file_name in os.listdir(INPUT_PATH):
        if os.path.isfile(os.path.join(INPUT_PATH, file_name)):
            translated_content = process_file(file_name)
            output_file_name = file_name.replace(".txt", "_en.txt")
            with open(os.path.join(OUTPUT_PATH, output_file_name), 'w', encoding='utf-8') as output_file:
                output_file.write(translated_content)


if __name__ == "__main__":
    main()
