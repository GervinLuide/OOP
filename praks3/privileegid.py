from praks3.administraator import Admin

class Privileegid(Admin):
    def __init__(self, privileegid):
        self.privileegid = []
        self.privileegid.append(privileegid)


admin1 = Privileegid("Lubatud lisada kasutajad")
admin1.naita_privileegid()

