# SBB Estatisticas
Programa que faz a soma de dicionários em Python e importa os dados para um CSV, pronto para ser usado no Google Sheets

Para utilizar o programa, baixe essa pasta pelo Git Bash ou seu Prompt de Comando com o comando `git clone https://github.com/jgabrielsg/SBB-Estatisticas` e todas as pastas e arquivos serão instalados no seu computador. Se preferir, pode copiar o código direto do arquivo "soma.py" e colocar no VS Code, Spyder e afins e criar as pastas "Jovem" e "SBB" no mesmo diretório (pasta) que estiver o "soma.py" e colocar pastas com os txt de cada rodada dentro, seguindo a padronização daqui.

Ademais, é possível baixar por zip clicando no botão verde "Code" e instalando por lá.

---

## Funcionamento

Após os txt's colocados na pasta da rodada do campeonato, altere a variável `RODADA` dentro do soma.py e rode o programa. Também será necessário alterar o valor de `pasta = "SBB/"+str(RODADA)` para `pasta = "Jovem/"+str(RODADA)` ou o contrário dependendo se quiser somar os jogos da SBB ou da Liga Jovem. O resultado sairá em CSV, Comma Separated Variables (Variáveis separadas por vírgula), se você tiver excel no computador é provável que o excel até identifique os arquivos CSV como planilhas do Excel.

![image](https://github.com/jgabrielsg/SBB-Estatisticas/assets/126505004/2f95b86e-f1f0-4ef2-8482-433bc49e9fe5)

Após isso, com o arquivo CSV, entre no Google Sheets e clique na aba "Arquivo". Lá dentro, clique em "Importar" e faça o Upload do "resultados.csv", coloque-o:

![image](https://github.com/jgabrielsg/SBB-Estatisticas/assets/126505004/2f0b307c-59b2-41e3-b49c-01963bd376f0)

Enfim, os resultados estarão nesse formato:

![image](https://github.com/jgabrielsg/SBB-Estatisticas/assets/126505004/bccf763e-347e-4408-8d3d-24aee8be1ca9)

Por fim, coloque estes dados nas planilhas de Controle de Stats e coloque os times dos jogadores, o resto da planilha se atualizará sozinha. Qualquer dúvida sobre o Github e o código falar comigo no Discord, qualquer sugestão é bem vinda.
