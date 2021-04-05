import PySimpleGUI as sg
from faker import Faker
import os

#Layout PYSIMPLEGUI
sg.theme('reddit')

#Layout janela PYSIMPLEGUI
layout = [[ sg.Text('Digite o número dos dados que deseja que sejam gerados!')],
            [sg.Button('Gerar nome aleatório', size=(20,0)), sg.Input(key= 'nome_aleatorio', size=(40,0))],
            [sg.Button('Gerar email aleatório',size=(20,0)), sg.Input(key= 'email_aleatorio', size=(40,0))],
            [sg.Button('Gerar telefone aleatório',size=(20,0)), sg.Input(key= 'telefone_aleatorio', size=(40,0))],
            [sg.Button('Gerar cidade aleatória',size=(20,0)), sg.Input(key= 'cidade_aleatoria', size=(40,0))],
            [sg.Button('Gerar estado aleatório',size=(20,0)), sg.Input(key= 'estado_aleatorio', size=(40,0))],
            [sg.Button('Gerar endereço aleatório',size=(20,0)), sg.Input(key= 'endereço_aleatorio', size=(40,0))],
            [sg.Text(size=(40,1), key= '-OUTPUT-')],
            [sg.Button('Gerar todos os dados aleatórios'), sg.Button('Salvar dados em um arquivo'), sg.Button('Sair do programa')]]
            
#Criando a janela
window = sg.Window('Gerador de dados aleatórios',layout=layout)
#criando classe faker
fake = Faker('pt-BR')
Faker.seed(0)
#monitorando dados janela
while True:
    event, values = window.read()
    #descobrir se fecharam a janela
    if event == sg.WINDOW_CLOSED or event == 'Sair do programa':
        break

    elif event == 'Gerar nome aleatório':
        aleatorio_nome = fake.name()
        window['nome_aleatorio'].update(aleatorio_nome)

    elif event == 'Gerar email aleatório':
        aleatorio_email = fake.email()
        window['email_aleatorio'].update(aleatorio_email)

    elif event == 'Gerar telefone aleatório':
        aleatorio_telefone = fake.phone_number()
        window['telefone_aleatorio'].update(aleatorio_telefone)

    elif event == 'Gerar cidade aleatória':
        aleatoria_cidade = fake.city()
        window['cidade_aleatoria'].update(aleatoria_cidade)

    elif event == 'Gerar estado aleatório':
        aleatorio_estado = fake.state()
        window['estado_aleatorio'].update(aleatorio_estado)
    
    elif event == 'Gerar endereço aleatório':
        aleatorio_endereço = fake.address()
        window['endereço_aleatorio'].update(aleatorio_endereço)
    
    elif event == 'Gerar todos os dados aleatórios':
        aleatorio_nome = fake.name()
        aleatorio_email = fake.email()
        aleatorio_telefone = fake.phone_number()
        aleatoria_cidade = fake.city()
        aleatorio_estado = fake.state()
        window['nome_aleatorio'].update(aleatorio_nome)
        window['email_aleatorio'].update(aleatorio_email)
        window['telefone_aleatorio'].update(aleatorio_telefone)
        window['cidade_aleatoria'].update(aleatoria_cidade)
        window['estado_aleatorio'].update(aleatorio_estado)
    
    try:
        if event == 'Salvar dados em um arquivo':
            with open('Dados_Falsos.txt', 'a', encoding='utf-8', newline='') as arquivo:
                arquivo.write(f'Nome: {aleatorio_nome}{os.linesep}Email: {aleatorio_email}{os.linesep}Telefone: {aleatorio_telefone}{os.linesep}Cidade: {aleatoria_cidade}{os.linesep}Estado: {aleatorio_estado}{os.linesep}')
            window['-OUTPUT-'].update('Dados salvos!')
    except NameError as erro:
        print('Não foi possivel salvar seus dados pois não foi gerado nenhum dado')
