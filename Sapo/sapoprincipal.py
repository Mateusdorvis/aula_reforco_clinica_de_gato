from sapoclasse import Sapo

def leitura_do_sapo():
    with open("C:\Users\182400253\Documents\Desenvolvimento Python\python\python\pasta\aula_reforco_clinica_de_gato\Sapo\sapo.txt", "a") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.startswith("Sapo="):
                x =linha.strip().split('Pessoa= ')[1].split(":")[1]
                name_do_sapo=linha.strip().split('Pessoa= ')[1].split(":")[0]
                idade_do_sapo = linha.strip().split('Pessoa= ')[2].split(":")[-0]
                cor_do_olho =linha.strip().split('Pessoa= ')[1].split(":")[-4]
                objsapo = Sapo(name_do_sapo,idade_do_sapo,cor_do_olho )
                return objsapo
            

funcao = leitura_do_sapo()