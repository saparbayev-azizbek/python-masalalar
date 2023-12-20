from googletrans import Translator

tarjimon = Translator()

xabar = "Tarjima uchun matn kiriting "
xabar += "(chiqib ketish uchun 'x' belgisini bosing) \n>>> "

while True:
    matn = input(xabar)
    if matn == 'x':
        break;
    else:
        tarjima = tarjimon.translate(matn, src = 'uz', dest = 'en')
        print(tarjima.text.lower())
        print()