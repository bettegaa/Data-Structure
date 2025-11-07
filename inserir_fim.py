class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
    
class Linked_list:
    def __init__(self):
        self.primeiro = None
    
    def inserir_fim(self,valor):
        atual= self.primeiro
        if self.primeiro is None:
            novo_no = No(valor)
            self.primeiro = novo_no
            return
        elif self.primeiro.proximo is None:
            novo_no = No(valor)
            self.primeiro.proximo = novo_no
            atual = self.primeiro.proximo
            atual.anterior = self.primeiro
            return
        while atual != None:
            if atual.proximo == None:
                novo_no = No(valor)
                atual.proximo = novo_no
                novo_no.anterior = atual
                break
            atual = atual.proximo
            
        
