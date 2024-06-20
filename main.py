from gato import Gato

gato1 = Gato("Michi", 20)
gato2 = Gato("Salsa", 5)

def salva_gato(gato:Gato):
    with open('clinica_de_gato/gatos.txt', 'a') as file:
        file.write(f'Gato: nome:{gato.nome};idade:{gato.idade}\n')
   
def ler_gato():
    with open('clinica_de_gato/gatos.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Gato: '):
            atributos = line.strip().split('Gato: ')[1]
            nome = atributos.split(':')[1].split(';')[0]
            idade = atributos.split(':')[2]
            gato = Gato(nome, idade)
            return gato
        
def salva_lista_gato(list_g:list[Gato]):
    with open('clinica_de_gato/gatos.txt', 'a') as file:
        for gato in list_g:
            salva_gato(gato)
def le_lista_gato():
    list_g = []
    with open('clinica_de_gato/gatos.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Gato: '):
            atributos = line.strip().split('Gato: ')[1]
            nome = atributos.split(':')[1].split(';')[0]
            idade = atributos.split(':')[2]
            gato = Gato(nome, idade)
            list_g.append(gato)
    return list_g
Gato.calabreza_s()#o chamado estático
#Gato.calabreza()
#Gato.calabreza()#ia dar erro pois nao é um objeto é uma classe

#gato1.calabreza()#o chamado pro instancia        
#gato_do_txt = ler_gato()

#print(f"Gato({gato_do_txt.nome , gato_do_txt.idade})")

    

list_gato = [gato1,gato2]
#salva_lista_gato(list_gato)

list_gato_txt = le_lista_gato()
print(list_gato_txt)