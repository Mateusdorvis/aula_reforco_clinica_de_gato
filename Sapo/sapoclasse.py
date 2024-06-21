class Sapo:
    def __init__(self,nomedosapo, idadedosapo, cordosolhos):
        self.nomedosapo = nomedosapo
        self.idadedosapo = idadedosapo
        self.cordosolhos = cordosolhos
    def __repr__(self):
        return f" Sapo=  nome do sapo : {self.nomedosapo} idade do sapo : {self.idadedosapo} cor dos olhos : {self.cordosolhos}"