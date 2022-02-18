import os
#dir = os.path.dirname(os.path.realpath(__file__))


a = open('arquivos nomes.txt', 'wt+')

dir = input('> ')
with open('arquivos nomes.txt', 'a') as txt:

  for diretorio, subpastas, arquivos in os.walk(dir):
    if 'venv' not in diretorio:
      for arquivo in arquivos:
        if '/' in diretorio:
          livros = diretorio + '\\' + arquivo
          txt.write(arquivo+'\n')
          print(livros)