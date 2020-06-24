from time import sleep

alunos = ['Ana', 'Beatriz', 'Cĺáudio', 'Daniela', 'Eduarda']

def checa_se_presente_ou_faltou(presente_ou_faltou):
    if presente_ou_faltou == 'presente':
        print(f"{aluno} - presente!")
    elif presente_ou_faltou == 'faltou':
        print(f'{aluno} - faltou!')

for aluno in alunos:
    print(f"{aluno}!")
    presente_ou_faltou = input("Digite 'presente' se aluno estiver presente e 'faltou' se o aluno tiver faltado: ")
    sleep(1.2)
    checa_se_presente_ou_faltou(presente_ou_faltou)
    while presente_ou_faltou not in ['presente', 'faltou']:
        presente_ou_faltou = input(f"Algo deu errado. \nTente novamente. \nDigite 'presente' se {aluno} estiver presente e 'faltou' se o {aluno} tiver faltado: ")
        sleep(1.2)
        checa_se_presente_ou_faltou(presente_ou_faltou)
