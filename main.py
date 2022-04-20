import pymongo #importar biblioteca

myclient = pymongo.MongoClient("mongodb://localhost:27017/") #conexão com mongo
mydb = myclient["Internet"] #nome do database
mycol = mydb["Provedor"] # "pasta" do database


op = 0 #variavel para receber opcoes
exit = 0 #variavel para sair do while

while exit == 0:

    op = int(input('1 - Ler CSV e enviar dados para banco.\n2 - Inserir dados manualmente.\n3 - Apagar dados \n4 - Gerar TXT \n5 - Sair. \n')) #Entrada de dados

    if op == 1:
        arq = open('E:\ProjetoPythonMongo\m.csv', 'rb') #abri o arquivo

        lines = arq.readlines() #variavel para ler linhas

        for line in lines:  #for para percorrer o arquivo
            column = str(line).split(';') #Fazer a divisão do texto quando aparecer ';'
            mydict = {"CodMunicipio": column[0], "UF": column[1], "NomeMunicipio": column[2], "NomePrestadora": column[3]} #definindo e separando dados
            x = mycol.insert_one(mydict) #adicionando dados


    if op == 2:
        codmunicipio = int(input('Digite o codigo do municipio: \n'))  #Entrada de dados
        uf = (input('Digite o UF: \n')) #Entrada de dados
        nomeMunicipio = (input('Digite nome do municipio: \n')) #Entrada de dados
        nomePrestadora = (input('Digite o nome do provedor: \n')) #Entrada de dados

        mydict = {"CodMunicipio": codmunicipio, "UF": uf, "NomeMunicipio": nomeMunicipio,
                  "NomePrestadora": nomePrestadora} #definindo e separando dados
        x = mycol.insert_one(mydict) #adicionando dados

    if op == 3:
        mydb = myclient["Internet"]  #sinalizando database
        mycol = mydb["Provedor"]
        x = mycol.delete_many({}) #excluir tudo
        print(x.deleted_count, " documents deleted.") #mensagem gerada após deletar dados

    if op == 4:
        dados = [] #vetor para salvar dados do mongo para criar um TXT
        arq = open('E:\ProjetoPythonMongo\lista.txt', 'w') #criando TXT

        for lines in mycol.find({}, {'_id': 0}): #adicionando dados do mongo no vetor e criando/adicionando no TXT
            dados.append(str(lines) + "\n")
            print(lines)
        arq.writelines(dados)
        arq.close()

    if op == 5:
        exit = 1 #fecha o programa

