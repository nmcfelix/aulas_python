from deep_translator import GoogleTranslator

try:
    with open('test.txt') as f:
        texto = f.read()
        translated = GoogleTranslator(
            source='auto', target='en').translate(texto)
        with open('test.txt', 'a') as f:
            f.write('\n' + translated)
except FileNotFoundError:
    print('Não encontrado')
