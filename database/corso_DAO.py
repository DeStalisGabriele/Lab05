# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import *
from model.corso import Corso
from model.studente import Studente


class corso_DAO:

    @staticmethod
    def getCorsi():  # interagisco con il database per estrapoalre il codice insegnamenti
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute("SELECT nome, codins FROM corso")  # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        corsi = []
        for row in cursor:
            corsi.append(Corso(
                nome=row["nome"],
                codice=row["codins"]

            ))  # nome della colonna nel database

        cursor.close()
        cnx.close()
        return corsi


    @staticmethod
    def cercaIscritti( codins):
        '''carca gli iscritti appartenenti a un corso dato in input. Dal DB si nota che per risalire al nome degli studenti
                bisogna andare a prendere la matricola in 'iscrizione' dove è presente il codice del corso'''
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute("SELECT studente.matricola, studente.nome, studente.cognome "
                       "FROM iscrizione "
                       "JOIN studente ON iscrizione.matricola = studente.matricola "
                       "WHERE iscrizione.codins = %s", (codins,)) # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        studenti = []
        for row in cursor:
            studenti.append(Studente(
                nome = row["nome"],
                cognome = row["cognome"],
                matricola = row["matricola"],
            ))

        cursor.close()
        cnx.close()
        return studenti

    @staticmethod
    def cercaStudente( matricola):

        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute("SELECT studente.nome, studente.cognome, studente.matricola "
                       "FROM studente "
                       "WHERE matricola = %s",
                       (matricola,))  # scrivo l'azione (provare prima a faro direttamente su dbeaver)
        studente = None
        row = cursor.fetchone()
        studente = Studente(
            nome = row["nome"],
            cognome = row["cognome"],
            matricola = row["matricola"],
        )

        cursor.close()
        cnx.close()
        return studente

    @staticmethod
    def cercaCorsi(matricola):
        cnx = DBConnect.get_connection()  # creo la connesione
        cursor = cnx.cursor(dictionary=True)  # creo il cursore
        cursor.execute("SELECT corso.nome, corso.codins "
                       "FROM iscrizione "
                       "JOIN corso ON iscrizione.codins = corso.codins "
                       "WHERE matricola = %s",
                       (matricola,))  # scrivo l'azione (provare prima a faro direttamente su dbeaver)

        corsi=[]
        for row in cursor:
            corsi.append(Corso(
                nome=row["nome"],
                codice=row["codins"]
            ))

        cursor.close()
        cnx.close()
        return corsi


