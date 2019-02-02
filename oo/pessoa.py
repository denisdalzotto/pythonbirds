class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
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
    print(lucas.__dict__)
    print(denis.__dict__)