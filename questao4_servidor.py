import rpyc

class MyService(rpyc.Service):
    def exposed_sum_vector(self, vector):
        return sum(vector)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()


