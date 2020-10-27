from tkinter import *
from Calculadora import *

from Indicadores import *

class Form:
    inid = Indicadores()

    def __init__(self):
        self.root = Tk()
        self.calculadora = Calculadora()

        self.dolares = StringVar()

        self.n1 = StringVar()
        self.n2 = StringVar()
        self.resultado = StringVar()



        self.formulario()


    def sumar(self):
        self.resultado.set( self.calculadora.suma( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()
        print("Se realizó una suma")

    def restar(self):
        self.resultado.set( self.calculadora.resta( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()
        print("Se realizó una resta")

    def multiplicar(self):
        self.resultado.set( self.calculadora.multiplicacion( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()
        print("Se realizó una multiplicación")

    def dividir(self):
        self.resultado.set( self.calculadora.division( float(self.n1.get()), float(self.n2.get()) ))
        self.borrar()
        print("Se realizó una división")


    def borrar(self):
        self.n1.set("")
        self.n2.set("")



    def divisas(self):
        trm = self.inid.trm()
        self.resultado.set(
            round(
            float(trm) * float(self.dolares.get()),
            3
            )
        )


    def formulario(self): #BOTONES
        self.root.config(bd=20)

        Label(self.root, text="Valor en dolares").pack()
        Entry(self.root, textvariable = self.dolares).pack()

        Label(self.root, text="Número 1").pack()
        Entry(self.root, textvariable = self.n1).pack()

        Label(self.root, text="Número 2").pack()
        Entry(self.root, textvariable = self.n2).pack()

        Label(self.root, text="Resultado").pack()
        Entry(self.root, textvariable = self.resultado, state = 'disabled').pack()


        Button(self.root, text='+', command = self.sumar).pack(side="left")
        Button(self.root, text='-', command = self.restar).pack(side="left")
        Button(self.root, text='*', command = self.multiplicar).pack(side="left")
        Button(self.root, text='/', command = self.dividir).pack(side="left")

        Button(self.root, text='Valor en Pesos', command = self.divisas).pack(side="left")


        self.root.mainloop()
