# Curso básico de programação com Python da Bastter.com

## Exercícios D12

### Ex. 1:

Dada a string abaixo, do Silvio Santos Ipsum
    
    'Silvio Santos Ipsum Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você vai gerar textuans ha haae. Mah você mora com o papai ou com a mamãem? Ha haeeee. Hi hi. Valendo um milhão de reaisammm. Mah é a porta da esperançaam. É com você Lombardiam. Ma você, topa ou não topamm. Ma tem ou não tem o celular do milhãouamm? É com você Lombardiam. Valendo um milhão de reaisammm. O arriscam tuduam, valendo um milhão de reaisuam. Ma quem quer dinheiroam? Ma vai pra lá.'

Crie um programa que vai contar a frequência dos caracteres de cada letra. O programa deve finalizar retornando um dicionário com a frequência de cada letra, ordenado do maior para o menor

Resultado esperado:

    {'a': 55, 'm': 51, 'o': 39, 'e': 30, 'i': 25, 'u': 17, 'r': 17, 's': 15, 'l': 15, 't': 13, 'h': 13, 'v': 12, 'n': 12, 'c': 12, 'd': 12, 'p': 9, 'b': 2, 'q': 2, 'g': 1, 'x': 1}
    
### Ex. 2:

Crie um programa que vai simular as jogadas de um dado. Jogue esse dado 100 vezes e armazene os resultados. 

Conte a frequência de jogadas de cada rodada de 100 vezes. Imprima na tela o resultado.

Resultado esperado (os números podem variar de acordo com as jogadas do dado):

    O número 1 foi obtido 12 vezes.
    O número 2 foi obtido 19 vezes.
    O número 3 foi obtido 22 vezes.
    O número 4 foi obtido 15 vezes.
    O número 5 foi obtido 16 vezes.
    O número 6 foi obtido 16 vezes.

### Ex. 3:

Crie um programa que vai trabalhar com uma base de dados de médias de temperaturas em uma cidade. Exemplo:

    temperatura_sp_max = {
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

O programa deve ler essa base de dados, calcular a média de temperatura anual e ter como output o seguinte:

    Meses com temperaturas máximas acima da média em São Paulo: 
    Janeiro 27,3 ºC
    Fevereiro 28 ºC
    Março 27,2 ºC
    Abril 25,1 ºC
    Novembro 25,9 ºC
    Dezembro 26,3 ºC

    Meses com temperaturas máximas abaixo da média em São Paulo: 
    Maio 23 ºC
    Junho 21,8 ºC
    Julho 21,8 ºC
    Agosto 23,3 ºC
    Setembro 23,9 ºC
    Outubro 24,8 ºC
