from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font

dicCursos = {}

 #######################METODO PARA LA SUMATORIA DE CRÉDITOS################################   
def sumaCredito():
        sumaCredito = 0  
        for i in dicCursos.values():
            if(i[5]=="0"):
                sumaCredito += int(i[4])
            else:
                print("el curso: " + i[0] + " no tiene créditos")  
        print("total de créditos: " + str(sumaCredito))
        return sumaCredito

#sumaCredito()

'''MENU PRINCIPAL / PANTALLA 1'''
class MenuPrincipal():
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Menú Principal")
        self.Centrar(self.ventana, 600, 600)
        self.ventana.geometry('600x600')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=50, pady=50)
        Label(self.frame, text="Menú Principal - Pensum Ingeniería", font=('Segoe UI',20), fg='#FDFEFE', bg='#00747C', width=60).place(x=250, y=50, anchor="center")
        Label(self.frame, text="Lenguajes Formales y de Programación 1 B+", font=('Segoe UI',15), fg='#FDFEFE', bg='#00747C', width=50).place(x=250, y=90, anchor="center")
        Label(self.frame, text="Lusvin Alexander Sicajá Ramírez", font=('Segoe UI',10), fg='#FDFEFE', bg='#00747C', width=50).place(x=250, y=120, anchor="center")
        Label(self.frame, text="Carnet: 201602630", font=('Segoe UI',10), fg='#FDFEFE', bg='#00747C', width=20).place(x=250, y=140, anchor="center")
        Label(self.frame, text="", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=69, height=18).place(x=250, y=340, anchor="center")
        Button(self.frame, text="Cargar Archivo", command=self.cargarArchivo , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=125, y=300, anchor="center")
        Button(self.frame, text="Gestionar Cursos", command=self.btnGestionar , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=375, y=300, anchor="center")
        Button(self.frame, text="Conteo de Créditos", command=self.btnConteo , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=125, y=400, anchor="center")
        Button(self.frame, text="Salir", command=self.salir , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=20).place(x=375, y=400, anchor="center")
        
        self.frame.mainloop()
    
    def cargarArchivo(self):
        nombreArchivo = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo de Cursos", filetypes=(("archivo lfp", "*.lfp"),))
        if nombreArchivo!='':
            with open(nombreArchivo, "r", encoding="utf-8") as archivo:
            #FOR PARA CREAR DICCIONARIO DESDE ARCHIVO
                for linea in archivo:
                    linea = linea.rstrip("\n")
                    campos = linea.split(",")
                    valores = [campos[1], campos[2], campos[3], campos[4], campos[5], campos[6]]
                    dicCursos[campos[0]]=valores
            messagebox.showinfo(message="El archivo se cargo correctamente", title="Carga de archivo")
        else:
            messagebox.showinfo(message="El archivo NO se cargo correctamente \n Intente nuevamente", title="Carga de archivo")

    def salir(self):
        self.ventana.destroy()
        
    def btnGestionar(self):
        self.ventana.destroy()
        Cursos()
        
    def btnConteo(self):
        self.ventana.destroy()
        CursosConteo()
       
'''GESTIONAR CURSOS / PANTALLA 2 ++++++++++++++++++++++++++++++++++++'''
class Cursos():
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Gestionar Cursos")
        self.Centrar(self.ventana, 600, 600)
        self.ventana.geometry('600x600')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=50, pady=50)
        Label(self.frame, text="Gestionar Cursos - Facultad de Ingeniería", font=('Segoe UI',15), fg='#FDFEFE', bg='#00747C', width=50).place(x=250, y=50, anchor="center")
        Label(self.frame, text="", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=69, height=22).place(x=250, y=290, anchor="center")
        
        Button(self.frame, text="Listar Cursos", command=self.btnlistarCursos , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=25).place(x=250, y=150, anchor="center")
        Button(self.frame, text="Mostrar Curso Individual", command=self.btnMostrar , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=25).place(x=250, y=200, anchor="center")
        Button(self.frame, text="Agregar Curso Individual", command=self.btnCrear , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=25).place(x=250, y=250, anchor="center")
        Button(self.frame, text="Editar Curso Individual", command=self.btnEditar , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=25).place(x=250, y=300, anchor="center")
        Button(self.frame, text="Eliminar Curso Individual", command=self.btnEliminar , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=25).place(x=250, y=350, anchor="center")
        Button(self.frame, text="Regresar al Menú Principal", command=self.btnMenuprincipal , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=30).place(x=250, y=420, anchor="center")
        
        self.frame.mainloop()
    
    def btnMenuprincipal(self):
        self.ventana.destroy()
        MenuPrincipal()
    
    def btnlistarCursos(self):
        self.ventana.destroy()
        ListarCursos()
    
    def btnMostrar(self):
        self.ventana.destroy()
        MostrarCurso()

    def btnCrear(self):
        self.ventana.destroy()
        CrearCurso()
    
    def btnEditar(self):
        self.ventana.destroy()
        EditarCurso()
        
    def btnEliminar(self):
        self.ventana.destroy()
        EliminarCurso()
        
