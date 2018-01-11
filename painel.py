
########Isso aqui importa duas bibliotecas que a gente precisa usar no sistema ##########
import sys

import tkinter.messagebox
from tkinter.ttk import*
from datetime import datetime
now = datetime.now()

##################
try:
    from Tkinter import *
except ImportError: #Esse except é tipo uma manipulação de erro, é tipo um condicional pra se não der certo com o Tkienter com T maisculo ele importa com o t minusculo.
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
import painel_support
def vp_start_gui():
  
    global val, w, root
    root = Tk()
    root.resizable(width=False, height=False)
    top = Primeiro_Painel (root)
    painel_support.init(root, top)
    root.mainloop()
w = None
def create_Primeiro_Painel(root, *args, **kwargs):

    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Primeiro_Painel (w)
    
    painel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Primeiro_Painel():
    global w
    w.destroy()
    w = None

def tempo():
        global ano
        global mes
        global dia
        global hora
        global minutos
        global segundos
        ano = now.year
        mes = now.month
        dia = now.day
        hora = now.hour
        minutos = now.minute
        segundos = now.second
        return ano,mes,dia,hora,minutos,segundos
        
###############################################
###### Funções que varrem os arquivos ############# 
def arquivo():
    arquivo = open("usuarios.txt", "r")
    global usuariosCadastrados
    global chavesUsuarios
    usuariosCadastrados = {}
    continuar = True
    while continuar:
        nome = arquivo.readline() 
        cpf = arquivo.readline()
        if cpf == "":
            continuar = False
        senha = arquivo.readline()
        acesso = arquivo.readline()
        usuariosCadastrados[cpf] = [nome,cpf,senha,acesso]
        chavesUsuarios = usuariosCadastrados.keys()
    return usuariosCadastrados
    arquivo.close()

    
def elementos():
    arquivoElementos =  open("elementos.txt", "r")
    global elementosCadastrados
    elementosCadastrados = {}
    continuar = True
    while continuar:
        nome = arquivoElementos.readline()
        if nome == "":
            continuar = False
        cpf = arquivoElementos.readline()
        numero = arquivoElementos.readline()
        endereco = arquivoElementos.readline()
        numeroPedidos = arquivoElementos.readline()
        elemento = "\n"+numeroPedidos
        preferencias = arquivoElementos.readline()
        elementosCadastrados[numero]= [nome,cpf,endereco,[preferencias],[elemento]]
    return elementosCadastrados
    arquivoElementos.close()

def elementosAtualizados():
    atualizarArquivo = open("elementos.txt", "r")
    global adicionandoElementos
    global chaves
    adicionandoElementos = {}
    lista = []
    verificar = True
    while verificar:
        nome = atualizarArquivo.readline()
        if nome == "":
            verificar = False
        cpf = atualizarArquivo.readline()
        numero = atualizarArquivo.readline()
        endereco = atualizarArquivo.readline()
        numeroPedidos = atualizarArquivo.readline()
        preferencias = atualizarArquivo.readline()
        if verificar == True:
            adicionandoElementos[numero]=[nome,cpf,numero,endereco,numeroPedidos,preferencias]
            lista = [nome,cpf,numero,endereco,[numeroPedidos],[preferencias]]
        chaves = adicionandoElementos.keys()

        
###############################################
###########   funções de cliques  ##############
   
def chamar_click():
    entradaNumero = procurarCliente.get()
    entradaNumero += "\n"
    elementosAtualizados()
    lista = []
    listaAux = []
    itensTexto = ""
    tempo()
    chaves = adicionandoElementos.keys()
    limpar = True
    global existe
    existe = False
    for dados in chaves:
        if dados == entradaNumero:
            varrer = adicionandoElementos[dados][4]
            for itens in varrer:
                if itens == "$":
                    lista.append(itensTexto)
                    itensTexto = ""
                else:
                    itensTexto += itens

            lbNome["text"]= "\n" + adicionandoElementos[dados][0]
            lbCpf["text"]= "\n" + adicionandoElementos[dados][1]
            lbEnd["text"] = "\n" + adicionandoElementos[dados][3]

            for elementos in lista:
                print(elementos)
                if elementos != "":
                    listaAux.append(elementos)
            quantidadePedidos = len(listaAux)
            print(listaAux)
            print(listaAux[quantidadePedidos -1])            
            lbPedido01["text"]= listaAux[quantidadePedidos -1]
            if quantidadePedidos > 1:
                lbPedido02["text"]= listaAux[quantidadePedidos - 2]
                if quantidadePedidos > 2:
                    lbPedido03["text"]= listaAux[quantidadePedidos - 3]
                    if quantidadePedidos > 3:
                        lbPedido04["text"]= listaAux[quantidadePedidos - 4]
                        if quantidadePedidos > 4:
                            lbPedido05["text"]=  listaAux[quantidadePedidos - 5]
                        else:
                            lbPedido05["text"] = ""
                    else:
                        lbPedido04["text"] = ""
                        lbPedido05["text"] = ""

                else:
                    lbPedido03["text"] = ""
                    lbPedido04["text"] = ""
                    lbPedido05["text"] = ""

            else:
                lbPedido02["text"] = ""
                lbPedido03["text"] = ""
                lbPedido04["text"] = ""
                lbPedido05["text"] = ""

            limpar =False


    if limpar == True:
            lbNome["text"]= "" 
            lbCpf["text"]= "" 
            lbEnd["text"] = "" 
            lbPedido01["text"] = ""
            lbPedido02["text"] = ""
            lbPedido03["text"] = ""
            lbPedido04["text"] = ""
            lbPedido05["text"] = ""
    clientesFidelidade()
