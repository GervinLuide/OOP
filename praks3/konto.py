class Konto():
    def __init__(self, nimi, saldo):
        self.nimi = nimi
        self.saldo = saldo

    def deposiit(self, kogus):
        self.saldo += kogus

    def ylekanne(self, amount):
        if amount <= self.saldo:
            self.saldo -= amount
        else:
            self.saldo = 0

    def naita_saldo(self):
        return self.saldo
    def naita_nimi(self):
        return self.nimi
