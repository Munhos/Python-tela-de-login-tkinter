from tkinter import *
import tkinter as tk
import json 

root = Tk()

class janela_principal():
    global solto
    global pressionado
    
    def __init__(self) -> None:

        self.root = root
        
        self.root.geometry("700x500")
        self.root.title("Tela de Login")
        self.root.resizable(False, False)

        texto_login = Label(root, text="LOGIN", font="Varane 40")
        texto_login.pack(pady=30)
        

        texto_email = Label(root, text="Digite seu e-mail:", font="Agency_FB")
        texto_email.place(x= 30, y= 150)
        texto_senha = Label(root, text="Digite sua senha:", font="Agency_FB")
        texto_senha.place(x= 30, y= 220)
        

        self.email_selecionado = Entry(root)
        self.email_selecionado.place(x= 30, y= 180, width= 640, height=20)
        self.senha_selecionada = Entry(root, show="*")
        self.senha_selecionada.place(x= 30, y= 250, width= 640, height=20)

        botao_logar = Button(root, text="Logar", command=self.verificar_cadastro)
        botao_logar.place(x= 30, y= 350, width= 640, height=50)
        botao_nova_conta = Button(root, text="Criar conta", command=self.direcionar_nova_conta)
        botao_nova_conta.place(x= 30, y= 400, width= 640, height=50)

        self.botao_mostrar_senha = Button(root, text="Mostrar Senha", state="disabled")
        self.botao_mostrar_senha.place(x=30, y = 280, height=20)

        self.botao_mostrar_senha.bind("<ButtonPress-1>", pressionado)
        self.botao_mostrar_senha.bind("<ButtonRelease-1>", solto)

    def direcionar_nova_conta(self):
        tela_nova_conta(window_2)

    def pressionado(event):
        global senha_34
        main_window.botao_mostrar_senha.config(state="normal")

        senha_digitando = main_window.senha_selecionada.get()

     
        senha_34 = Entry(root)
        senha_34.place(x= 30, y= 250, width= 640, height=20)
        senha_34.insert(0, senha_digitando)

    def solto(event):
        main_window.botao_mostrar_senha.config(state="disabled")

        senha_34.destroy()

    def verificar_cadastro(self):
        msg_login = StringVar()

        aviso_login = Label(root, textvariable=msg_login)
        aviso_login.place(x= 30, y= 300, width= 640, height=50)

        senha_selecionado = main_window.senha_selecionada.get()
        email_selecionado = main_window.email_selecionado.get()

        with open("Banco_Dados.json") as d:
            Ler_BD = json.load(d)

        
        for c in range(len(Ler_BD)):
            if email_selecionado in Ler_BD[c]:
                if senha_selecionado == Ler_BD[c][email_selecionado]["SENHA"]:
                    usuario = Ler_BD[c][email_selecionado]["USUARIO"]
                    print("Login aprovado")
                    Frame(root).place(x=0, y=0, height=500 , width=700)

                    usuario = "Bem vindo " + usuario
                    print(usuario)
                    texto_bem_vindo = Label(root, text=usuario, font="Varane 40")
                    texto_bem_vindo.pack(pady=30)

                else:
                    print("Login ou senha invalida")
                    msg_login.set("Login ou senha inválida")

            else:
                msg_login.set("Login ou senha inválida")
          
    

    
