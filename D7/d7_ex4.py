silvio = """
Silvio Santos Ipsum Ma tem ou não tem o celular do milhãouamm? Um, dois três, quatro, PIM, entendeuam? Mah ooooee vem pra cá. Vem pra cá. Ma quem quer dinheiroam? Ma não existem mulher feiam, existem mulher que não conhece os produtos Jequitiamm. Mah roda a roduamm. É bom ou não éam?

É por sua conta e riscoamm? Mah é a porta da esperançaam. Mah ooooee vem pra cá. Vem pra cá. Eu não queria perguntar isso publicamente, ma vou perguntar. Carla, você tem o ensino fundamentauam? Boca sujuam... sem vergonhuamm. Ma você, topa ou não topamm.

Mah você mora com o papai ou com a mamãem? Ma o Silvio Santos Ipsum é muitoam interesanteam. Com ele ma você vai gerar textuans ha haae. É namoro ou amizadeemm? Ma! Ao adquirir o carnê do Baú, você estará concorrendo a um prêmio de cem mil reaisam. Estamos em ritmo de festamm. Patríciaaammmm... Luiz Ricardouaaammmmmm.

Mah você mora com o papai ou com a mamãem? É bom ou não éam? Eu só acreditoammmm.... Vendoammmm. Mah você não consegue né Moisés? Você não consegueam. Ma vejam só, vejam só. Patríciaaammmm... Luiz Ricardouaaammmmmm.

Mah é a porta da esperançaam. Ma vejam só, vejam só. Valendo um milhão de reaisammm. Ma você, topa ou não topamm. Patríciaaammmm... Luiz Ricardouaaammmmmm. Ma não existem mulher feiam, existem mulher que não conhece os produtos Jequitiamm.
"""

contador_mah = 0
for palavra in silvio.split(' '):
    if palavra in ["Ma", "Mah", "Ma!"]:
        contador_mah += 1

print(f'O Silvio disse "Mah" ou "Ma" {contador_mah} vezes.')