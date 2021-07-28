
from googletrans import Translator
from pprint import pprint

a = '3.1.0a0'

translator = Translator()

def tarjima_qil(txt, til1='auto', til2='uz'):
    lang = translator.detect(txt).lang
    tarj = ''
    a = len(txt.split())
    if a < 2:
        data = translator.translate(txt, dest=til2, src=til1).extra_data
        data1 = data['all-translations']
        if data1:
            data2 = data1[0][1]
            for soz in data2[:4]:
                tarj += f"{soz}\n"
        else:
           tarj = translator.translate(txt, dest=til2, src=til1).text
    elif til1 == 'auto':
        tarj = translator.translate(txt, dest=til2, src=til1).text
    else:
        if lang == til1:
            tarj = translator.translate(txt, dest=til2, src=til1).text
        elif lang == til2:
            tarj = translator.translate(txt, dest=til1, src=til2).text
        else:
            tarj = translator.translate(txt, dest=til2, src='auto').text

    return tarj

if __name__ == '__main__':
    print(translator.translate('human', dest='en', src='auto').text)
    print(tarjima_qil('I am a programmer'))
    print(translator.detect('nok'))
    data = translator.translate('odam', dest='en', src='uz').extra_data
    data1 = data['all-translations']
    if data1:
        print(1)
    else:
        print(2)
    pprint(data1)


