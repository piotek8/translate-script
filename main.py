from app.services import Translator

if __name__ == "__main__":
    translator = Translator()
    translator.process_all_files()