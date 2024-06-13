from translate import Translator

def translate(language, text):
    translator = Translator(to_lang=language)
    return translator.translate(text)