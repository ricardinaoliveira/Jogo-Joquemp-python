import pygame
import random
pygame.init()
tela_do_jogo = pygame.display.set_mode((500,500))
pygame.display.set_caption("Jogo Joquempô")

#variaveis contantes/página inicial
pagina_atual = "inicial"
tela_aberta = True
escolha_jogador = None 
empate = 0
vitoria = 0
derrota = 0
resultado = None
imagem_fundo = pygame.image.load("img/imagemfundo.png")
botao1 = pygame.image.load("img/botão.png")
botao_sombra = pygame.image.load("img/botao_sombra.png")
botao_jogar_rect= botao1.get_rect(topleft=(95, 325)) 
botao2 = pygame.image.load("img/botão.png")
botao_desafio_rect = botao2.get_rect(topleft=(260,325)) 

tipo_fonte = pygame.font.Font(None,24)
cor_texto = (0,0,0)
texto_botao1 = tipo_fonte.render("Jogar", True, cor_texto)
texto_botao2 = tipo_fonte.render("Desafio", True,cor_texto)

#variaveis constantes da segunda página
tela_aberta_jogo = True
img_fundo_jogo = pygame.image.load("img/pagina_jogo.png")
img_papel = pygame.image.load("img/PAPEL.png")
img_tesoura = pygame.image.load("img/tesoura.png")
img_pedra = pygame.image.load("img/PEDRA.png")
img_botao_pag_jogo = pygame.image.load("img/botao_pagina_jogo.png")
img_retangulo1 = pygame.image.load("img/retangulo.png")
img_retangulo2 = pygame.image.load("img/retangulo.png")
img_retangulo3 = pygame.image.load("img/retangulo.png")
retangulo_pedra_rect = img_retangulo1.get_rect(topleft=(342,360))
retangulo_papel_rect = img_retangulo2.get_rect(topleft=(244,360))
retangulo_tesoura_rect = img_retangulo3.get_rect(topleft=(140,360))
botao_pag_jogo_rect= img_botao_pag_jogo.get_rect(topleft=(180,280))
texto_pag_jogo_botao = tipo_fonte.render("Jogar", True,cor_texto)
animacao_img_maquina = [img_papel,img_pedra,img_tesoura]
indice = 0
#variaveis constantes da terceira página
img_fundo_pag_resultado = pygame.image.load("img/pag_resultado_jogo.png")
img_botao_resultado = pygame.image.load("img/Botao_pg_resul.png")
botao_pagina_resul_rect = img_botao_resultado.get_rect(topleft=(330,150))
texto_Empate = tipo_fonte.render("Empate!",True,cor_texto)
texto_vitória = tipo_fonte.render("Ganhou!!!",True,cor_texto)
texto_derrota = tipo_fonte.render("Perdeu!",True,cor_texto)
texto_bto_nv_jogo= tipo_fonte.render("Jogar", True, cor_texto)
# Função para chamar/cena a página inicial, desenhando os elementos.
def pagina_inicial():
    tela_do_jogo.blit(imagem_fundo,(0,0))
    tela_do_jogo.blit(botao1,botao_desafio_rect)
    tela_do_jogo.blit(botao2,botao_jogar_rect)
    tela_do_jogo.blit(texto_botao1,(152,342))
    tela_do_jogo.blit(texto_botao2,(310,342))
# Função para chamar/cena a página jogo, desenhando os elementos.    
def pagina_jogo():
    global indice
    tela_do_jogo.blit(img_fundo_jogo,(0,0))
    tela_do_jogo.blit(img_botao_pag_jogo,botao_pag_jogo_rect)
    tela_do_jogo.blit(texto_pag_jogo_botao,(233,298))
    tela_do_jogo.blit(img_retangulo1,retangulo_tesoura_rect)
    tela_do_jogo.blit(img_retangulo2,retangulo_papel_rect)
    tela_do_jogo.blit(img_retangulo3,retangulo_pedra_rect)
    tela_do_jogo.blit(img_tesoura,(143,371))
    tela_do_jogo.blit(img_papel,(248,371))
    tela_do_jogo.blit(img_pedra,(345,359))
    tela_do_jogo.blit(animacao_img_maquina[indice],(350,170)) 
    indice = (indice + 2) % len(animacao_img_maquina)
    global escolha_jogador
    if escolha_jogador == "tesoura":           
        tela_do_jogo.blit(img_tesoura,(90,175))           
    elif escolha_jogador =="papel":
      tela_do_jogo.blit(img_papel,(90,175))
    elif escolha_jogador == "pedra":
      tela_do_jogo.blit(img_pedra,(90,160)) 

