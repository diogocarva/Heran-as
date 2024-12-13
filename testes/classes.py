class Felinos:
    def __init__(self, altura, comprimento, cor, alimento):
        self.altura = altura
        self.comprimento = comprimento
        self.cor = cor
        self.alimento = alimento

class Gatos(Felinos):
    def __init__(self, altura, comprimento, cor, alimento, raca, habitat):
   # Aproveitar o construtor da superclasse Felinos
        super().__init__(altura, comprimento, cor, alimento)
        self.raca = raca  # Atributo especifico para Gatos
        self.habitat = habitat #Atributos sobre o habitats dos Gatos 

class Tigres(Felinos):
     def __init__(self, altura, comprimento, cor, alimento, habitat, raca):
 # Aproveitar o construtor da superclasse Felinos
        super().__init__(altura, comprimento, cor, alimento)
        self.habitat = habitat  # Atributo específico para Tigre
        self.raca = raca #Atributos sobre as racas dos Tigres