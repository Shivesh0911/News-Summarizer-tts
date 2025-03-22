from gtts import gTTS
from googletrans import Translator

def translate_to_hindi(text):
    """Translate English text to Hindi using googletrans."""
    translator = Translator()
    try:
        # Translate the text from English to Hindi
        translation = translator.translate(text, src='en', dest='hi')
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Fallback to English if translation fails

def generate_hindi_tts(text, filename="output.mp3"):
    """Generate Hindi speech using gTTS."""
    # Translate English text to Hindi
    hindi_text = translate_to_hindi(text)
    print("Translated Text (Hindi):", hindi_text)  # Debugging

    # Generate Hindi TTS using gTTS
    try:
        tts = gTTS(text=hindi_text, lang='hi')  # Use 'hi' for Hindi language
        tts.save(filename)
        print("Audio file generated successfully:", filename)  # Debugging
        return filename
    except Exception as e:
        print(f"TTS error: {e}")
        return None
