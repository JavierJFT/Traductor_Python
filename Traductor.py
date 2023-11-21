#programa facilillo que usa google translator para traducir cosas, tiene un limite de 50 peticiones diarias

from translate import Translator
#hay que hacer python -m pip install translate para que coja el import bien

languajes = ['fr','it','en','ru','de']
#aqui van los lenguajes  fr es frances, it italiano , ru es rumano, en ingles, de aleman

text = input ('introduce lo que quieras traducir >>')
#text text = input ('type what you want to translate >>')

for language in languajes:
    translator = Translator(provider='libre', from_lang= "es", to_lang=language)
    translation = translator.translate(text)
    print(f'{language}: {translation}')

















