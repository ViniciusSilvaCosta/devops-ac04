def inicializar():
  tab = [ ]
  for i in range(3):
    linha = [ ]
    for j in range(3):
      linha.append(".")
    tab.append(linha)
  return tab

def main( ):
  jogo = inicialzar( )
  print (jogo)
if _name_ == "_main_":
  main()
  
