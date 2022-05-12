from xmlrpc.server import SimpleXMLRPCServer


class MyFuncs:
    def add(self, x, y):
        return x+y

    def sub(self, x, y):
        return x-y


# create and launch server
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MyFuncs)
server.serve_forever()