class janela_secundaria:
    global tela_nova_conta
    global verificar_erros
    global verificar_email
    global carregar_BD
   
    def tela_nova_conta(self):
        
        
        self.fundo_tela2 = Frame(root)
        self.fundo_tela2.place(x=0, y=0, width=700, height=500)

        self.botao_voltar = Button(root, text="Voltar", command= window_2.destroy_tela_2)
        self.botao_voltar.place(x=10, y=10)
    
        self.texto_novo_cadastro = Label(root, text="NOVO CADASTRO", font="Varane 40")
        self.texto_novo_cadastro.pack(pady=30)

        self.texto_novo_cadastro.place(y=30, x=200)

        self.texto_nome2 = Label(root, text="Digite seu nome:", font="Agency_FB")
        self.texto_nome2.place(x= 30, y= 150)
        self.texto_email2 = Label(root, text="Digite um e-mail válido:", font="Agency_FB")
        self.texto_email2.place(x= 30, y= 220)
        self.texto_senha2 = Label(root, text="Digite uma senha válida:", font="Agency_FB")
        self.texto_senha2.place(x= 30, y= 290)
    
        self.input_nome = Entry(root)
        self.input_nome.place(x= 30, y= 180, width= 640, height=20)
        self.input_email = Entry(root)
        self.input_email.place(x= 30, y= 250, width= 640, height=20)
        self.input_senha = Entry(root)
        self.input_senha.place(x= 30, y= 320, width= 640, height=20)

        self.botao_nova_conta = Button(root, text="Criar conta", command=window_2.novo_cadastro)
        self.botao_nova_conta.place(x= 30, y= 400, width= 640, height=50)

       
        self.msg_erro = StringVar()
        self.msg_aviso = Label(root, textvariable=window_2.msg_erro)
        self.msg_aviso.place(x= 30, y= 350, width= 640, height=50)

        
    def destroy_tela_2(self):

        widgets = (window_2.fundo_tela2, window_2.botao_voltar, window_2.texto_novo_cadastro, window_2.botao_nova_conta, window_2.input_email, window_2.input_nome, window_2.input_senha,
        window_2.texto_senha2, window_2.texto_nome2, window_2.texto_email2, window_2.msg_aviso)
        for widget in widgets:
            widget.destroy()

        
    def novo_cadastro(self):

        novo_nome_selecionado = window_2.input_nome.get()
        novo_email_selecionado = window_2.input_email.get()
        novo_senha_selecionado = window_2.input_senha.get()
        verificar_erros()
        if verificar_erros() == False:
            pass
        else:
            if verificar_email(novo_email_selecionado) == True:
                print("Email ja cadastrado")
                window_2.msg_erro.set("E-mail já cadastrado")
            else:
                try:        
                    with open("Banco_Dados.json") as l:
                        Ler_BD = json.load(l)
                    with open("Banco_Dados.json", "w") as f:

                        
                        data = [{novo_email_selecionado:{"USUARIO":novo_nome_selecionado, "SENHA":novo_senha_selecionado}}]
                        
                        data = Ler_BD + data
                        json.dump(data, f, indent=4)

                        window_2.msg_erro.set("Sucesso!")

                        window_2.input_email.delete(0,END)
                        window_2.input_senha.delete(0,END)
                        window_2.input_nome.delete(0,END)

                        window_2.botao_nova_conta.destroy()
                except:
                    with open("Banco_Dados.json", "w") as f:
                        str(window_2.input_email) 
                        str(window_2.input_nome)
                        str(window_2.input_senha)
                        data = [{novo_email_selecionado:{"USUARIO":novo_nome_selecionado, "SENHA":novo_senha_selecionado}}]
                        json.dump(data, f, indent=4)

                        window_2.msg_erro.set("Sucesso!")

                        window_2.input_email.delete(0,END)
                        window_2.input_senha.delete(0,END)
                        window_2.input_nome.delete(0,END)

                        window_2.botao_nova_conta.destroy()


    def verificar_email(email):
        try:

            with open("Banco_Dados.json") as l:
                Ler_BD = json.load(l)

        
            for c in range(len(Ler_BD)):
                if email in Ler_BD[c]:
                    return True
                else:
                    return False
        except:
            return False


    def verificar_erros():
        novo_nome_selecionado = window_2.input_nome.get()
        novo_email_selecionado = window_2.input_email.get()
        novo_senha_selecionado = window_2.input_senha.get()

        if novo_nome_selecionado == "":
            print("nome em branco")
            window_2.msg_erro.set("Nome em Branco")
            return False
            

        elif novo_email_selecionado == "":
            print("email em branco")
            window_2.msg_erro.set("E-mail em Branco")
            return False

        elif novo_senha_selecionado == "":
            print("senha em branco")
            window_2.msg_erro.set("Senha em Branco")
            return False
                
        elif novo_senha_selecionado == novo_email_selecionado or novo_senha_selecionado == novo_nome_selecionado:
            print("selecione uma senha diferente do email ou usuario")
            window_2.msg_erro.set("Selecione uma senha diferente do email ou usuario")
            return False
                        
        elif "@" not in novo_email_selecionado:
            print("email invalido")
            window_2.msg_erro.set("E-mail invalido (sem @)")
            return False

        else:
            return True
                                                  

main_window = janela_principal()
window_2 = janela_secundaria()
root.mainloop()