import os
import openai

openai.api_key = ""


def divide_text(text, chunk_size=1000):
  chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
  return chunks

def translate_text(chunk):

  prompt = f"""
  Take a deep breath and focus. Please translate the text below from polish into english. PRESERVE MARKDOWN FORMATTING and STYLE of the author the best you can.  

  {chunk}
  """

  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=2000
  )

  return response.choices[0].text.strip()

def process_file(input_path, output_path):

  with open(input_path, 'r', encoding='utf-8') as f:
    text = f.read()

  chunks = divide_text(text)

  translated_chunks = []
  for i in range(len(chunks)):

    # Sprawdź czy ostatni chunk nie jest za krótki
    if i == len(chunks)-1 and len(chunks[i]) < 200:
      # Połącz ostatni chunk z poprzednim
      chunks[i-1] += chunks[i]

    translated = translate_text(chunks[i])
    translated_chunks.append(translated)

  translated_text = "".join(translated_chunks)

  with open(output_path, 'w', encoding='utf-8') as f:
    f.write(translated_text)



# Ścieżki do katalogów
input_dir = r"C:\Users\Gaming\Desktop\try\basic_files"
output_dir = r"C:\Users\Gaming\Desktop\try\translated_files"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"translated_{filename}")

        process_file(input_path, output_path)

print("Gotowe!")