def chamar_click01():
    entradaNumero03 = procurarCliente03.get()
    entradaNumero03 += "\n"
    elementosAtualizados()
    lista = []
    listaLimpa = []
    itensTexto= ""
    tempo()
    chaves = adicionandoElementos.keys()
    limpar = True
    existe = False
    for dados in chaves:
        if dados == entradaNumero03:
            existe = True
            alterarNome.config(state="normal")
            alterarNumero.config(state="normal")
            alterarEndereco.config(state="normal")
            alterar.config(state="normal")
            print(adicionandoElementos[dados][4])
            for itens in adicionandoElementos[dados][4]:
                if itens == "$" or itens == "$$":
                    lista.append(itensTexto)
                    itensTexto = ""
                else:
                    itensTexto += itens

            for limpando in lista:
                if limpando != "":
                    listaLimpa.append(limpando)
            quantidadePedidos = len(listaLimpa)
            print(lista)
            lbNome03["text"]= "\n" + adicionandoElementos[dados][0]
            lbCpf03["text"]= "\n" + adicionandoElementos[dados][1]
            lbEnd03["text"] = "\n" + adicionandoElementos[dados][2]
            print(quantidadePedidos)
            lbPedido013["text"]= listaLimpa[quantidadePedidos - 1]
            if quantidadePedidos > 1:
                lbPedido023["text"]= listaLimpa[quantidadePedidos - 2]
                if quantidadePedidos > 2:
                     lbPedido033["text"]= listaLimpa[quantidadePedidos - 3]
                     if quantidadePedidos > 3:
                        lbPedido043["text"]= listaLimpa[quantidadePedidos - 4]
                        if quantidadePedidos > 4:
                            lbPedido053["text"]=  listaLimpa[quantidadePedidos - 5]
                        else:
                            lbPedido053["text"] = ""
                     else:
                        lbPedido043["text"] = ""
                        lbPedido053["text"] = ""

                else:
                    lbPedido033["text"] = ""
                    lbPedido043["text"] = ""
                    lbPedido053["text"] = ""

            else:
                lbPedido023["text"] = ""
                lbPedido033["text"] = ""
                lbPedido043["text"] = ""
                lbPedido053["text"] = ""
            limpar =False
    if existe == False:
        alterarNome.config(state="disabled")
        alterarNumero.config(state="disabled")
        alterarEndereco.config(state="disabled")
        alterar.config(state="disabled")

    if limpar == True:
            lbNome03["text"]= "" 
            lbCpf03["text"]= "" 
            lbEnd03["text"] = "" 
            lbPedido013["text"] = ""
            lbPedido023["text"] = ""
            lbPedido033["text"] = ""
            lbPedido043["text"] = ""
            lbPedido053["text"] = ""
    clientesFidelidade()       
def concluir_click():
    global verificadorLabel
    tempo()
    
    getPedidos = entradaPedidos.get()
    getPedidos += "\n"
    entradaTotal = str(dia)+"/"+str(mes)+"/"+str(ano)+"-"+str(hora)+":"+str(minutos)+":"+str(segundos)+" Foram realizado(s) o(s) pedido(s) de nº " + getPedidos
    getPreferencias = entradaPreferencias.get()
    getPreferencias += "\n"
    entradaNumero = procurarCliente.get()
    entradaNumero += "\n"
    concluir_click()
    verificadorLabel = 0
    for dados in chaves:
        if dados == entradaNumero:
            tempo()
            lista = []
            elementosAtualizados()
            palavra=""
            adicionandoElementos[dados][4] += entradaTotal
            for i in adicionandoElementos[dados][4]:
              if i!="\n":
                palavra=palavra+i
              else:
                if palavra!="\n":
                  lista.append(palavra)
                  verificadorLabel += 1
                  palavra=""
            if palavra != "":
                    lista.append(palavra)
            vazio=""
            for elementos in lista:
                vazio +=  str(elementos) + "$"
            vazio += "\n"

            adicionandoElementos[dados][4] = vazio
            
            escreverArquivo = open("elementos.txt", "w")
            for elementos in chaves:
                escreverArquivo.writelines(adicionandoElementos[elementos])
            escreverArquivo.close()
    tela.destroy()

    
def vender_click():
    global tela
    global entradaPedidos
    global entradaPreferencias
    tela = Tk()
    tela.resizable(width=False, height=False)
    tela.configure(background="#253942")
    tela.geometry("300x200+200+200")
    
    cadastro = Label(tela, text="------ Venda ------",background="#253942",foreground="white")
    cadastro.pack(padx=0, pady=8)
    
    numeroPedidos = Label(tela, text=" Número do(s) pedido(s):",background="#253942",foreground="white")
    numeroPedidos.place(relx=0.055, rely=0.25, height=15, width=150)
    entradaPedidos = Entry(tela,)
    entradaPedidos.place(relx=0.1, rely=0.35, height=20, width=250)    
    clientesFidelidade()
    concluir = Button(tela, text="Concluir", background="#093D78", foreground="white",command=concluir_click).place(relx=0.35, rely=0.80, height=25, width=100)
    tela.mainloop()
   

def cadastrarCliente_click():
    entradaNome = nome.get()
    entradaNome += "\n"
    entradaCpf = cpf.get()
    entradaCpf += "\n"
    entradaTele = telefone.get()
    entradaTele += "\n"
    entradaEnd = endereco.get()
    entradaEnd += "\n"
    entradaPedido = nPedido.get()
    tempo()
    dataPedido =  str(dia)+"/"+str(mes)+"/"+str(ano)+"-"+str(hora)+":"+str(minutos)+":"+str(segundos)+" Foram realizados os pedidos de nº "+ entradaPedido + "$"+ "\n"
    entradaPreferencias = preferencias.get()
    entradaPreferencias += "\n"
    elementos()
    global chavesElementos
    chavesElementos = elementosCadastrados.keys()
    if entradaTele in chavesElementos:
        msg = tkinter.messagebox.showinfo("Frame1","Número já cadastrado!")
    elif entradaTele not in chavesElementos:   
        arquivo = open("elementos.txt", "a" )
        arquivo.write(entradaNome)
        arquivo.write(entradaCpf)
        arquivo.write(entradaTele)
        arquivo.write(entradaEnd)
        arquivo.write(dataPedido)
        arquivo.write(entradaPreferencias)
        arquivo.close()
        msg = tkinter.messagebox.showinfo("Frame1","Cliente cadastrado com sucesso!")
    elementos()
    clientesFidelidade()
def alterar_click():
    comparandoEntrada = procurarCliente03.get()
    comparandoEntrada += "\n"
    entNome =  alterarNome.get()
    entNome += "\n"
    entNum =  alterarNumero.get()
    entNum += "\n"
    entEnd =  alterarEndereco.get()
    entEnd += "\n"

    elementosAtualizados()
    igual = False
    for elementos in chaves:
        if elementos == comparandoEntrada:
            adicionandoElementos[elementos][0] = entNome
            adicionandoElementos[elementos][2] = entNum
            adicionandoElementos[elementos][3] = entEnd
            
            escreverArquivo = open("elementos.txt", "w")
            for elementos in chaves:
                escreverArquivo.writelines(adicionandoElementos[elementos])
            escreverArquivo.close()            
    clientesFidelidade()
