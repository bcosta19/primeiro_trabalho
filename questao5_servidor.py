from time import time
import rpyc

class MyService(rpyc.Service):
    def exposed_sum_vector(self, vector):
        # Instrução principal
        start = time()
        soma = self.soma(vector)
        print(f"Tempo {time() - start}")
        return soma

    def soma(self, vector):
        self.s = 0
        for i in range(len(vector)):
            self.s += vector[i]
        return self.s



if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()


