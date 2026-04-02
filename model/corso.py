class Corso:

    nome: str
    codice: str

    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice

    def __str__(self):
        return f'{self.nome} ({self.codice})'