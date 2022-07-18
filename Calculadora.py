# importando o tkinter
from cProfile import label
from re import T              #biblioteca
from tkinter import *         #biblioteca
from tkinter import ttk       #biblioteca

#cores
cor1="#1f2420" #preta
cor2="#e6ede8" #branca
cor3="#404169" #azul
cor4="#abdbc3" #cizenta
cor5="#ed901f" #laranja


janela =Tk()
janela.title("Daniel Gostoso cal") #titulo 
janela.geometry("235x310") # tamanho largura ecomprimento
janela.config(bg=cor1)

#criando frames
frame_tela=Frame(janela, width=235, height=50, bg=cor3) #tela da calculadora
frame_tela.grid(row=0,column=0) # tela da calculadora

frame_corpo=Frame(janela, width=235, height=268) #corpo da calculadora
frame_corpo.grid(row=1,column=0) #corpo da calculadora


# variavel todos valores
todos_valores=""

#criando label
valor_texto=StringVar()

#criando_funçoes
def entrar_valores(event):

    global todos_valores

    todos_valores= todos_valores + str(event)
    
    #passando valor para a frame_tela
    valor_texto.set(todos_valores)


# funçao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


#funçao limpa tela
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")


app_label=Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#criando botoes  /    # x= botoes lateral/ y= botoes colunas
# 1° botao                   botao c
b_1= Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)      #x= vaiser o 0 lateral/ y= 0 colunas
# 2° botao                   botao %
b_2= Button(frame_corpo, command= lambda: entrar_valores("%"), text="%", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)  
# 3° botao                    botao /
b_3= Button(frame_corpo, command= lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0) 

# botoes  de 7 a 9 e *
# 4° botao                   botao 7
b_4= Button(frame_corpo, command= lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)  
#5° botao                   botao 8
b_5= Button(frame_corpo, command= lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
#6° botao                   botao 9
b_6= Button(frame_corpo, command= lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)  
# botao "*"                botao *
b_7= Button(frame_corpo, command= lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52) 

#botoes de 4 a 6 e - 
b_8= Button(frame_corpo, command= lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)  
#5° botao                   botao 8
b_9= Button(frame_corpo, command= lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
#6° botao                   botao 9
b_10= Button(frame_corpo, command= lambda: entrar_valores("6"), text="6", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)  
# botao "*"                botao *
b_11= Button(frame_corpo, command= lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104) 

# botoes de 1 a 3 e +
b_12= Button(frame_corpo, command= lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)  
#5° botao                   botao 8
b_13= Button(frame_corpo, command= lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
#6° botao                   botao 9
b_14= Button(frame_corpo, command= lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)  
# botao "*"                botao *
b_15= Button(frame_corpo, command= lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156) 

# botoes de 0 . =            botao 0                                                      
b_16= Button(frame_corpo, command= lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)      #x= vaiser o 0 lateral/ y= 0 colunas
# 2° botao                   botao .
b_17= Button(frame_corpo, command= lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)  
# 3° botao                    botao =
b_18= Button(frame_corpo, command= calcular,  text="=", width=5, height=2, bg=cor5, fg=cor2,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208) 



janela.mainloop()