def alterando_dados_clientes_click():
        global aba03
        global lbNome03
        global lbCpf03
        global lbEnd03
        global procurarCliente03
        global lbPreferencia03
        global lbPedido013
        global lbPedido023
        global lbPedido033
        global lbPedido043
        global lbPedido053
        Label(aba03, text = "Nº do cliente", background="#253942",foreground="white" ).place(relx=0.02, rely=0.17, height=10, width=100)
        procurarCliente03 = Entry(aba03)
        procurarCliente03.place(relx=0.18, rely=0.17, height=16, width=100)
        pesquisar03 = Button(aba03,text="Pesquisar",background="#63e276",foreground="black",command=chamar_click01)
        pesquisar03.place(relx=0.33, rely=0.17, height=19, width=70)

        Label(aba03, text = "Nome: ", background="#253942",foreground="white" ).place(relx=0.01, rely=0.23, height=10, width=100)
        lbNome03 = Label(aba03, text = "", background="#34515E",foreground="white" )
        lbNome03.place(relx=0.15, rely=0.225, height=25, width=550)
        Label(aba03, text = "CPF: ", background="#253942",foreground="white" ).place(relx=0.001, rely=0.31, height=10, width=100)
        lbCpf03 = Label(aba03, text = "", background="#34515E",foreground="white" )
        lbCpf03.place(relx=0.15, rely=0.297, height=25, width=550)
        Label(aba03, text = "Endereço: ", background="#253942",foreground="white" ).place(relx=0.001, rely=0.39, height=10, width=120)
        lbEnd03 = Label(aba03, text = "", background="#34515E",foreground="white" )
        lbEnd03.place(relx=0.15, rely=0.37, height=25, width=550)
    
        lbPedido013 = Label(aba03, text = "", background="#34515E",foreground="white")
        lbPedido013.place(relx=0.01, rely=0.45, height=20, width=700)
        lbPedido023 = Label(aba03, text = "",background="#34515E",foreground="white" )
        lbPedido023.place(relx=0.01, rely=0.50, height=20, width=700)
        lbPedido033 = Label(aba03, text = "",background="#34515E",foreground="white" )
        lbPedido033.place(relx=0.01, rely=0.55, height=20, width=700)
        lbPedido043 = Label(aba03, text = "",background="#34515E",foreground="white" )
        lbPedido043.place(relx=0.01, rely=0.60, height=20, width=700)
        lbPedido053 = Label(aba03, text = "",background="#34515E",foreground="white" )
        lbPedido053.place(relx=0.01, rely=0.65, height=20, width=700)

        global alterarNome
        global alterarNumero
        global alterarEndereco
        global alterar
    
        Label(aba03, text = "", background="#253942").place(relx=0.01, rely=0.70, height=17, width=300)


        Label(aba03, text = "Nome", background="#253942",foreground="white" ).place(relx=0.01, rely=0.75, height=10, width=100)
        alterarNome = Entry(aba03)
        alterarNome.place(relx=0.15, rely=0.75, height=16, width=150)
        alterarNome.config(state="disabled")
        
        Label(aba03, text = "Número", background="#253942",foreground="white" ).place(relx=0.016, rely=0.80, height=10, width=100)
        alterarNumero = Entry(aba03)
        alterarNumero.place(relx=0.15, rely=0.80, height=16, width=150)
        alterarNumero.config(state="disabled")
        
        Label(aba03, text = "Endereço", background="#253942",foreground="white" ).place(relx=0.02, rely=0.85, height=10, width=100)
        alterarEndereco = Entry(aba03)
        alterarEndereco.place(relx=0.15, rely=0.85, height=16, width=150)
        alterarEndereco.config(state="disabled")

        alterar = Button(aba03,text="Alterar",background="#63e276",foreground="black",command=alterar_click)
        alterar.place (relx=0.185, rely=0.9, height=20, width=100)
        alterar.config(state="disabled")
        clientesFidelidade()

def chamar_funcionarios_click():
    entradaDados = procurarFuncionario.get()
    entradaDados += "\n"
    arquivo()
    lista = []
    itensTexto = ""
    chaves = usuariosCadastrados.keys()
    limpa = True
    for dados in chaves:
        if dados == entradaDados:
            lbNomeFun["text"] = "\n" + usuariosCadastrados[dados][0]
            senha = usuariosCadastrados[dados][1]
            lbCpfFun["text"] = "\n" + usuariosCadastrados[dados][3]
 
def alterar_click1(valor):
        if valor != 0:
            arquivo()
            convertendo = str(valor)
            convertendo += "\n"
            funcionario = procurarFuncionario.get()
            funcionario += "\n"
            for elementos in chavesUsuarios:

                if funcionario == elementos:
                    usuariosCadastrados[funcionario][3] = convertendo
                    escreverArquivo = open("usuarios.txt", "w")
                    for elementos in chavesUsuarios:

                        escreverArquivo.writelines(usuariosCadastrados[elementos])
                    escreverArquivo.close()
        clientesFidelidade()
def alterando_dados_funcionarios_click():
        global aba03
        global lbNomeFun
        global lbCpfFun
        global procurarFuncionario


        Label(aba03, text = "CPF do funcionário", background="#253942",foreground="white").place(relx=0.02, rely=0.17, height=10, width=100)
        procurarFuncionario = Entry(aba03)
        procurarFuncionario.place(relx=0.18, rely=0.17, height=16, width=100)
        pesquisarFun = Button(aba03,text="Pesquisar",background="#63e276",foreground="black",command=chamar_funcionarios_click )
        pesquisarFun.place(relx=0.33, rely=0.17, height=19, width=70)

        Label(aba03, text = "", background="#253942",foreground="white" ).place(relx=0.01, rely=0.23, height=10, width=100)
        lbNomeFun = Label(aba03, text = "", background="#253942",foreground="white" )
        lbNomeFun.place(relx=0.15, rely=0.225, height=25, width=550)

        Label(aba03, text = "Nome: ", background="#253942",foreground="white" ).place(relx=0.01, rely=0.31, height=10, width=100)
        lbNomeFun = Label(aba03, text = "", background="#34515E",foreground="white" )
        lbNomeFun.place(relx=0.15, rely=0.3, height=25, width=550)
        
        Label(aba03, text = "Nível de acesso: ", background="#253942",foreground="white" ).place(relx=0.001, rely=0.39, height=10, width=100)
        lbCpfFun = Label(aba03, text = "", background="#34515E",foreground="white" )
        lbCpfFun.place(relx=0.15, rely=0.38, height=25, width=550)

        lbPedido01Fun = Label(aba03, text = "", background="#253942",foreground="white")
        lbPedido01Fun.place(relx=0.01, rely=0.45, height=20, width=700)
        lbPedido02Fun = Label(aba03, text = "",background="#253942",foreground="white" )
        lbPedido02Fun.place(relx=0.01, rely=0.50, height=20, width=700)
        lbPedido03Fun = Label(aba03, text = "",background="#253942",foreground="white" )
        lbPedido03Fun.place(relx=0.01, rely=0.55, height=20, width=700)
        lbPedido04Fun = Label(aba03, text = "",background="#253942",foreground="white" )
        lbPedido04Fun.place(relx=0.01, rely=0.60, height=20, width=700)
        lbPedido05Fun = Label(aba03, text = "",background="#253942",foreground="white" )
        lbPedido05Fun.place(relx=0.01, rely=0.65, height=20, width=700)
    
        Label(aba03, text = "Estagiário", background="#253942",foreground="white" ).place(relx=0.01, rely=0.70, height=10, width=100)
        alterarNivel01 = Entry(aba03)
        alterarNivel01.place(relx=0.15, rely=0.70, height=16, width=150)
        
        Label(aba03, text = "Efetivo", background="#253942",foreground="white" ).place(relx=0.01, rely=0.75, height=10, width=100)
        alterarNivel02 = Entry(aba03)
        alterarNivel02.place(relx=0.15, rely=0.75, height=16, width=150)
        
        Label(aba03, text = "Gerente", background="#253942",foreground="white" ).place(relx=0.01, rely=0.80, height=10, width=100)
        alterarNivel03 = Entry(aba03)
        alterarNivel03.place(relx=0.15, rely=0.80, height=16, width=150)

        Label(aba03, text = "Super Usuário", background="#253942",foreground="white" ).place(relx=0.01, rely=0.85, height=10, width=100)
        alterarNivel04 = Entry(aba03)
        alterarNivel04.place(relx=0.15, rely=0.85, height=16, width=150)

        valor= IntVar()

        primeiro = Radiobutton(aba03, text="1",variable = valor,value = "1", background="#34515E" )
        primeiro.place(relx=0.15, rely=0.70, height=18, width=150)
    

        segundo = Radiobutton(aba03,text = "2",variable = valor, value = "2", background="#34515E")
        segundo.place(relx=0.15, rely=0.75, height=18, width=150)

        terceiro = Radiobutton(aba03,text = "3",variable = valor, value = "3", background="#34515E")
        terceiro.place(relx=0.15, rely=0.80, height=18, width=150)

        quarto = Radiobutton(aba03,text = "4",variable = valor, value = "4", background="#34515E")
        quarto.place(relx=0.15, rely=0.85, height=18, width=150)       

        alterar = Button(aba03,text="Alterar",background="#63e276",foreground="black", command=lambda:alterar_click1(valor.get()))
        alterar.place (relx=0.185, rely=0.9, height=20, width=100)
        clientesFidelidade()

