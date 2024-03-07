import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("Google Chrome")

pyautogui.press("enter")

pyautogui.click(x=870, y=461)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=728, y=411)

pyautogui.write("samucaprogramador@gmail.com")

pyautogui.press("tab")

pyautogui.write("ilovesoares123")

pyautogui.click(x=957, y=571)  

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

pyautogui.click(x=693, y=295)

for linha in tabela.index:
    
    #codigo
    codigo = tabela.loc[linha, "codigo"] 
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"] 
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"] 
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"] ))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(0.5)
    # pyautogui.scroll(5000) 
    pyautogui.click(x=772, y=289)




