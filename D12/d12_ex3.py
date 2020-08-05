from statistics import mean


temperaturas_sp_max = {
    'Janeiro': 27.3,
    'Fevereiro': 28,
    'Março': 27.2,
    'Abril': 25.1,
    'Maio': 23,
    'Junho': 21.8,
    'Julho': 21.8,
    'Agosto': 23.3,
    'Setembro': 23.9,
    'Outubro': 24.8,
    'Novembro': 25.9,
    'Dezembro': 26.3,
}

media_temperaturas = mean(temperaturas_sp_max.values())

meses_acima_maxima = dict()

meses_abaixo_maxima = dict()

for key, value in temperaturas_sp_max.items():
    if value < media_temperaturas:
        meses_abaixo_maxima[key] = value
    else:
        meses_acima_maxima[key] = value

print("Meses com temperaturas máximas acima da média em São Paulo: ")
for key, value in meses_acima_maxima.items():
    print(key, str(value).replace('.', ',') + ' ºC')

print("\nMeses com temperaturas máximas abaixo da média em São Paulo: ")
for key, value in meses_abaixo_maxima.items():
    print(key, str(value).replace('.', ',') + ' ºC')