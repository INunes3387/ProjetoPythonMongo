import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Internet"]
mycol = mydb["Provedor"]

sair = 1
op = 0
exit = 0

while exit == 0:

    sair = int(input('1 - Ler CSV e enviar dados para banco.\n 2 - Inserir dados manualmente.\n 3 - Apagar dados \n 4 - Gerar TXT \n5 - Sair. \n'))

    if sair == 1:
        arq = open('G:\ProjetoPythonMongo\m.csv', 'rb')

        lines = arq.readlines()

        for line in lines:
            column = str(line).split(';')
            mydict = {"CodMunicipio": column[0], "UF": column[1], "NomeMunicipio": column[2], "NomePrestadora": column[3]}
            x = mycol.insert_one(mydict)


    if sair == 2:
        codmunicipio = int(input('Digite o codigo do municipio: \n'))
        uf = (input('Digite o UF: \n'))
        nomeMunicipio = (input('Digite nome do municipio: \n'))
        nomePrestadora = (input('Digite o nome do provedor: \n'))

        mydict = {"CodMunicipio": codmunicipio, "UF": uf, "NomeMunicipio": nomeMunicipio,
                  "NomePrestadora": nomePrestadora}
        x = mycol.insert_one(mydict)

    if sair == 3:
        mydb = myclient["Internet"]
        mycol = mydb["Provedor"]
        x = mycol.delete_many({})
        print(x.deleted_count, " documents deleted.")

    if sair == 4:
        dados = []
        arq = open('G:\ProjetoPythonMongo\lista.txt', 'w')

        for lines in mycol.find({}, {'_id': 0}):
            dados.append(str(lines) + "\n")
            print(lines)
        arq.writelines(dados)
        arq.close()

    if sair == 5:
        exit = 1