'''CONTEO DE CRÉDITOS / PANTALLA 3 ++++++++++++++++++++++++++++++++++'''
class CursosConteo():
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Conteo de Cursos")
        self.Centrar(self.ventana, 600, 600)
        self.ventana.geometry('600x600')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=50, pady=50)
        Label(self.frame, text="Conteo de Cursos - Facultad de Ingeniería", font=('Segoe UI',15), fg='#FDFEFE', bg='#00747C', width=50).place(x=250, y=48, anchor="center")
        Label(self.frame, text="", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=69, height=25).place(x=250, y=280, anchor="center")
        
        Label(self.frame, text="Créditos Aprobados: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=30).place(x=150, y=100, anchor="center")
        Label(self.frame, text="Créditos Cursando: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=30).place(x=150, y=130, anchor="center")
        Label(self.frame, text="Créditos Pendientes: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=30).place(x=150, y=160, anchor="center")
              
        Label(self.frame, text="_________________________________________________________________________________________", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=60).place(x=250, y=180, anchor="center")
        Label(self.frame, text="Créditos Obligatorios hasta el semestre seleccionado: ", font=('Segoe UI',12), fg='#FDFEFE', bg='#202022', width=50).place(x=250, y=210, anchor="center")
        Label(self.frame, text="Seleccione Semestre...", font=('Segoe UI',10), fg='#FDFEFE', bg='#00BBC9', width=20).place(x=100, y=240, anchor="center")
        Label(self.frame, text="Créditos:", font=('Segoe UI',10), fg='#FDFEFE', bg='#00BBC9', width=10).place(x=380, y=240, anchor="center")
        Button(self.frame, text="Contar", command=self.conteos , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=8).place(x=290, y=242, anchor="center")

        Label(self.frame, text="_________________________________________________________________________________________", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=60).place(x=250, y=270, anchor="center")
        Label(self.frame, text="Créditos del semestre seleccionado: ", font=('Segoe UI',12), fg='#FDFEFE', bg='#202022', width=50).place(x=250, y=300, anchor="center")
        Label(self.frame, text="Seleccione Semestre...", font=('Segoe UI',10), fg='#FDFEFE', bg='#00BBC9', width=20).place(x=100, y=330, anchor="center")
        Label(self.frame, text="Créditos:", font=('Segoe UI',10), fg='#FDFEFE', bg='#00BBC9', width=10).place(x=380, y=330, anchor="center")
        Button(self.frame, text="Contar", command=self.conteos , font=('Segoe UI',10), fg='#000000', bg='#CACACA', width=8).place(x=290, y=332, anchor="center")

        Button(self.frame, text="Regresar al Menú Principal", command=self.btnMenuprincipal , font=('Segoe UI',15), fg='#000000', bg='#CACACA', width=30).place(x=250, y=420, anchor="center")
        
        self.frame.mainloop()
            
    def btnMenuprincipal(self):
        self.ventana.destroy()
        MenuPrincipal()
    
    def conteos(self):
        print("estoy contando cursos...")

'''GC-LISTAR CURSOS''' 
class ListarCursos():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Cursos")
        self.Centrar(self.ventana, 550, 400)
        self.ventana.geometry('550x400')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()


    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=390, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Listado Cursos - Facultad de Ingeniería", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        tabla = ttk.Treeview(self.frame, columns=("col1","col2", "col3", "col4", "col5", "col6"))
        tabla.place(x=250, y=160, anchor="center")
        
        style = ttk.Style()
        style.configure(
            'Treeview',
            background = 'white',
            foreground = '#202022',
            rowheight = 20,
            fielbackground = 'silver'
        )
        style.map(
            'Treeview',
            background = [('selected', '#00747C')]
        )
        
        tabla.column("#0",width=55)
        tabla.column("col1",width=110, anchor=CENTER)
        tabla.column("col2",width=80, anchor=CENTER)
        tabla.column("col3",width=60, anchor=CENTER)
        tabla.column("col4",width=60, anchor=CENTER)
        tabla.column("col5",width=60, anchor=CENTER)
        tabla.column("col6",width=50, anchor=CENTER)

        tabla.heading("#0", text="Codigo", anchor=CENTER)
        tabla.heading("col1", text="Nombre de Curso", anchor=CENTER)
        tabla.heading("col2", text="Pre-Requisito", anchor=CENTER)
        tabla.heading("col3", text="Opcional", anchor=CENTER)
        tabla.heading("col4", text="Semestre", anchor=CENTER)
        tabla.heading("col5", text="Créditos", anchor=CENTER)
        tabla.heading("col6", text="Estado", anchor=CENTER)
        
        for c in dicCursos:
            valores = dicCursos[c]
            tabla.insert("",END,text=c, values=(valores[0], valores[1], valores[2], valores[3], valores[4], valores[5]))

        Button(self.frame, text="Regresar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=435, y=360, anchor="center")
        self.frame.mainloop()
        
    
    def btnsalir(self):
        self.ventana.destroy()
        Cursos()

'''GC-CREAR CURSOS''' 
class CrearCurso():
       
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Crear Curso")
        self.Centrar(self.ventana, 550, 400)
        self.ventana.geometry('550x400')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()
        
    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
      
        
    def VentanaFrame(self):
                
        def btnAgregar():
            valoresInd = [nombreValor.get(), requisitoValor.get(), opcionalValor.get(), semestreValor.get(), creditosValor.get(), estadoValor.get()]  
            dicCursos[codigoValor.get()] = valoresInd  
            print("agregando curso")
            self.btnsalir()            
        
        self.frame = Frame(height=390, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Agregar Curso - Facultad de Ingeniería", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        Label(self.frame, text="Código: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=60, anchor="center")
        Label(self.frame, text="Nombre: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=100, anchor="center")
        Label(self.frame, text="Pre Requisito: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=140, anchor="center")
        Label(self.frame, text="Semestre: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=180, anchor="center")
        Label(self.frame, text="Opcional: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=220, anchor="center")
        Label(self.frame, text="Créditos: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=260, anchor="center")
        Label(self.frame, text="Estado: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=300, anchor="center")
        
        codigoValor = StringVar()
        nombreValor = StringVar()
        requisitoValor = StringVar()
        semestreValor = StringVar()
        opcionalValor = StringVar()
        creditosValor = StringVar()
        estadoValor = StringVar()
        #e = Entry(self.frame, textvariable=codigoValor, text="codigo", font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=60, anchor="center")

        boxCodigo= Entry(self.frame, textvariable=codigoValor, font=('Segoe UI',10), fg='#000000', width=40).place(x=300, y=60, anchor="center")
        boxNombre = Entry(self.frame, textvariable=nombreValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=100, anchor="center")
        boxRequisito = Entry(self.frame, textvariable=requisitoValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=140, anchor="center")
        boxSemestre = Entry(self.frame, textvariable=semestreValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=180, anchor="center")
        boxOpcional = Entry(self.frame, textvariable=opcionalValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=220, anchor="center")
        boxCreditos = Entry(self.frame, textvariable=creditosValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=260, anchor="center")
        boxEstado = Entry(self.frame, textvariable=estadoValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=300, anchor="center")

        Button(self.frame, text="Cancelar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=435, y=360, anchor="center")
        Button(self.frame, text="Agregar", command=btnAgregar, font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=300, y=360, anchor="center")
  
        self.frame.mainloop()

    def btnsalir(self):
        self.ventana.destroy()
        Cursos()

'''GC-EDITAR CURSOS''' 
class EditarCurso():
       
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Editar Curso")
        self.Centrar(self.ventana, 550, 400)
        self.ventana.geometry('550x400')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()
        
    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
      
        
    def VentanaFrame(self):
                
        def btnAgregar():
            valoresInd = [nombreValor.get(), requisitoValor.get(), opcionalValor.get(), semestreValor.get(), creditosValor.get(), estadoValor.get()]  
            dicCursos[codigoValor.get()] = valoresInd  
            print("agregando curso")
            print(codigoValor.get())
            print(nombreValor.get())
            self.btnsalir()            
        
        self.frame = Frame(height=390, width=500)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Editar Curso - Facultad de Ingeniería", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        Label(self.frame, text="Código: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=60, anchor="center")
        Label(self.frame, text="Nombre: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=100, anchor="center")
        Label(self.frame, text="Pre Requisito: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=140, anchor="center")
        Label(self.frame, text="Semestre: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=180, anchor="center")
        Label(self.frame, text="Opcional: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=220, anchor="center")
        Label(self.frame, text="Créditos: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=260, anchor="center")
        Label(self.frame, text="Estado: ", font=('Segoe UI',10), fg='#FDFEFE', bg='#202022', width=20).place(x=72, y=300, anchor="center")
        
        codigoValor = StringVar()
        nombreValor = StringVar()
        requisitoValor = StringVar()
        semestreValor = StringVar()
        opcionalValor = StringVar()
        creditosValor = StringVar()
        estadoValor = StringVar()
        #e = Entry(self.frame, textvariable=codigoValor, text="codigo", font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=60, anchor="center")

        boxCodigo= Entry(self.frame, textvariable=codigoValor, font=('Segoe UI',10), fg='#000000', width=40).place(x=300, y=60, anchor="center")
        boxNombre = Entry(self.frame, textvariable=nombreValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=100, anchor="center")
        boxRequisito = Entry(self.frame, textvariable=requisitoValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=140, anchor="center")
        boxSemestre = Entry(self.frame, textvariable=semestreValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=180, anchor="center")
        boxOpcional = Entry(self.frame, textvariable=opcionalValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=220, anchor="center")
        boxCreditos = Entry(self.frame, textvariable=creditosValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=260, anchor="center")
        boxEstado = Entry(self.frame, textvariable=estadoValor, font=('Segoe UI',10), fg='#000000', width=40 ).place(x=300, y=300, anchor="center")

        Button(self.frame, text="Cancelar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=435, y=360, anchor="center")
        Button(self.frame, text="Agregar", command=btnAgregar, font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=300, y=360, anchor="center")
  
        self.frame.mainloop()

    def btnsalir(self):
        self.ventana.destroy()
        Cursos()


'''GC-MOSTRAR CURSO''' 
class MostrarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Mostrar Curso")
        self.Centrar(self.ventana, 500, 200)
        self.ventana.geometry('500x200')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=190, width=490)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Curso - Facultad de Ingeniería", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        Button(self.frame, text="Regresar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=420, y=160, anchor="center")
        self.frame.mainloop()
    
    def btnsalir(self):
        self.ventana.destroy()
        Cursos()

'''GC-ELIMINAR CURSO''' 
class EliminarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Practica 1 LFP B+ - Eliminar Curso")
        self.Centrar(self.ventana, 500, 200)
        self.ventana.geometry('500x200')
        self.ventana.configure(bg='#202022')
        self.VentanaFrame()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')
        
    def VentanaFrame(self):
        self.frame = Frame(height=190, width=490)
        self.frame.config(bg='#00747C')
        self.frame.pack(padx=10, pady=10)
        
        Label(self.frame, text="Curso a Eliminar - Facultad de Ingeniería", font=('Segoe UI',15), fg='#00747C', bg='#202022', width=60).place(x=250, y=20, anchor="center")
        
        Button(self.frame, text="Regresar", command=self.btnsalir , font=('Segoe UI',10), fg='#000000', bg='#878787', width=15).place(x=420, y=160, anchor="center")
        self.frame.mainloop()
    
    def btnsalir(self):
        self.ventana.destroy()
        Cursos()


#CrearCurso()
MenuPrincipal()
print(dicCursos)

    
