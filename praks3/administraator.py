from praks2.kasutajad3 import Kasutaja

class Admin(Kasutaja):
    privileegid = "lubatud lisada kasutajad", "lubatud eemaldada kasutajad", "lubatud blokeerida kasutajad"

    def naita_privileegid(self):
        print(self.privileegid)


