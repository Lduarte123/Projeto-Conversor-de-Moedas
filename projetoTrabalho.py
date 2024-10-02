

import customtkinter as ctk
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_moeda

janela = ctk.CTk()
janela.geometry("500x500")


dic_conversoes_disponiveis = conversoes_disponiveis()


titulo = ctk.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = ctk.CTkLabel(janela, text="Selecione moeda de origem")
texto_moeda_destino = ctk.CTkLabel(janela, text="Selecione moeda de destino")


campo_moeda_origem = ctk.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()))
campo_moeda_destino = ctk.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()))

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moedas.configure(text=f"{moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = ctk.CTkButton(janela, text='Converter', command=converter_moeda)


lista_moedas = ctk.CTkScrollableFrame(janela, width=480, height=200)

texto_cotacao_moedas = ctk.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = ctk.CTkLabel(lista_moedas, text=f'{codigo_moeda}: {nome_moeda}')
    texto_moeda.pack()


titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moedas.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


janela.mainloop()