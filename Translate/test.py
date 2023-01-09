from translate import Translator

src = input("Enter a language of your text: ")
dest = input("Enter a language you want to translate to: ")
text = input("Enter text: ")


def translate_text(src, text, dest):
    try:
        ts = Translator(from_lang=src, to_lang=dest)
        translation = ts.translate(text)
        print(translation)

    except TypeError:
        print("TypeError")

    except:
        print("An error occurred")


translate_text(src, text, dest)