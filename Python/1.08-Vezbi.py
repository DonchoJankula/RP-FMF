def sml():
    a = input("Внесете реченица со смајли: ")

    rezultat = "🙂".join(a.split(":)"))
    rezultat = "🙁".join(rezultat.split(":("))

    print(rezultat)


sml()