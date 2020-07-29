# Curso básico de programação com Python da Bastter.com

## Exercícios D11

(Enunciado): O Cadastro de pessoas físicas (CPF) é um número que precisa ser validado. Não pode ser criado um CPF como 111.111.111-11 ou um número que não passe a validação. A validação consiste em validar os dois últimos dígitos de acordo com uma regra matemática. Primeiro se pega os 9 primeiros dígitos e é feita a soma da multiplicação de cada dígito por números de 10 a 2 na ordem. Exemplo: Considerando o CPF 911.478.980-90, é feita a seguinte conta:

    9 x 10 + 1 x 9 + 1 x 8 + 4 x 7 + 7 x 6 + 8 x 5 + 9 x 4 + 8 x 3 + 0 x 2

O somatório acima deve ser multiplicado por 10 e dividido por 11
O resto da divisão deve ser igual ao primeiro dígito verificador (9)
Se o resto da divisão for 10, considera-se resto 0.
Em seguida separa-se os 10 primeiros dígitos e é feita nova soma de multiplicações, agora de 11 a 2:

    9 x 11 + 1 x 10 + 1 x 9 + 4 x 8 + 7 x 7 + 8 x 6 + 9 x 5 + 8 x 4 + 0 x 3 + 9 x 2

A soma acima deve ser multiplicada por 10 e dividida por 11
O resto da divisão deve ser igual ao segundo dígito verificador. Resto 10 considera-se resto 0.
CPFs com números iguais (111.111.111-11) passam a validação acima mas são inválidos. Invalidar CPFs assim.

(Problema): Crie uma função que vai receber cpfs nos formatos abaixo: ‘111.222.333-44’ e valide o cpf. Se o cpf for inválido, “estoure” um ValueError. Se o cpf for válido, retorne True. Se a entrada de dado já for uma entrada inválida (exemplos: ‘111.111.111-111’, ‘111-111-111-11’) retorne uma mensagem de erro dizendo que o formato não é o formato aceito. 
