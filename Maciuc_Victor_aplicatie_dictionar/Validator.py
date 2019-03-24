from Error import ValidError

class Validator:

    def valideaza_traducere(self, trad):
        Limbi = ["RO","EN","FR"]
        errors = ""
        if trad.get_cuvant() == " ":
            errors += 'cuvant vid!\n'
        if trad.get_traducere() == " ":
            errors += 'traducere vida!\n'
        if trad.get_sursa() == trad.get_traducere():
            errors += 'sursa este aceeasi cu destinatia!\n'
        if trad.get_destinatie() not in Limbi or trad.get_sursa() not in Limbi:
            errors += 'limba invalida!\n'
        if len(errors):
            raise ValidError(errors)
