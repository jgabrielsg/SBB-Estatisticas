import csv
import json
import glob

# Função para somar os tempos jogados
def somar_tempos(tempo1, tempo2):
    minutos1, segundos1 = map(int, tempo1.split(":"))
    minutos2, segundos2 = map(int, tempo2.split(":"))

    total_minutos = minutos1 + minutos2
    total_segundos = segundos1 + segundos2

    if total_segundos >= 60:
        total_minutos += 1
        total_segundos -= 60

    resultado = f"{total_minutos:02}:{total_segundos:02}"
    return resultado

# Função para somar os dados de vários arquivos
def somar_dados(*arquivos):
    soma = {}
    for arquivo in arquivos:
        dados = ler_arquivo(arquivo)
        for jogador in dados:
            nome = jogador["name"]
            if nome in soma:
                for chave in jogador:
                    if chave != "name" and chave != "tempojogando":
                        soma[nome][chave] += jogador[chave]
                
                # Somar os tempos jogados
                soma[nome]["tempojogando"] = somar_tempos(soma[nome]["tempojogando"], jogador["tempojogando"])
            else:
                # Adicionar novo jogador à soma
                soma[nome] = jogador.copy()

    return soma

# Função para ler o arquivo e retornar os dados como uma lista de dicionários
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados

RODADA = 1
# Pasta onde estão os arquivos TXT
pasta = "Jovem/"+str(RODADA)

# Obter a lista de caminhos para os arquivos TXT na pasta
arquivos = glob.glob(pasta + "/*.txt")

# Chamada da função somar_dados com a lista de arquivos
resultado = somar_dados(*arquivos)

# Nome do arquivo de saída CSV
arquivo_csv = "resultado.csv"


# Salvar o resultado em um arquivo CSV
with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    
    # Escrever o cabeçalho do arquivo CSV
    header = ["Nome", "Rodada", "Minutos", "Gols", "Finalizações", "Passe Certo", "Passe Errado", "Assistências", "Interceptações", "Defesas", "Gols Contra", "Erros", "Bumps", "Bumped", "Team Bumps"]
    writer.writerow(header)
    
    # Escrever os dados de cada jogador no arquivo CSV
    for jogador, estatisticas in resultado.items():
        linha = [
            jogador,
            RODADA,
            estatisticas["tempojogando"],
            estatisticas["gols"],
            estatisticas["finalizacoes"],
            estatisticas["passecerto"],
            estatisticas["passeerrado"],
            estatisticas["assistencias"],
            estatisticas["interceptacoes"],
            estatisticas["defesas"],
            estatisticas["golscontra"],
            estatisticas["erros"],
            estatisticas["bumps"],
            estatisticas["bumped"],
            estatisticas["teambumps"]
        ]
        print(linha)
        writer.writerow(linha)

print("Resultado salvo no arquivo CSV com sucesso!")
