from tkinter import *
import tkinter as tk

root = Tk()



class janela_principal():
    global substituir_caracteres, senha_selecionada
    global tela_nova_conta
    global destroy_tela_2
    global solto
    global pressionado
    
    def __init__(self) -> None:

        self.root = root
        
        self.root.geometry("700x500")
        self.root.title("Tela de Login")
        self.root.resizable(False, False)

        global email_selecionado, senha_selecionada, botao_mostrar_senha
        texto_login = Label(root, text="LOGIN", font="Varane 40")
        texto_login.pack(pady=30)
        #texto_login.place(y=30, x=295)

        texto_email = Label(root, text="Digite seu e-mail:", font="Agency_FB")
        texto_email.place(x= 30, y= 150)
        texto_senha = Label(root, text="Digite sua senha:", font="Agency_FB")
        texto_senha.place(x= 30, y= 220)
        

        email_selecionado = Entry(root)
        email_selecionado.place(x= 30, y= 180, width= 640, height=20)
        senha_selecionada = Entry(root, show="*")
        senha_selecionada.place(x= 30, y= 250, width= 640, height=20)

        botao_logar = Button(root, text="Logar", command=verificar_cadastro)
        botao_logar.place(x= 30, y= 350, width= 640, height=50)
        botao_nova_conta = Button(root, text="Criar conta", command=tela_nova_conta)
        botao_nova_conta.place(x= 30, y= 400, width= 640, height=50)

        botao_mostrar_senha = Button(root, text="Mostrar Senha", state="disabled")
        botao_mostrar_senha.place(x=30, y = 280, height=20)

        botao_mostrar_senha.bind("<ButtonPress-1>", pressionado)
        botao_mostrar_senha.bind("<ButtonRelease-1>", solto)


    def pressionado(event):
        global senha_34, senha_digitando
        botao_mostrar_senha.config(state="normal")

        senha_digitando = senha_selecionada.get()

     
        senha_34 = Entry(root)
        senha_34.place(x= 30, y= 250, width= 640, height=20)
        senha_34.insert(0, senha_digitando)

    def solto(event):
        botao_mostrar_senha.config(state="disabled")

        senha_34.destroy()

        
    

    
 
    
    def tela_nova_conta():
        global fundo_tela2
        global botao_voltar
        global texto_novo_cadastro
        global texto_nome2, texto_email2, texto_senha2
        
        fundo_tela2 = Frame(root)
        fundo_tela2.place(x=0, y=0, width=700, height=500)

        botao_voltar = Button(root, text="Voltar", command=destroy_tela_2)
        botao_voltar.place(x=10, y=10)
    
        texto_novo_cadastro = Label(root, text="NOVO CADASTRO", font="Varane 40")
        texto_novo_cadastro.pack(pady=30)

        texto_novo_cadastro.place(y=30, x=200)

        texto_nome2 = Label(root, text="Digite seu nome:", font="Agency_FB")
        texto_nome2.place(x= 30, y= 150)
        texto_email2 = Label(root, text="Digite um e-mail válido:", font="Agency_FB")
        texto_email2.place(x= 30, y= 220)
        texto_senha2 = Label(root, text="Digite uma senha válida:", font="Agency_FB")
        texto_senha2.place(x= 30, y= 290)
        

        global input_email, input_nome, input_senha, msg_erro, botao_nova_conta, msg_aviso

        input_nome = Entry(root)
        input_nome.place(x= 30, y= 180, width= 640, height=20)
        input_email = Entry(root)
        input_email.place(x= 30, y= 250, width= 640, height=20)
        input_senha = Entry(root)
        input_senha.place(x= 30, y= 320, width= 640, height=20)

        botao_nova_conta = Button(root, text="Criar conta", command=novo_cadastro)
        botao_nova_conta.place(x= 30, y= 400, width= 640, height=50)

       
        msg_erro = StringVar()
        msg_aviso = Label(root, textvariable=msg_erro)
        msg_aviso.place(x= 30, y= 350, width= 640, height=50)

        
    def destroy_tela_2():
        

        widgets = (fundo_tela2, botao_voltar, texto_novo_cadastro, botao_nova_conta, input_email, input_nome, input_senha,
        texto_senha2, texto_nome2, texto_email2, msg_aviso)
        for widget in widgets:
            widget.destroy()

        
