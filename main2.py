import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Internet2"]
mycol = mydb["Provedor2"]

sair = 1
op = 0

while sair != 3:

    sair = int(input('1 - Ler CSV e enviar dados para banco.\n2 - Filtrar dados.\n3 - Sair.\n'))

    if sair == 1:
        arq = open('E:\ProjetoPythonMongo\m.csv', 'rb')

        lines = arq.readlines()

        for line in lines:
            column = str(line).split(';')
            mydict = {"CodMunicipio": column[0], "UF": column[1], "NomeMunicipio": column[2],
                      "NomePrestadora": column[3]}
            x = mycol.insert_one(mydict)

    if sair == 2:
        op = int(input(
            '1 - Filtrar por CodMunicipio.\n2 - Filtrar por UF.\n3 - Filtrar por NomeMunicipio. \n4 - Filtrar por NomePrestadora. \n'))


        if op == 1:
            for x in mycol.find({}, {'_id': 0, 'CodMunicipio': 1}):
                print(x)
        if op == 2:
            for x in mycol.find({}, {'_id': 0, 'UF': 1}):
                print(x)
        if op == 3:
            for x in mycol.find({}, {'_id': 0, 'NomeMunicipio': 1}):
                print(x)
        if op == 3:
            for x in mycol.find({}, {'_id': 0, 'NomePrestadora': 1}):
                print(x)


    if sair == 3:
        sair = 3