class Pessoa:
    olhos = 2 # criado atributo de classe

    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade         #são os objetos
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    denis = Pessoa(nome='Denis')
    lucas = Pessoa(denis, nome='lucas')
    print(Pessoa.cumprimentar(lucas))
    print(id(lucas))
    print(lucas.cumprimentar()) # esse código é igual ao da linha 12.
    print(lucas.nome)
    print(lucas.idade)
    for filhos in lucas.filhos:
        print(filhos.nome)
    lucas.sobrenome = 'Dalzotto'
    del lucas.filhos
    lucas.olhos = 1 # aqui criei um atributo na instância.
    del lucas.olhos # foi deletado o atributo do objeto lucas a instância.
    print(lucas.__dict__) # o dict só mostra os atributos de instâncias
    print(denis.__dict__)
    Pessoa.olhos = 3 # foi criado um atributo de olhos na class todos tem 3.
    print(Pessoa.olhos)
    print(lucas.olhos)
    print(denis.olhos)
    print(id(Pessoa.olhos), id(lucas.olhos), id(denis.olhos))
