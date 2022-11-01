class Product:
    def __init__(self,_name,_upc,_code1,_code2):
        self.name = _name
        self.upc = _upc
        self.code1 = _code1
        self.code2 = _code2

    def decode(self):
        print(self.name)
        print(self.upc)
        print(self.code1, ":", int(self.code1,2))
        print(self.code2, ":", int(self.code2,2))

p1 = Product("GV_CWY_VARIETY_24CT", "16122 5972","0010100011110001101111111", "0100100110011101010100100")
p1.decode()