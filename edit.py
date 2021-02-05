from manipularArquivo import escreverArquivo, escrever_abaixo

class Edit:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.imports = ''
        self.classes = []
        self.nomescampos = []
        self.generate_imports_and_classes()
        self.generate_campos()
    
    def generate_imports_and_classes(self):
        arq_temp = self.arquivo
        cod = "\nclass"
        position = arq_temp.find(cod)
        #Separando importacoes
        self.imports = arq_temp[:position]
        #Apagando importacoes de arq_temp
        arq_temp = arq_temp[position:]
        #encontrando local de quebra de class
        while True:
            position_first = arq_temp.find(cod)
            position = arq_temp.find(cod, position_first+1)
            if position == -1: break
            #Separando classes
            temp = arq_temp[:position]
            self.classes.append(temp)
            arq_temp = arq_temp[position:]

    def generate_campos(self):
        cod1 = " = models"
        for clss in self.classes:
            campos = []
            position = 0
            while True:
                position = clss.find(cod1, position)
                if position == -1: break
                final_position = position-1
                init_position = final_position
                cp = clss[final_position]
                str_vazia = ' '
                while cp != str_vazia:
                    init_position = init_position -1
                    cp = clss[init_position]
                campos.append(clss[init_position+1:final_position+1])
                position = position + 5
            self.nomescampos.append(campos)

    def generate_dict_repr(self):
        arq = "teste.py"
        escrever_abaixo(arq, self.imports)
        i=0
        for lista in self.nomescampos:
            escrever_abaixo(arq, str(self.classes[i]))
            line = "\n\tdef dict_repr(self):\n"
            escrever_abaixo(arq, line)
            line = "\t\treturn {\n"
            escrever_abaixo(arq, line)
            for nome in lista:
                line = f"\t\t\t'{nome}': self.{nome},\n"
                escrever_abaixo(arq, line)
            line = "\t\t}\n\n\n"
            escrever_abaixo(arq, line)
            i = i+1

            
                


        
            

            