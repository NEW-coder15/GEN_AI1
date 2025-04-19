import translate
from translate import Translator
translator=Translator(to_lang='hi')
# Text to be translated
text = 'Hello, who the hell are you?'
# Perform the translation
translation = translator.translate(text)

# Print the translated text
print('Translated Text:', translation)