import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código executado quando conexão é iniciada, caso seja necessário
        # sobrescreve o método da classe pai Service
        pass

    def on_disconnect(self, conn):
        # código executado quando conexão é encerrada, caso seja necessário
        # sobrescreve o método da classe pai Service
        pass

    def exposed_get_answer(self): # método exposto
        return 42

    exposed_the_real_answer_though = 43 #este é um atributo exposto

    def get_question(self): # Este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"

# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861) # Oferece o serviço na porta 18861 para ser acessado por outros clientes
    t.start()
