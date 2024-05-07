# 1. Abrir o sistema para cadastro de produtos
  # >>>> https://dlp.hashtagtreinamentos.com/python/intensivao/login
  # Biblioteca >> pyautogui
  
# 2. Importar base de dados dos produtos para cadastro
# 3. Testar o cadastro de produtos
# 4. Cadastrar os produtos até o fim da base.


import pyautogui
import time
import pandas as pd

# pyautogui.click # Clicar com o mouse
# pyautogui.write # Escrever texto
# pyautogui.press # Pressionar tecla
# pyautogui.hotkey #Pressionar conjunto de teclas

# Configuração de PAUSE entre comandos (0.3seg, menos de meio segundo)
pyautogui.PAUSE = 0.3

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1115, y=779)

# Entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#LOGAR NO SISTEMA
pyautogui.click(x=1257, y=410)
pyautogui.write("testandox1@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhamuitoforte12x")
# Clicando no botão
pyautogui.press("tab")
pyautogui.press("enter")


# Abrir / Importar a base de dados para cadastro
# Bibliotecas: pandas, numpy, openpyxl
# Tabula pacote do PY que transforma PDF em Pandas.

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastro de Produto

for linha in tabela.index:
    pyautogui.click(x=1153, y=291)
    # Pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # Preencher o campo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # Cadastro finalizado, vai clicar no botão ENVIAR
    
    
    
    # Dar scroll e voltar ao inicio
    pyautogui.scroll(5000)

