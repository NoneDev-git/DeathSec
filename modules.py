class InfectedDevice:
    def __init__(self, method:str, name:str, ip:str, country:str, position:set, status:str, last_online:str):
        self.method = method
        self.name = name
        self.ip = ip
        self.country = country
        self.status = status
        self.position = position

