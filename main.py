class BankHisobi:
    def __init__(self, ism, boshlangich=0):
        self.egasi = ism
        self.__balans = boshlangich   

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            print(f"+ {miqdor} so'm qo‘shildi")
        else:
            print("Miqdor musbat bo‘lishi kerak")

    def pul_yech(self, miqdor):
        if miqdor > 0 and miqdor <= self.__balans:
            self.__balans -= miqdor
            print(f"- {miqdor} so'm yechildi")
        else:
            print("Balans yetarli emas yoki miqdor noto‘g‘ri")

    def balansni_kor(self):
        print(f"{self.egasi}ning balansida: {self.__balans} so'm")


hisob = BankHisobi("Ali", 200000)

hisob.pul_qosh(150000) 
hisob.pul_yech(100000)   
hisob.balansni_kor()  

hisob.pul_yech(300000) 
hisob.balansni_kor()    
