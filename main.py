# Classificador de Nível de Herói
nome_heroi = input("Coloque o nome do Herói aqui: ")

while True:
    try:
        xp = float(input(f"Qual o XP de {nome_heroi}: "))
        if xp >= 0:
            break
        else:
            print("Por favor, experiência invalida.")
    except ValueError:
        print("Por favor, insira um número válido.")

nivel_heroi = "Nível não disponível"

if xp < 0:
    print("Valor negativo inserido. O XP não pode ser negativo.")
else:
    if xp <= 1000:
        nivel_heroi = "Ferro"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 1001 <= xp <= 2000:
        nivel_heroi = "Bronze"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 2001 <= xp <= 5000:
        nivel_heroi = "Prata"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 5001 <= xp <= 7000:
        nivel_heroi = "Ouro"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 7001 <= xp <= 8000:
        nivel_heroi = "Platina"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 8001 <= xp <= 9000:
        nivel_heroi = "Ascendente"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif 9001 <= xp <= 10000:
        nivel_heroi = "Imortal"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    elif xp >= 10001:
        nivel_heroi = "Radiante"
        print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
    else:
        print("Valor inválido")
