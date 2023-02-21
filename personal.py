from Tkconstants import END

from eulexistdb import db
import Tkinter as tk

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'Almosa09'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/mo06uf3"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL,username='admin',password='Almosa09')
window = tk.Tk()
window.title("ams")



def insertar():

     try:
        lbl_resultat.delete('0.0',END)
        query="""
            update insert
            <treballador>
                <departament>{0}</departament>
                <dni>{1}</dni>
                <nom>{2}</nom>
                <cognom>{3}</cognom>
                <telefon>{4}</telefon>
                <mail>{5}</mail>
                <sou>{6}</sou>
              </treballador>
             into /personal""".format(ent_departament.get(),ent_dni.get(),ent_nom.get(),ent_cognom.get(),ent_telefon.get(),ent_mail.get(),ent_sou.get())
        sou=int(ent_sou.get())+2
        res = db.executeQuery(query)
        lbl_resultat.insert('0.0', query)
     except Exception:
        lbl_resultat.delete('0.0', END)
        lbl_resultat.insert('0.0',"Has posat la consulta malament recorda que el sou ha de ser un numero")


def modificar():
    try:
        lbl_resultat.delete('0.0', END)
        dni = ent_dniOperacions.get()
        query = """
            update replace  //treballador[dni='{7}']
            with <treballador>
                <departament>{0}</departament>
                <dni>{1}</dni>
                <nom>{2}</nom>
                <cognom>{3}</cognom>
                <telefon>{4}</telefon>
                <mail>{5}</mail>
                <sou>{6}</sou>
              </treballador>
             """.format(ent_departament.get(), ent_dni.get(), ent_nom.get(), ent_cognom.get(),
                                      ent_telefon.get(), ent_mail.get(), ent_sou.get(),dni)
        sou = int(ent_sou.get()) + 2
        res = db.executeQuery(query)
        lbl_resultat.insert('0.0', query)
    except Exception:
        lbl_resultat.delete('0.0', END)
        lbl_resultat.insert('0.0', "Has posat la consulta malament recorda que el sou ha de ser un numero")


def eliminar():
    try:
        lbl_resultat.delete('0.0', END)
        dni = ent_dniOperacions.get()
        query = """
            update delete //treballador[dni='{0}']""".format(dni)

        res = db.executeQuery(query)
        lbl_resultat.insert('0.0', query)
    except Exception:
        lbl_resultat.delete('0.0', END)
        lbl_resultat.insert('0.0', "Has posat la consulta malament ")

def modificaSou():
    try:
        lbl_resultat.delete('0.0', END)
        dni = ent_departamentOperacions.get()
        query = """
            update value //treballador[departament='{0}']/sou
            with '{1}'""".format(dni,ent_souOperacions.get())
        sou = int(ent_souOperacions.get()) + 2
        res = db.executeQuery(query)
        lbl_resultat.insert('0.0', query)
    except Exception:
        lbl_resultat.delete('0.0', END)
        lbl_resultat.insert('0.0', "Has posat la consulta malament ")

def pujaSou():
    try:



        lbl_resultat.delete('0.0', END)
        dni = ent_departamentOperacions.get()
        query = """for $treballador in //treballador 
        let $sou:=$treballador/sou 
        where $treballador/departament='{0}'
                 return (update value $sou 
                    with $sou+{1})""".format(dni,ent_souOperacions.get())

        res = db.executeQuery(query)
        lbl_resultat.insert('0.0', query)
    except Exception:
        lbl_resultat.delete('0.0', END)
        lbl_resultat.insert('0.0', "Has posat la consulta malament ")

def buscar1():
    try:
        lbl_resultat.delete('0.0',END)
        dni = ent_dniOperacions.get()
        resut=""
        query = """//treballador[dni='{0}']""".format(dni)
        res = db.executeQuery(query)
        hits = db.getHits(res)


        for i in range(hits):
           resut+=  str(db.retrieve(res, i))+"\n"+"\n"
        lbl_resultat.insert('0.0',resut)
        print (resut)
    except Exception:
        lbl_resultat.insert('0.0',"Has posat la consulta malament ")

def buscarTots():
    try:
        lbl_resultat.delete('0.0', END)
        dni = ent_dniOperacions.get()
        resut=""
        query = """//treballador""".format(dni)
        res = db.executeQuery(query)
        hits = db.getHits(res)

        for i in range(hits):
           resut+=  str(db.retrieve(res, i))+"\n\n"
        lbl_resultat.insert('0.0',resut)
        print (resut)
    except Exception:
        lbl_resultat.insert('0.0',"Has posat la consulta malament")

lbl_resultat =tk.Text(master=window)
lbl_resultat.pack()
ent_departament = tk.Entry(master=window,width="50")
ent_dni = tk.Entry(master=window,width="50")
ent_nom = tk.Entry(master=window,width="50")
ent_cognom = tk.Entry(master=window,width="50")
ent_telefon = tk.Entry(master=window,width="50")
ent_mail = tk.Entry(master=window,width="50")
ent_sou = tk.Entry(master=window,width="50")
ent_dniOperacions = tk.Entry(master=window,width="50")
ent_souOperacions= tk.Entry(master=window,width="50")
ent_departamentOperacions= tk.Entry(master=window,width="50")
btn_insert = tk.Button(master=window,text="insertar",command=insertar )
btn_eliminar = tk.Button(master=window,text="eliminar",command=eliminar)
btn_modificar = tk.Button(master=window,text="modificar",command=modificar)
btn_buscar1 = tk.Button(master=window,text="buscar1",command=buscar1 )
btn_buscarTots=tk.Button(master=window,text="buscarTots",command= buscarTots )
btn_asignar=tk.Button(master=window,text="assignar sou departament",command=modificaSou )
btn_pujar=tk.Button(master=window,text="pujar sou departament",command=pujaSou )
lbl_departament = tk.Label(master=window,text="departament").pack()
ent_departament.pack()
lbl_dni = tk.Label(master=window,text="dni").pack()
ent_dni.pack()
lbl_nom = tk.Label(master=window,text="nom").pack()
ent_nom.pack()
lbl_cognom = tk.Label(master=window,text="cognom").pack()
ent_cognom.pack()
lbl_telefon = tk.Label(master=window,text="telefon").pack()
ent_telefon.pack()
lbl_mail = tk.Label(master=window,text="mail").pack()
ent_mail.pack()
lbl_sou = tk.Label(master=window,text="sou").pack()
ent_sou.pack()

btn_insert.pack()
lbl_dnioper = tk.Label(master=window,text="dni per operacions").pack()
ent_dniOperacions.pack()
btn_buscar1.pack()
btn_modificar.pack()
btn_eliminar.pack()
btn_buscarTots.pack()
lbl_departamentOperacions = tk.Label(master=window,text="departament per operacions").pack()
ent_departamentOperacions.pack()
lbl_souOperacions = tk.Label(master=window,text="sou per operacions").pack()
ent_souOperacions.pack()
btn_asignar.pack()
btn_pujar.pack()
window.mainloop()