def clientesFidelidade():
    '''
    Está função realiza a contagem de pedidos que cada cliente realizou e as atribui à um dicionário, logo depois, a função realiza uma ordenação
    desse valores de forma decrescente.
    ''' 
    elementosAtualizados()
    ordenacao = {}
    ordenacao1 = {}
    listaOrd = []
    listaOrd1 = []
    listaOrdStr=[]
    listaChaves = []
    ordemChaves = []

    ### ordena a quantidade de compras de forma decrescente
    for valores in chaves:
        contador = 0
        varrer = adicionandoElementos[valores][4]
        for contagem in varrer:
            if contagem == "$":
                contador += 1 
            elif contagem == "\n":
                pass                
        if contador == 1 or contador == 2 :
            ordenacao[valores] = (contador)
        elif contador == 3:
            ordenacao[valores] = contador -1
        elif contador % 2 == 0 :
            operacao = ((contador/2) - 1)
            ordenacao[valores] = (operacao)
        else:
            ordenacao[valores] = (contador//2)
    valores = ordenacao.values()
    for itens in valores:
        listaOrd.append(int(itens))

    listaOrd.sort(reverse=True)

    for convertendo in listaOrd:
        listaOrdStr.append(str(convertendo))
    escrevendo = 1
    for dados in listaOrdStr:
        for chavesAcesso in ordenacao:
            if str(ordenacao[chavesAcesso]) == dados :
                if escrevendo == 1:
                    cliente01["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                elif escrevendo == 2:
                    cliente02["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 3 and nome != adicionandoElementos[chavesAcesso][0]:
                    cliente03["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome1 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 4 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0]:
                    cliente04["text"] = '\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome3 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 5 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0]:
                    cliente05["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome4 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 6  and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0] and nome4 !=  adicionandoElementos[chavesAcesso][0]:
                    cliente06["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome5 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 7 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0] and nome4 !=  adicionandoElementos[chavesAcesso][0] and nome5 != adicionandoElementos[chavesAcesso][0]:
                    cliente07["text"] = '\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome6 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 8 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0] and nome4 !=  adicionandoElementos[chavesAcesso][0] and nome5 != adicionandoElementos[chavesAcesso][0] and nome6 != adicionandoElementos[chavesAcesso][0]:
                    cliente08["text"] ='\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome7 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 9 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0] and nome4 !=  adicionandoElementos[chavesAcesso][0] and nome5 != adicionandoElementos[chavesAcesso][0] and nome6 != adicionandoElementos[chavesAcesso][0] and nome7!= adicionandoElementos[chavesAcesso][0]:
                    cliente09["text"] = '\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                    escrevendo += 1
                    nome8 = adicionandoElementos[chavesAcesso][0]
                elif escrevendo == 10 and nome != adicionandoElementos[chavesAcesso][0] and nome1 != adicionandoElementos[chavesAcesso][0] and nome3 != adicionandoElementos[chavesAcesso][0] and nome4 !=  adicionandoElementos[chavesAcesso][0] and nome5 != adicionandoElementos[chavesAcesso][0] and nome6 != adicionandoElementos[chavesAcesso][0] and nome7!= adicionandoElementos[chavesAcesso][0] and nome8 != adicionandoElementos[chavesAcesso][0]:
                   cliente10["text"] = '\n' + adicionandoElementos[chavesAcesso][0]+ "realizou " + str(dados) +" compras" + " - > número: " +  adicionandoElementos[chavesAcesso][2]
                   escrevendo += 1
                else:
                    pass

def consultarPedidos_click():
    '''
    essa função acessa o dicionario em uma respectiva posição, trata seus dados e escreve no labels
    '''
    global leitura
    global listaAux
    testandoUser = numeroCliente.get()
    testandoUser += '\n'
    remover = numeroPedido.get()
    elementosAtualizados()
    acesso = adicionandoElementos
    lista=[]
    listaPedidos=[]
    listaAux = []
    leitura = ""
    itensTexto = ""
    chaves = acesso.keys()
    contador = 0
    for clientes in chaves:
        if clientes == testandoUser:
            pedidoRemover.config(state="normal")
            botaoRemover.config(state="normal")

            listaPedidos.append(adicionandoElementos[clientes][4])
            contador += 1
    
    for dados in listaPedidos[0]:
        if dados == "$" or dados == "$$":
            lista.append(itensTexto)
            itensTexto = ""
        else:
           itensTexto += dados
           
    for elementos in lista:
        if elementos != "":
            listaAux.append(elementos)
    quantidadePedidos = len(listaAux)
    print(listaAux)
    inversoLista  =  listaAux[::-1]
    print(inversoLista)
            
    lbPedidoRemove01["text"]="pedido nº 1: " + inversoLista[0]
    if quantidadePedidos > 1:
        lbPedidoRemove02["text"]="pedido nº 2: " + inversoLista[1]
        if quantidadePedidos > 2:
            lbPedidoRemove03["text"]="pedido nº 3: " + inversoLista[2]
            if quantidadePedidos > 3:
               lbPedidoRemove04["text"]="pedido nº 4: " + inversoLista[3]
               if quantidadePedidos > 4:
                   lbPedidoRemove05["text"]= "pedido nº 5: " + inversoLista[4]
                   if quantidadePedidos > 5:
                        lbPedidoRemove06["text"]= "pedido nº 6: " + inversoLista[5]
                        if quantidadePedidos > 6:
                            lbPedidoRemove07["text"]="pedido nº 7: " +  inversoLista[6]
                            if quantidadePedidos > 7:
                                lbPedidoRemove08["text"]= "pedido nº 8: " + inversoLista[7]
                            else:
                                lbPedidoRemove08["text"] = ""
                        else:
                            lbPedidoRemove08["text"] = ""
                            lbPedidoRemove07["text"] = ""
                   else:
                        lbPedidoRemove06["text"] = ""
                        lbPedidoRemove07["text"] = ""
                        lbPedidoRemove08["text"] = ""
               else:
                    lbPedidoRemove05["text"] = ""
                    lbPedidoRemove06["text"] = ""
                    lbPedidoRemove07["text"] = ""
                    lbPedidoRemove08["text"] = ""
            else:
                lbPedidoRemove04["text"] =""
                lbPedidoRemove05["text"] = ""
                lbPedidoRemove06["text"] = ""
                lbPedidoRemove07["text"] = ""
                lbPedidoRemove08["text"] = ""
        else:
             lbPedidoRemove03["text"] = "" 
             lbPedidoRemove04["text"] = ""
             lbPedidoRemove05["text"] = ""
             lbPedidoRemove06["text"] = ""
             lbPedidoRemove07["text"] = ""
             lbPedidoRemove08["text"] = ""

    else:
         lbPedidoRemove02["text"] =""
         lbPedidoRemove03["text"] = "" 
         lbPedidoRemove04["text"] = ""
         lbPedidoRemove05["text"] = ""
         lbPedidoRemove06["text"] = ""
         lbPedidoRemove07["text"] = ""
         lbPedidoRemove08["text"] = ""
    if limpar == True:
            lbNome03["text"]= "" 
            lbCpf03["text"]= "" 
            lbEnd03["text"] = "" 
            lbPedido013["text"] = ""
            lbPedido023["text"] = ""
            lbPedido033["text"] = ""
            lbPedido043["text"] = ""
            lbPedido053["text"] = ""
    return lista
def removerPedido_click():
    '''
    essa função é chamada quando o usuário clica no botão remover, ele acessa seus entrys correspondetes, acessa o dicionário e exclui o item desejado, logo depois
    ele sobreescrevre o arquivo com os elementos atualizados. 
    '''
    consultarPedidos_click()
    elementosAtualizados()
    verificador = numeroCliente.get()
    verificador += "\n"
    tratandoLista = []
    tratandoString = ""
    entrada = int(pedidoRemover.get())
    entrada -= 1
    contador = 1
    print(entrada)
    
    print(listaAux)
    tamanhoListaAux = len(listaAux)
    inversoRemoverPedido = listaAux[::-1]
    del inversoRemoverPedido[entrada]

    for pedidos in inversoRemoverPedidos:
        tratandoString += pedidos + "$$"
    tratandoString += "\n"
    print(tratandoString)
    
    adicionandoElementos[verificador][4] = tratandoString

    escreverRetirandoPedido = open("elementos.txt", "w")
    print(chaves)
    for elementos in chaves:
        escreverRetirandoPedido.writelines(adicionandoElementos[elementos])
    escreverRetirandoPedido.close()  

def sair_click():
    '''
    '''
    Frame1.destroy()
########################################
###### funções para telas ##############    
def pesquisarClientes(Frame1):
    '''
    Essa função define posições dos elementos na tela e acessa seus correspondetes labels
    '''
    global aba01
    global lbNome
    global lbCpf
    global lbEnd
    global procurarCliente
    global lbPreferencia
    global lbPedido01
    global lbPedido02
    global lbPedido03
    global lbPedido04
    global lbPedido05
    aba01 = Frame(janelaPrincipal,background="#253942")
    aba01.grid()
    Label(aba01, text = "Número do cliente", background="#253942",foreground="white" ).pack(padx=0,pady =10)
    procurarCliente = Entry(aba01)
    procurarCliente.pack()
    procurar = Button(aba01, text= "Buscar", background="#63e276", foreground="black", command=chamar_click).place(relx=0.414, rely=0.16, height=25, width=125)
    vender = Button(aba01, text= "Vender", background="#63e276", foreground="black", command=vender_click).place(relx=0.80, rely=0.90, height=25, width=100)

    Label(aba01, text = "Nome: ", background="#253942",foreground="white" ).place(relx=0.01, rely=0.23, height=10, width=100)
    lbNome = Label(aba01, text = "", background="#34515E",foreground="white" )
    lbNome.place(relx=0.15, rely=0.225, height=25, width=550)
    Label(aba01, text = "CPF: ", background="#253942",foreground="white" ).place(relx=0.001, rely=0.30, height=10, width=100)
    lbCpf = Label(aba01, text = "", background="#34515E",foreground="white" )
    lbCpf.place(relx=0.15, rely=0.297, height=25, width=550)
    Label(aba01, text = "Endereço: ", background="#253942",foreground="white" ).place(relx=0.02, rely=0.37, height=10, width=100)
    lbEnd = Label(aba01, text = "", background="#34515E",foreground="white" )
    lbEnd.place(relx=0.15, rely=0.37, height=25, width=550)
    
    Label(aba01, text = "  ------------------------------------------------- Últimos pedidos realizados ----------------------------------------------- ", background="#253942",foreground="white" ).pack(padx=0,pady=180)
    lbPedido01 = Label(aba01, text = "", background="#34515E",foreground="white")
    lbPedido01.place(relx=0.01, rely=0.59, height=25, width=700)
    lbPedido02 = Label(aba01, text = "",background="#34515E",foreground="white" )
    lbPedido02.place(relx=0.01, rely=0.65, height=21, width=700)
    lbPedido03 = Label(aba01, text = "",background="#34515E",foreground="white" )
    lbPedido03.place(relx=0.01, rely=0.70, height=21, width=700)
    lbPedido04 = Label(aba01, text = "",background="#34515E",foreground="white" )
    lbPedido04.place(relx=0.01, rely=0.75, height=21, width=700)
    janelaPrincipal.add(aba01, text="Pequisar")
    lbPedido05 = Label(aba01, text = "",background="#34515E",foreground="white" )
    lbPedido05.place(relx=0.01, rely=0.80, height=21, width=700)

def cadastrarCliente(Frame1):
    '''
    Essa função define posições dos elementos na tela e acessa seus correspondetes labels
    '''
    global nome
    global cpf
    global telefone
    global endereco
    global nPedido
    global preferencias

    aba02 = Frame(janelaPrincipal, width=10,  background="#253942")
    aba02.grid()
    Label(aba02, text = "Nome: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    nome = Entry(aba02)
    nome.pack()
    Label(aba02, text = "CPF: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    cpf = Entry(aba02)
    cpf.pack()
    Label(aba02, text = "telefone: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    telefone = Entry(aba02)
    telefone.pack()
    Label(aba02, text = "Endereço: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    endereco = Entry(aba02)
    endereco.pack()
    Label(aba02, text = "nº pedido: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    nPedido = Entry(aba02)
    nPedido.pack()
    Label(aba02, text = "Preferências: ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    preferencias = Entry(aba02)
    preferencias.pack()

    cadastrar = Button(aba02,text="Cadastrar", background="#0E171F", foreground="white",command=cadastrarCliente_click)
    cadastrar.pack()
    janelaPrincipal.add(aba02, text="Cadastrar clientes")    
    
def atualizarDados(Frame1):
    '''
    Essa função define posições dos elementos na tela e acessa seus correspondetes labels
    '''
    global aba03
    aba03 = Frame(janelaPrincipal,background="#253942")
    aba03.grid()
    Label(aba03, text = "-------- Atualização de dados --------", background="#253942", foreground="white").pack(padx=10, pady=5)
    clientes = Button(aba03,text= "Clientes", background="#D7D7D9", foreground="black",command=alterando_dados_clientes_click)
    clientes.place(relx=0.05, rely=0.07, height=20, width=100)
    funcionarios = Button(aba03,text= "Funcionários", background="#D7D7D9", foreground="black",command=alterando_dados_funcionarios_click)
    funcionarios.place(relx=0.19, rely=0.07, height=20, width=100)
    janelaPrincipal.add(aba03, text="Atualizar dados")

def removerUsuario(Frame1):
    '''
    
    '''
    global removePedido
    global numeroCliente
    global numeroPedido
    global  lbPedidoRemove01
    global  lbPedidoRemove02
    global  lbPedidoRemove03
    global  lbPedidoRemove04
    global  lbPedidoRemove05
    global  lbPedidoRemove06
    global  lbPedidoRemove07
    global  lbPedidoRemove08
    global pedidoRemover
    global botaoRemover
    aba04 = Frame(janelaPrincipal,background="#253942")
    aba04.grid()
    janelaPrincipal.add(aba04, text="Remover pedidos")
    Label(aba04, text = "Numero do cliente ",background="#253942",foreground="white" ).pack(padx=10, pady=3)
    numeroCliente= Entry(aba04)
    numeroCliente.pack()
    numeroPedido= Entry(aba04)
    numeroPedido.place(relx=0.01, rely=0.65, height=20, width=20)
    removePedido = Button(aba04,text="Consultar",background="#63e276",foreground="black", command=consultarPedidos_click ).pack(padx=0,pady=8)
    
    lbPedidoRemove01 = Label(aba04, text = "", background="#34515E",foreground="white")
    lbPedidoRemove01.place(relx=0.01, rely=0.30, height=20, width=700)
    lbPedidoRemove02 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove02.place(relx=0.01, rely=0.35, height=20, width=700)
    lbPedidoRemove03 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove03.place(relx=0.01, rely=0.40, height=20, width=700)
    lbPedidoRemove04 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove04.place(relx=0.01, rely=0.45, height=20, width=700)
    lbPedidoRemove05 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove05.place(relx=0.01, rely=0.50, height=20, width=700)
    lbPedidoRemove06 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove06.place(relx=0.01, rely=0.55, height=20, width=700)
    lbPedidoRemove07 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove07.place(relx=0.01, rely=0.60, height=20, width=700)
    lbPedidoRemove08 = Label(aba04, text = "",background="#34515E",foreground="white" )
    lbPedidoRemove08.place(relx=0.01, rely=0.65, height=20, width=700)


    Label(aba04, text="Digite o número do pedido que deseja remover",background="#253942",foreground="white").place(relx=0.01, rely=0.75, height=20, width=300)    
    pedidoRemover = Entry(aba04)
    pedidoRemover.place(relx=0.15, rely=0.80, height=20, width=80)



    botaoRemover = Button(aba04, text ="Remover", backgroun="#63e276", foreground ="black", command=removerPedido_click)
    botaoRemover.place(relx=0.15, rely=0.85, height=20, width=80)

    pedidoRemover.config(state="disabled")
    botaoRemover.config(state="disable")
def fidelidade(Frame1):
    '''
    Essa função define posições dos elementos na tela e acessa seus correspondetes labels
    '''
    global cliente01
    global cliente02
    global cliente03
    global cliente04
    global cliente05
    global cliente06
    global cliente07
    global cliente08
    global cliente09
    global cliente10
    aba05 = Frame(janelaPrincipal,background="#253942")
    aba05.grid()
    janelaPrincipal.add(aba05, text="Clientes fidelidade")
    Label(aba05, text=" #### Clientes fidelidade ####",background="#253942", foreground="white").pack(padx="10", pady="20")
    cliente01 = Label(aba05, text = "", background="#34515E",foreground="white")
    cliente01.place(relx=0.015, rely=0.10, height=30, width=700)
    cliente02 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente02.place(relx=0.015, rely=0.18, height=30, width=700)
    cliente03 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente03.place(relx=0.015, rely=0.26, height=30, width=700)
    cliente04 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente04.place(relx=0.015, rely=0.34, height=30, width=700)
    cliente05 = Label(aba05, text = "", background="#34515E",foreground="white")
    cliente05.place(relx=0.015, rely=0.42, height=30, width=700)
    cliente06 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente06.place(relx=0.015, rely=0.50, height=30, width=700)
    cliente07 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente07.place(relx=0.015, rely=0.58, height=30, width=700)
    cliente08 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente08.place(relx=0.015, rely=0.66, height=30, width=700)
    cliente09 = Label(aba05, text = "", background="#34515E",foreground="white")
    cliente09.place(relx=0.015, rely=0.74, height=30, width=700)
    cliente10 = Label(aba05, text = "",background="#34515E",foreground="white" )
    cliente10.place(relx=0.015, rely=0.82, height=30, width=700)

    clientesFidelidade()
    verificarAtualizacao = Button(aba05, text="Atualizar",background="#63e276", foreground="black")
    verificarAtualizacao.place(relx=0.015, rely=0.90, height=20, width=100)
def sair(Frame1,background="#253942"):
    '''
    função de sair
    '''
    aba06 = Frame(janelaPrincipal)
    aba06.grid()
    janelaPrincipal.add(aba06, text="Sair")
    sair = Button(aba06, text="sair",command=sair_click).pack()

    
###############################################
###### PAINÉIS: NÍVEIS DE ACESSO ##############

def acessoNivel_04():
    """
    Essa função representa a janela de acessoNive04. Esse nível de acessso corresponde ao super usuário
    """
    limpar()
    Frame1 = Frame()
    Frame1.place(relx=0.03, rely=0.04, relheight=0.92, relwidth=0.95)
    Frame1.place(relx=0.03, rely=0.04)
    Frame1.configure(relief=GROOVE)
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief=GROOVE)
    Frame1.configure(background="#0E171F")
    Frame1.configure(width=800)
    Frame1.configure(height=537)
        
    global janelaPrincipal
    janelaPrincipal = Notebook(Frame1, width=725, height=440)
    janelaPrincipal.grid()

    
    pesquisarClientes(Frame1)
    cadastrarCliente(Frame1)
    atualizarDados(Frame1)
    removerUsuario(Frame1)
    fidelidade(Frame1)
    sair(Frame1)

    Frame1.mainloop()

def acessoNivel_03():
    """
    Essa função representa a janela de acessoNive03. Esse nível de acessso corresponde ao gerente.
    """
    limpar()
    Frame1 = Frame()
    Frame1.place(relx=0.03, rely=0.04, relheight=0.92, relwidth=0.95)
    Frame1.place(relx=0.03, rely=0.04)
    Frame1.configure(relief=GROOVE)
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief=GROOVE)
    Frame1.configure(background="#0E171F")
    Frame1.configure(width=800)
    Frame1.configure(height=537)
        
    global janelaPrincipal
    janelaPrincipal = Notebook(Frame1, width=725, height=440)
    janelaPrincipal.grid()

    pesquisarClientes(Frame1)
    cadastrarCliente(Frame1)
    atualizarDados(Frame1)
    removerUsuario(Frame1)
    fidelidade(Frame1)
    sair(Frame1)
def acessoNivel_02():
    """
    Essa função representa a janela de acessoNive02. Esse nível de acessso corresponde ao efetivo.
    """
    limpar()
    Frame1 = Frame()
    Frame1.place(relx=0.03, rely=0.04, relheight=0.92, relwidth=0.95)
    Frame1.place(relx=0.03, rely=0.04)
    Frame1.configure(relief=GROOVE)
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief=GROOVE)
    Frame1.configure(background="#0E171F")
    Frame1.configure(width=800)
    Frame1.configure(height=537)
        
    global janelaPrincipal
    janelaPrincipal = Notebook(Frame1, width=725, height=440)
    janelaPrincipal.grid()

    pesquisarClientes(Frame1)
    cadastrarCliente(Frame1)
def acessoNivel_01():
    """
    Essa função representa a janela de acessoNive01. Esse nível de acessso corresponde ao estagiário.
    """
    limpar()
    Frame1 = Frame()
    Frame1.place(relx=0.03, rely=0.04, relheight=0.92, relwidth=0.95)
    Frame1.place(relx=0.03, rely=0.04)
    Frame1.configure(relief=GROOVE)
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief=GROOVE)
    Frame1.configure(background="#0E171F")
    Frame1.configure(width=800)
    Frame1.configure(height=537)
        
    global janelaPrincipal
    janelaPrincipal = Notebook(Frame1, width=725, height=440)
    janelaPrincipal.grid()

    pesquisarClientes(Frame1)


###################################################
############ cadastrar usuários ##################
def botao_click():
    '''
    Essa função pega os valores dos entrys e cadastra novos usuários
    '''
    valorNome = entradaNome.get()
    valorNome += "\n"
    valorCPF = entradaCPF.get()
    valorCPF += "\n"
    valorSenha = entradaSenha.get()
    valorSenha += "\n"
    autorizacao = entradaAdm.get()
    autorizacao+= "\n"
    printar = arquivo()
    palavrasChaves = usuariosCadastrados.keys()
    acesso = False
    for chaves in palavrasChaves:
        nivelAcesso = usuariosCadastrados[chaves][2]
        
        entrada = "4\n"
        if nivelAcesso == entrada:
            
            if autorizacao == usuariosCadastrados[chaves][1]:
                acesso = True
                if valorCPF in usuariosCadastrados:
                    msg = tkinter.messagebox.showinfo("cadastro","CPF já cadastrado")
                elif valorCPF not in usuariosCadastrados:
                    adicionandoArquivo = open("usuarios.txt","a")
                    adicionandoArquivo.write(valorNome)
                    adicionandoArquivo.write(valorCPF)
                    adicionandoArquivo.write(valorSenha)
                    adicionandoArquivo.write("1\n")
                    msg = tkinter.messagebox.showinfo("cadastro","Usuário cadastrado com sucesso!")
                    adicionandoArquivo.close()               
    if acesso == False:
        msg = tkinter.messagebox.showinfo("cadastrado","Autorização do administrador não autenticada")
def cadastrar():
    '''
    Essa função cria a janela de cadastro de novos usuários
    '''
          
    janelaCadastro = Tk()
    janelaCadastro.configure(background="#0A1829")
    janelaCadastro.title("Cadastro")

    #elementos da tela
    cadastro = Label(janelaCadastro, text="------ Cadastro ------")
    cadastro.pack()
    nome = Label(janelaCadastro, text=" Nome ")
    nome.pack()
    cpf  = Label(janelaCadastro, text=" CPF ")
    cpf.pack()
    senha = Label(janelaCadastro, text="Senha ")
    senha.pack()
    autorizacaoAdm  = Label(janelaCadastro, text="Autorização do administrador")
    autorizacaoAdm.pack() 
    global entradaNome
    global entradaCPF
    global entradaSenha
    global entradaAdm
    global entradaAdm
    entradaNome = Entry(janelaCadastro,)
    entradaCPF  = Entry(janelaCadastro,)
    entradaSenha = Entry(janelaCadastro, show="*")
    entradaAdm = Entry(janelaCadastro, show="*")
    

    botaoCadastrar = Button(janelaCadastro, text="Cadastrar",command= botao_click)

    #posição na tela
    cadastro.place(relx=0.23, rely=0.07, height=21, width=170)
    nome.place(relx=0.20, rely=0.17, height=21, width=37)
    cpf.place(relx=0.20, rely=0.29, height=21, width=27)
    senha.place(relx=0.20, rely=0.41, height=21, width=37)
    autorizacaoAdm.place(relx=0.20, rely=0.53, height=21, width=160)

    entradaNome.place(relx=0.21, rely=0.22, height=21, width=180)
    entradaCPF.place(relx=0.21, rely=0.34, height=21, width=180)
    entradaSenha.place(relx=0.21, rely=0.46, height=21, width=180)
    entradaAdm.place(relx=0.21, rely=0.58, height=21, width=180)

    botaoCadastrar.place(relx=0.33, rely=0.66, height=21, width=90)

    #cores de fundo/letras 
    cadastro.configure(background="#0A1829")
    cadastro.configure(foreground="#fdfdfd")
    nome.configure(background="#0A1829")
    nome.configure(foreground="#fdfdfd")
    cpf.configure(background="#0A1829")
    cpf.configure(foreground="#fdfdfd")
    autorizacaoAdm.configure(background="#0A1829")
    autorizacaoAdm.configure(foreground="#fdfdfd")
    senha.configure(background="#0A1829")
    senha.configure(foreground="#fdfdfd")
    
    botaoCadastrar.configure(background="#63e276")
        
    janelaCadastro.geometry("300x400+200+200")
    janelaCadastro.mainloop()



############################################################       
def limpar():
    '''
    Essa função limpa a tela
    '''
    Frame1.destroy()     
    
class Primeiro_Painel:
    def login(self):
        dadosSenha= self.entradaSenha.get()
        dadosLogin= self.entradaCPF.get()
        senha = dadosSenha
        acesso = dadosLogin
        dadosSenha += "\n"
        dadosLogin += "\n"
        arquivo()
        
        if senha == "adm" and acesso == "adm":
            nivelAcesso = 4
            msg = tkinter.messagebox.showinfo("Primeiro Painel","Login realizado com sucesso!")
            acessoNivel_04()
        global palavrasChaves
        palavrasChaves = usuariosCadastrados.keys()
        login = False
        for chaves in palavrasChaves:
            if dadosLogin == chaves and dadosSenha == usuariosCadastrados[chaves][1]:
                 nivelAcesso = usuariosCadastrados[chaves][2]
                 if nivelAcesso == "1\n":
                     msg = tkinter.messagebox.showinfo("Primeiro Painel","Login realizado com sucesso!")
                     acessoNivel_01()
                 elif nivelAcesso == "2\n":
                    msg = tkinter.messagebox.showinfo("Primeiro Painel","Login realizado com sucesso!")
                    acessoNivel_02()                    
                 elif nivelAcesso == "3\n":
                    msg = tkinter.messagebox.showinfo("Primeiro Painel","Login realizado com sucesso!")
                    acessoNivel_03()                     
                 elif nivelAcesso == "4\n":
                    #msg = tkinter.messagebox.showinfo("Primeiro Painel","Login realizado com sucesso!")
                    acessoNivel_04()
                 login = True
        if login == False:
           msg = tkinter.messagebox.showinfo("Primeiro Painel","Login ou senha incorretos!")
        #elif login == True:
        #   Primeiro_Painel()
    
            

    def cadastrar_usuario(self):
        cadastrar()
    
    def Primeiro_Painel():
        global w
        w.destroy()
        w = None
   
    def __init__(self, top=None): #funÃ§Ãµes reservadas em python (construtora de objetos)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("772x508+458+154")
        top.title("Login")
        top.configure(background="#d9d9d9")

        global Frame1
        Frame1 = Frame(top) 
        Frame1.place(relx=0.03, rely=0.04, relheight=0.95, relwidth=0.95)
        Frame1.configure(relief=GROOVE)
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief=GROOVE)
        Frame1.configure(background="#0A1829")
        Frame1.configure(width=2000)

        self.cpf = Label(Frame1,)
        self.cpf.place(relx=0.39, rely=0.17, height=21, width=27)
        self.cpf.configure(background="#0A1829")
        self.cpf.configure(disabledforeground="#a3a3a3")
        self.cpf.configure(foreground="#f9f9f9")
        self.cpf.configure(text='''CPF''')

        self.senha = Label(Frame1,)
        self.senha.place(relx=0.39, rely=0.28, height=21, width=38)
        self.senha.configure(background="#0A1829")
        self.senha.configure(disabledforeground="#a3a3a3")
        self.senha.configure(foreground="#fdfdfd")
        self.senha.configure(text='''Senha''')

        self.entradaCPF = Entry(Frame1,)
        self.entradaCPF.place(relx=0.39, rely=0.22, relheight=0.04
                , relwidth=0.22)
        self.entradaCPF.configure(background="white")
        self.entradaCPF.configure(disabledforeground="#a3a3a3")
        self.entradaCPF.configure(font="TkFixedFont")
        self.entradaCPF.configure(foreground="#000000")
        self.entradaCPF.configure(insertbackground="black")
        a = self.entradaCPF.get()
        self.entradaCPF.configure()

        self.entradaSenha = Entry(Frame1, show ="*")
        self.entradaSenha.place(relx=0.39, rely=0.32, relheight=0.04
                , relwidth=0.22)
        self.entradaSenha.configure(background="white")
        self.entradaSenha.configure(disabledforeground="#a3a3a3")
        self.entradaSenha.configure(font="TkFixedFont")
        self.entradaSenha.configure(foreground="#000000")
        self.entradaSenha.configure(insertbackground="black")

        self.botaoLogin = Button(Frame1,command=self.login)
        self.botaoLogin.place(relx=0.40, rely=0.41, height=24, width=147)
        self.botaoLogin.configure(activebackground="#d9d9d9")
        self.botaoLogin.configure(activeforeground="#000000")
        self.botaoLogin.configure(background="#63e276")
        self.botaoLogin.configure(disabledforeground="#a3a3a3")
        self.botaoLogin.configure(foreground="#000000")
        self.botaoLogin.configure(highlightbackground="#d9d9d9")
        self.botaoLogin.configure(highlightcolor="black")
        self.botaoLogin.configure(pady="0")
        self.botaoLogin.configure(text='''Entrar''')
        self.botaoLogin.configure(width=147)

        self.labelCadastro = Label(Frame1)
        self.labelCadastro.place(relx=0.39, rely=0.49, height=21, width=105)
        self.labelCadastro.configure(background="#0A1829")
        self.labelCadastro.configure(disabledforeground="#a3a3a3")
        self.labelCadastro.configure(foreground="#ffffff")
        self.labelCadastro.configure(text='''Não tem cadastro?''')

        self.botaoCadastrar = Button(Frame1,command=self.cadastrar_usuario)
        self.botaoCadastrar.place(relx=0.39, rely=0.56, height=24, width=73)
        self.botaoCadastrar.configure(activebackground="#d9d9d9")
        self.botaoCadastrar.configure(activeforeground="#000000")
        self.botaoCadastrar.configure(background="#d9d9d9")
        self.botaoCadastrar.configure(disabledforeground="#a3a3a3")
        self.botaoCadastrar.configure(foreground="#000000")
        self.botaoCadastrar.configure(highlightbackground="#d9d9d9")
        self.botaoCadastrar.configure(highlightcolor="black")
        self.botaoCadastrar.configure(pady="0")
        self.botaoCadastrar.configure(text='''Cadastre-se''')
if __name__ == '__main__':
    vp_start_gui()