# Função para chamar cena da página jogo, desenhando os elementos    
def pag_resultado_jogo():
    tela_do_jogo.blit(img_fundo_pag_resultado,(0,0))
    tela_do_jogo.blit(img_botao_resultado, botao_pagina_resul_rect)
    total_empate = tipo_fonte.render(str(empate),True,cor_texto)
    total_derrota = tipo_fonte.render(str(vitoria),True,cor_texto)
    total_vitoria = tipo_fonte.render(str(derrota),True,cor_texto)
    tela_do_jogo.blit(total_derrota,(88,370))
    tela_do_jogo.blit(total_vitoria,(248,370))
    tela_do_jogo.blit(total_empate,(410,370))
    tela_do_jogo.blit(texto_bto_nv_jogo,(380,170))
    if resultado == "empate":
       tela_do_jogo.blit(texto_Empate,(210,175))
    elif resultado == "vitoria":
       tela_do_jogo.blit(texto_vitória,(210,175))
    else: 
       tela_do_jogo.blit(texto_derrota,(220,175))  

def resultado_jogo():
   global vitoria, empate, derrota 
   global escolha_maquina
   global resultado
   
   if escolha_jogador == escolha_maquina:
        empate += 1
        resultado = "empate"
   elif(escolha_jogador == "pedra" and escolha_maquina == "tesoura")or\
        (escolha_jogador == "tesoura" and escolha_maquina == "papel") or\
        (escolha_jogador == "papel" and escolha_maquina == "pedra"):
        vitoria += 1
        resultado = "vitoria"
   else:
        derrota += 1 
        resultado = "derrota" 
    # segundo jogo no terminal
def jogo_terminal():
    print("==============================================") 
    print("Bem vindo ao Jogo Joquempô")  
    print("==============================================") 
    texto_opcao = print("Escolha entre as opções:")
    texto_opcoes = print("[1]Papel \n[2]pedra \n[3]tesoura")
    escolhamaquina = random.choice([1,2,3])
    papel = 1
    tesoura = 2
    pedra = 3
    vitoriajogo = 0
    derrotajogo = 0
    empatejogo = 0
    while True:
        escolhajogador = int(input("Determine a sua escolha: "))
        print("==============================================") 
        if escolhajogador == escolhamaquina:
            print("Empatou!")
            empatejogo += 1
            print(f"Você escolheu: {escolhamaquina}")
            print(f"Escolha da máquina:{escolhamaquina}")
        elif escolhajogador == 3 and escolhamaquina == 2:
            print("Você ganhou!!Parabéns.")
            vitoriajogo +=1
            print(f"Você escolheu: {escolhamaquina}")
            print(f"Escolha da máquina:{escolhamaquina}")
        elif  escolhajogador == 2 and escolhamaquina == 1:
            print("Você ganhou!!!Parabéns.")
            vitoriajogo +=1
            print(f"Você escolheu: {escolhamaquina}")
            print(f"Escolha da máquina:{escolhamaquina}")
        elif escolhajogador == 1  and escolhamaquina == 3:
            print("Você ganhou!!Parabéns.")
            vitoriajogo +=1 
            print(f"Você escolheu: {escolhamaquina}")
            print(f"Escolha da máquina:{escolhamaquina}") 
        elif escolhajogador not in [1,2,3]:
            print("Escolha uma das opções válidas!")
    
        else:
            derrotajogo += 1
            print("você perdeu!")
            print(f"Você escolheu: {escolhamaquina}")
            print(f"Escolha da máquina:{escolhamaquina}")
        novojogo = input("Deseja jogar novamente? sim[S] ou não[N]")
        if novojogo !="S":
          break
    print("==============================================") 
    print("Placar do Jogo")
    print("==============================================") 
    print("Total de vitórias: ", vitoriajogo)
    print("Total de Empate: ", empatejogo)
    print("Total de Derrota: ", derrotajogo)
    print("==============================================") 
# loop para tela ficar aberta e finaliza direcionando para as páginas. 
while tela_aberta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            tela_aberta = False
            pygame.quit()
            jogo_terminal()           
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicaoclick = evento.pos
            if pagina_atual == "inicial":
               if botao_jogar_rect.collidepoint(posicaoclick) or botao_desafio_rect.collidepoint(posicaoclick):
                   pagina_atual ="jogar"
            elif pagina_atual == "jogar":
               if botao_pag_jogo_rect.collidepoint(posicaoclick):
                   pagina_atual = "resultado"
               if retangulo_papel_rect.collidepoint(posicaoclick):
                   escolha_jogador ="papel" 
               elif retangulo_pedra_rect.collidepoint(posicaoclick):
                    escolha_jogador ="pedra"    
               elif retangulo_tesoura_rect.collidepoint(posicaoclick):
                    escolha_jogador ="tesoura"  
               elif botao_pag_jogo_rect.collidepoint(posicaoclick):
                    escolha_maquina = random.choice(["pedra","papel","tesoura"])  
                    resultado_jogo()
                    pagina_atual = "resultado"
            elif pagina_atual == "resultado":
                if botao_pagina_resul_rect.collidepoint(posicaoclick):
                    pagina_atual = "jogar"
                   
    if pagina_atual == 'inicial':
        pagina_inicial()
    elif pagina_atual == "jogar":
       pagina_jogo()
    elif pagina_atual == "resultado":
       pag_resultado_jogo()
    pygame.display.update()
   




   

   




    
 