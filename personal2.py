from Tkconstants import END, CENTER

from eulexistdb import db
import Tkinter as tk
import ttk

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

def buscar1(a):
    curItem = tree.focus()
    print(tree.item(curItem))
    text = tree.item(curItem)["values"]
    ent_departament.insert(0,text[6])
    ent_departamentOperacions.insert(0, text[6])
    ent_sou.insert(0, text[5])
    ent_souOperacions.insert(0, text[5])
    ent_mail.insert(0, text[4])
    ent_telefon.insert(0, text[3])
    ent_cognom.insert(0, text[2])
    ent_nom.insert(0, text[1])



def buscarTots():

        for item in tree.get_children():
            tree.delete(item)

        resut=""
        query = """//treballador/dni/text()"""
        res = db.executeQuery(query)
        hits = db.getHits(res)
        query = """//treballador/nom/text()"""
        res2 = db.executeQuery(query)
        query = """//treballador/cognom/text()"""
        res3 = db.executeQuery(query)
        query = """//treballador/telefon/text()"""
        res4 = db.executeQuery(query)
        query = """//treballador/mail/text()"""
        res5 = db.executeQuery(query)
        query = """//treballador/sou/text()"""
        res6= db.executeQuery(query)
        query = """//treballador/departament/text()"""
        res7 = db.executeQuery(query)


        for i in range(hits):

            tree.insert('', 'end', text="1", values=(str(db.retrieve(res, i)), str(db.retrieve(res2, i)), str(db.retrieve(res3, i)),str(db.retrieve(res4, i)),str(db.retrieve(res5, i)),str(db.retrieve(res6, i)),str(db.retrieve(res7, i))))




# Add a Treeview widget
tree = ttk.Treeview(window, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings', height=5)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="dni")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="nom")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="cognom")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="telefon")
tree.column("# 5", anchor=CENTER)
tree.heading("# 5", text="mail")
tree.column("# 6", anchor=CENTER)
tree.heading("# 6", text="sou")
tree.column("# 7", anchor=CENTER)
tree.heading("# 7", text="departament")
tree.bind('<ButtonRelease-1>', buscar1)
tree.pack()
lbl_resultat =tk.Text(master=window)

ent_departament = ttk.Entry(master=window,width="50")
ent_dni = ttk.Entry(master=window,width="50")
ent_nom = ttk.Entry(master=window,width="50")
ent_cognom = ttk.Entry(master=window,width="50")
ent_telefon = ttk.Entry(master=window,width="50")
ent_mail = ttk.Entry(master=window,width="50")
ent_sou = ttk.Entry(master=window,width="50")

ent_souOperacions= tk.Entry(master=window,width="50")
ent_departamentOperacions= tk.Entry(master=window,width="50")
btn_insert = tk.Button(master=window,text="insertar",command=insertar )
btn_eliminar = tk.Button(master=window,text="eliminar",command=eliminar)
btn_modificar = tk.Button(master=window,text="modificar",command=modificar)
ent_dniOperacions = tk.Entry(master=window,width="50")
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