def novo_cadastro():

    novo_nome_selecionado = input_nome.get()
    novo_email_selecionado = input_email.get()
    novo_senha_selecionado = input_senha.get()

    with open("banco_dados_tela_login.txt", "r") as banco_dados:
        banco_dados1 = banco_dados.read()

        if novo_nome_selecionado == "":
            print("nome em branco")
            msg_erro.set("Nome em Branco")
        else:
            if novo_email_selecionado == "":
                print("email em branco")
                msg_erro.set("E-mail em Branco")
            else:
                if novo_senha_selecionado == "":
                    print("senha em branco")
                    msg_erro.set("Senha em Branco")
                else:
                    if novo_senha_selecionado == novo_email_selecionado or novo_senha_selecionado == novo_nome_selecionado:
                        print("selecione uma senha diferente do email ou usuario")
                        msg_erro.set("Selecione uma senha diferente do email ou usuario")
                    else:
                        if "@" in novo_email_selecionado:
                            emailvalido = True
                        else:
                            emailvalido =  False
                        

                        if emailvalido == False:
                            print("email invalido")
                            msg_erro.set("E-mail invalido (sem @)")
                        elif emailvalido == True:
                            if len(novo_nome_selecionado) > 10:
                                print("Nome muito longa")
                                msg_erro.set("Nome maior que 10 caracteres")
                            else:
                                if len(novo_email_selecionado) > 30:
                                    print("email muito longa")
                                    msg_erro.set("E-mail maior que 30 caracteres")
                                else:
                                    
                                    if len(novo_senha_selecionado) > 20:
                                        print("Senha muito longa")
                                        msg_erro.set("Senha maior que 20 caracteres")
                                    else:
                                        n_caracteres_email = len(novo_email_selecionado)
                                        n_caracteres_email = int(n_caracteres_email)

                                        if  novo_email_selecionado in banco_dados1:
                                            print("E-mail já cadastrado")
                                            msg_erro.set("E-mail já cadastrado")
                                        else:
                                           
                                            n_caracteres_nome = int(len(novo_nome_selecionado))
                                            n_caracteres_email = int(len(novo_email_selecionado))
                                            n_caracteres_senha = int(len(novo_senha_selecionado))

                                          
                                            
                                            with open("banco_dados_tela_login.txt", "a") as banco_dados_2:
                                                if banco_dados1 == "":
                                                    pass
                                                else:
                                                    banco_dados_2.write("\n")
                                                banco_dados_2.write(novo_nome_selecionado)
                                                banco_dados_2.write("."*(10-n_caracteres_nome))
                                                banco_dados_2.write(novo_email_selecionado)
                                                banco_dados_2.write("."*(30-n_caracteres_email))
                                                banco_dados_2.write(novo_senha_selecionado)
                                                banco_dados_2.write("."*(20-n_caracteres_senha))

                                                msg_erro.set("Sucesso!")

                                                input_email.delete(0,END)
                                                input_senha.delete(0,END)
                                                input_nome.delete(0,END)

                                                botao_nova_conta.destroy()

def verificar_cadastro():
    msg_login = StringVar()
    with open("banco_dados_tela_login.txt", "r") as banco_dados:
        banco_dados = banco_dados.read()
        novo_email_selecionado = email_selecionado.get()
        novo_senha_selecionado = senha_selecionada.get()

        aviso_login = Label(root, textvariable=msg_login)
        aviso_login.place(x= 30, y= 300, width= 640, height=50)
        
        if novo_email_selecionado in banco_dados:
            n_caracteres_email = int(len(novo_email_selecionado))
            n_caracteres_senha = int(len(novo_senha_selecionado))
            novo_email_selecionado = novo_email_selecionado+"."*(30-n_caracteres_email)
            posi_email = banco_dados.find(novo_email_selecionado)

            if banco_dados[posi_email:posi_email+30] == novo_email_selecionado:
                print("E-mail passou")
                
                if banco_dados[posi_email+30:posi_email+50] == novo_senha_selecionado+"."*(20-n_caracteres_senha):
                    print("senha passou, aprovado")
                    Frame(root).place(x=0, y=0, height=500 , width=700)

                    usuario = "Bem vindo "+banco_dados[posi_email-10: posi_email]
                    usuario = usuario.replace(".", "")
                    print(usuario)
                    texto_bem_vindo = Label(root, text=usuario, font="Varane 40")
                    texto_bem_vindo.pack(pady=30)
                    #texto_bem_vindo.place(y=30, x=200)

                
                else:
                    print("Senha inválida")
                    msg_login.set("Senha inválida")

            else:
                if novo_email_selecionado == "":
                    msg_login.set("E-mail em branco")
                else:

                    msg_login.set("E-mail inválido")

        else:
            msg_login.set("E-mail não encontrado na base de dados")
            


    

                                            

janela_principal()
root.mainloop()