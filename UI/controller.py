import flet as ft
from database.corso_DAO import *

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def getCorsi(self):
        return corso_DAO.getCorsi()

    def cercaIscritti(self, e):


        codins = self._view.ddCorso.value  # prende il valore selezionato nel dropdown
        if codins is None:
            self._view.create_alert("Seleziona un corso!")
        studenti = corso_DAO.cercaIscritti(codins)
        # poi mostri gli studenti nella ListView
        for studente in studenti:
            self._view.txt_result.controls.append(ft.Text(str(studente)))
        self._view.update_page()

    def cercaStudente (self, e):
        matricola = self._view.txtMatricola.value
        if matricola is None  : self._view.create_alert("Seleziona un matricola!")
        studente = corso_DAO.cercaStudente(matricola)
        if studente is None : self._view.create_alert("Utente non trovato!")
        self._view.txtNome.value = studente.nome
        self._view.txtCognome.value = studente.cognome
        self._view.update_page()

    def cercaCorsi(self, e):
        matricola = self._view.txtMatricola.value
        if matricola is None :  self._view.create_alert("Seleziona un matricola!")
        corsi = corso_DAO.cercaCorsi(matricola)
        if corsi is None : self._view.create_alert("Utente non trovato!")
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(str(corso)))
        self._view.update_page()

    def iscrivi (self, e):
        corso = self._view.ddCorso.value
        matricola = self._view.txtMatricola.value
        if matricola is None : self._view.create_alert("inserisci una matricola!")
        if corso is None : self._view.create_alert("inserisci un corso!")
        corso_DAO.iscrivi(matricola, corso)
        self._view.create_alert("Studente iscritto con successo!")



