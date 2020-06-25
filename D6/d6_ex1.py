alunos = ['Ana', 'Beatriz', 'Cĺáudio', 'Daniela', 'Eduarda']

def checa_se_presente_ou_faltou(presente_ou_faltou):
    if presente_ou_faltou == 'presente':
        print(f"{aluno} - presente!")
    elif presente_ou_faltou == 'faltou':
        print(f'{aluno} - faltou!')
    else:
        print('Algo deu errado.')

for aluno in alunos:
    print(f"{aluno}!")
    presente_ou_faltou = input("Digite 'presente' se aluno estiver presente e 'faltou' se o aluno tiver faltado: ")
    checa_se_presente_ou_faltou(presente_ou_faltou)

