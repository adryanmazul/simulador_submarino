def movimentacao_submarino(x, y, oxigenio, comando):
    """
    Processa a movimentação do submarino com base no comando do usuário,
    atualiza as coordenadas e deduz o oxigênio caso o movimento seja válido.
    """
    comando = comando.lower()
    
    # Variáveis temporárias para simular o movimento antes de validá-lo
    sx, sy = x, y

    match comando:
        case "w": # Cima
            sy -= 1
        case "s": # Baixo
            sy += 1
        case "a": # Esquerda
            sx -= 1
        case "d": # Direita
            sx += 1
        case _:
            # Trata inputs inválidos sem gastar oxigênio
            print("Movimentação inválida!")
            return x, y, oxigenio
    
    # Boundary checking (Validação de limites do mapa 10x10)
    if 0 <= sx <= 9 and 0 <= sy <= 9:
        oxigenio -= 1
        return sx, sy, oxigenio
    else:
        print("Aviso: Pressão perigosa nas paredes da fossa! Movimento bloqueado.")
        return x, y, oxigenio # Retorna à posição original sem gastar oxigênio

def verificar_status_oxigenio(oxigenio):
    """
    Verifica se o oxigênio está em nível crítico ou se já esgotou.
    """
    if 1 <= oxigenio <= 5:
        print(f"Oxigênio em estado crítico! Oxigênio atual: {oxigenio}")
    
    # Retorna True se ainda houver oxigênio, False se tiver acabado
    return oxigenio > 0

def mapa(sx, sy, cx, cy, oxigenio):
    """
    Renderiza o mapa bidimensional 10x10 no terminal.
    S = Submarino | C = Caixa-preta | ~ = Água
    """
    for y in range(10):
        linha = ""
        for x in range(10):
            if x == sx and y == sy:
                linha += "S " # Posição atual do submarino
            elif x == cx and y == cy:
                linha += "C " # Posição do objetivo (Caixa-preta)
            else:
                linha += "~ " # Espaço vazio
        print(linha)
    print(f"Oxigênio restante: {oxigenio}")

# --- Configurações iniciais do jogo ---
x, y = 0, 0        # Posição inicial do submarino
cx, cy = 8, 9      # Posição da caixa-preta
oxigenio = 25      # Quantidade inicial de oxigênio

# --- Loop principal do jogo ---
while True:
    mapa(x, y, cx, cy, oxigenio)

    comando = input("Digite alguma das teclas de movimentação: W | S | A | D ou [emergencia]: ").lower()

    # Condição de término 1: Interrupção manual
    if comando == "emergencia":
        print("🚨 Subida de emergência acionada! Missão abortada.")
        break

    # Atualiza o estado do jogo
    x, y, oxigenio = movimentacao_submarino(x, y, oxigenio, comando)

    # Condição de término 2: Falha (Sem oxigênio)
    if not verificar_status_oxigenio(oxigenio):
        print("Oxigênio esgotado. A tripulação desmaiou. Fim de jogo.")
        break

    # Condição de término 3: Sucesso (Encontrou a caixa)
    if x == cx and y == cy:
        print("Caixa-preta recuperada! Iniciando subida de emergência. Você venceu!")
        break
