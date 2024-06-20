class Gato:
    def __init__(self,_nome,_idade):
        self.nome = _nome
        self.idade = _idade
    @staticmethod
    def calabreza_s():
        print("estatico calabreza")

    def calabreza(self):
        print("instancia calabreza")
