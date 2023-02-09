from eulexistdb import db
import Tkinter as tk





EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'Almosa09'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/mo06uf3"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL,username='admin',password='Almosa09')



def ferConsulta():
    try:
        nom = ent_nom.get()
        resut=""
        query = nom
        res = db.executeQuery(query)
        hits = db.getHits(res)

        for i in range(hits):

           resut+=  str(db.retrieve(res, i))+"\n"
        lbl_nom.config(text=resut)
        print (resut)
    except Exception:
        lbl_nom.config(text="Has posat la consulta malament")

window = tk.Tk()
window.title("ams")

lbl_nom = tk.Label(master=window,
    text="",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width="100",
    justify=tk.LEFT
)

ent_nom = tk.Entry(master=window,fg="red", bg="blue", width="50")



btn_entrarNom = tk.Button(master=window,text="Consultar", command=ferConsulta)


lbl_nom.pack()
ent_nom.pack()
btn_entrarNom.pack()

window.mainloop()