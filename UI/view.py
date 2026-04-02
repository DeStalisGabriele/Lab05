import flet as ft
from UI import controller

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None #title
        self.ddCorso = None #row1
        self.btnCercaIscritti = None #row1
        self.txtMatricola = None #row2
        self.txtNome = None #row2
        self.txtCognome = None #row2
        self.btnCercaStudente = None #row3
        self.btnCercaCorsi = None #row3
        self.btnIscrivi = None #row3


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self.ddCorso = ft.Dropdown (label = "corso",
                                    options=[
                                        ft.dropdown.Option(key=corso.codice, text=f'{corso.nome} ({corso.codice})')
                                        for corso in self._controller.getCorsi() #qua chiamo la funzione getCorsie prendo nome e codice di tutti i corsi nel database
                                    ],
                                    width=650)

        self.btnCercaIscritti = ft.ElevatedButton (text="Cerca Iscritti",
                                                   on_click=self._controller.cercaIscritti) #da creare

        row1=ft.Row([self.ddCorso, self.btnCercaIscritti]) #riga 1 da modificare larghezza

        #row2
        self.txtMatricola = ft.TextField(label="Matricola")

        self.txtNome = ft.TextField(label="nome", read_only=True) #solo lettura

        self.txtCognome = ft.TextField(label="cognome", read_only=True) #solo lettura

        row2 = ft.Row([self.txtMatricola, self.txtNome, self.txtCognome])

        #row3
        self.btnCercaStudente = ft.ElevatedButton (text="Cerca Studente",
                                                   on_click=self._controller.cercaStudente)

        self.btnCercaCorsi = ft.ElevatedButton (text="Cerca Corsi",
                                                on_click=self._controller.cercaCorsi)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi])

        #aggiungo le righe alla pagina
        self._page.controls.extend([row1, row2, row3]) #con extend posso aggiungere le righe in un colpo solo

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
