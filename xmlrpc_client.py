import xmlrpc.client

s = xmlrpc.client.Server("http://localhost:8000")
# pr int l i s t of a v a i l a b l e methods
print(s.system.listMethods())
# use methods
print(s.add(2, 3))
print(s.sub(5, 2))
