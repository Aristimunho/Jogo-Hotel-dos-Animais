

print("     ░░░░░░░░░░░                ▓ ▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓       ")
print("    ░░  ░░░░░██░░               ▓ ▓ ▓ ▓  ▓  ▓   ▓       ")
print("    ░░░░░░░░░░░░░               ▓▓▓ ▓ ▓  ▓  ▓▓  ▓       ")
print("    ░░  ░░░░░  ░░               ▓ ▓ ▓ ▓  ▓  ▓   ▓       ")
print("    ░░░░░░░░░░░░░               ▓ ▓ ▓▓▓  ▓  ▓▓▓ ▓▓▓     ")
print("   ░░░██░░░░░  ░░░                      DOS             ")
print("   ░░░░░░░░░░░░░░░        ▓▓▓ ▓▓▓ ▓ ▓ ▓▓▓ ▓▓▓ ▓▓▓ ▓ ▓▓▓ ")
print("   ░░░  ░░░░░██░░░        ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓   ")
print("   ░░░░░░░░░░░░░░░        ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓▓▓ ▓ ▓ ▓ ▓ ▓▓▓ ")
print("  ░░░░  ░░░░░  ░░░░       ▓▓▓ ▓ ▓ ▓ ▓ ▓     ▓ ▓▓▓ ▓   ▓ ")
print("  ░░░░░░░░█░░░░░░░░       ▓ ▓ ▓ ▓▓▓ ▓ ▓     ▓ ▓ ▓ ▓ ▓▓▓ ")
print("________________________________________________________")
print()
print("********************* Regras ******************************")
print("*Aloque os hóspedes nos quartos disponíveis lembrando que *")
print("*        O RATO não pode ficar ao lado do GATO.           *")
print("*        O CÃO não pode ficar ao lado do OSSO.            *")
print("*        O GATO não pode ficar ao lado do CÃO.            *")
print("*       O QUEIJO não pode ficar ao lado do RATO.          *")
print("*      Os quartos indisponíveis serão marcados com █.     *")
print("*   Cada hospede será representado por sua letra inicial. *")
print("*    Os quartos estão númerados como o exemplo seguinte:  *")
print("*                      ╔═╦═╦═╦═╗                          *")
print("*                      ║1║2║3║4║                          *")
print("*                      ╠═╬═╬═╬═╣                          *")
print("*                      ║5║6║7║8║                          *")
print("*                      ╚═╩═╩═╩═╝                          *")
print("***********************************************************")
print("                      BOA SORTE!!                          ")
print()
  

print("            ----------------(Fase 1)--------------       ")
print()
print("Aqui voçê deve alocar o RATO e o GATO nos quartos possíveis")
#As strings foram colocadas em variáveis para facilitar a impressão.
l1 = "╔═╦═╦═╦═╗"
l2 = "║█║█║ ║G║"
l3 = "╠═╬═╬═╬═╣"
l4 = "║R║ ║█║█║"
l5 = "╚═╩═╩═╩═╝"
#As strings foram impressas com espaço para melhor centralizar as caixas. 
print(" "*22,l1)
print(" "*22,l2)
print(" "*22,l3)
print(" "*22,l4)
print(" "*22,l5)
print()
#O valor inteiro digitado pelo usuário é atribuido as variáveis.
rato = int(input("Em qual quarto deseja colocar o rato? "))
print()
gato = int(input("Em qual quarto deseja colocar o gato? "))
print()

#Analisa a resposta do usuário sobre oque a fase pede.
if (rato == 6 and gato == 3): 
#Se a resposta for verdadeira imprime na tela.
 print("Parabéns você conseguiu")
 print("e desbloqueou a fase seguinte")
 print()
 print("            ----------------(Fase 2)--------------       ")
 print()
 print("Nesta fase voçê deve alocar um CÃO, um OSSO e outro CÃO nos quartos possíveis")
 l1 = "╔═╦═╦═╦═╗"
 l2 = "║ ║█║█║█║"
 l3 = "╠═╬═╬═╬═╣"
 l4 = "║█║C║ ║ ║"
 l5 = "╚═╩═╩═╩═╝"
 print(" "*22,l1)
 print(" "*22,l2)
 print(" "*22,l3)
 print(" "*22,l4)
 print(" "*22,l5)
 print()
 #O valor inteiro digitado pelo usuário é atribuido as variáveis.
 cao1 = int(input("Em qual quarto quer colocar o primeiro cão? "))
 print()
 osso = int(input("Em qual quarto quer colocar o osso? "))
 print()
 cao2 = int(input("Em qual quarto quer colocar o segundo cão? "))
 print()
 #Analisa a resposta do usuário sobre oque a fase pede.
 if((osso == 1 and cao1 == 7 and cao2 == 8) or (osso == 1 and cao1 == 8 and cao2 == 7)):
 #Se a resposta for verdadeira imprime na tela.
     print("Parabéns você está pegando o jeito!")
     print("bem vindo a fase seguinte")
     print()
     print("            ----------------(Fase 3)--------------       ")
     print()
     print("Nesta fase voçê deve alocar  GATO,  OSSO e RATO. ")
     l1 = "╔═╦═╦═╦═╗"
     l2 = "║ ║█║█║█║"
     l3 = "╠═╬═╬═╬═╣"
     l4 = "║ ║G║ ║█║"
     l5 = "╚═╩═╩═╩═╝"
     print(" "*22,l1)
     print(" "*22,l2)
     print(" "*22,l3)
     print(" "*22,l4)
     print(" "*22,l5)
     print()
#O valor inteiro digitado pelo usuário é atribuido as variáveis.
     gato = int(input("Onde deseja colocar o gato? "))
     print()
     osso = int(input("Em que lugar vai colocar o osso? "))
     print()
     rato = int(input("E o rato? "))
     print()
#Analisa a resposta do usuário sobre oque a fase pede.
     if(rato == 1 and osso == 5 and gato == 7):
     #Se a resposta for verdadeira imprime na tela.
         print("Parabéns você chegou a fase FINAL!")
         print("Vamos ver se passa nessa...")
         print()
         print("            ----------------(Fase 4)--------------       ")
         print()
         print("Nesta fase voçê deve alocar  QUEIJO,  OSSO e QUEIJO. ")
         l1 = "╔═╦═╦═╦═╗"
         l2 = "║ ║ ║ ║█║"
         l3 = "╠═╬═╬═╬═╣"
         l4 = "║█║R║█║█║"
         l5 = "╚═╩═╩═╩═╝"
         print(" "*22,l1)
         print(" "*22,l2)
         print(" "*22,l3)
         print(" "*22,l4)
         print(" "*22,l5)
         print()
          #O valor inteiro digitado pelo usuário é atribuido as variáveis.
         queijo = int(input("Onde deseja colocar o primeiro queijo? "))
         print()
         osso = int(input("Em que lugar vai colocar o osso? "))
         print()
         queijo2 = int(input("E o último queijo vai? "))
         print()
         #Analisa a resposta do usuário sobre oque a fase pede.
         if((osso == 2 and queijo == 3 and queijo2 == 1) or (osso == 2 and queijo == 1 and queijo2 == 3)):
             #Se a resposta for verdadeira imprime na tela.
             print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
             print("▓PARABÉNS você VENCEU!!!▓")
             print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

# A sequência de "else" imprime na tela caso a verificação dos "if" retorne falsa.
         else:
             print("GAME OVER!!")
     else:    
         print("GAME OVER!!")
 else:
     print("GAME OVER!!")
else: 
    print("GAME OVER!!")
