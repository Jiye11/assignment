class info:
    def __init__ (self,name,c_p,gender):
        self.name=name
        self.c_p=c_p
        self.gender=gender

    def info_list(self):
        return ("이름은 %s, 전화번호는 %s, 성별은 %s입니다."%(self.name,self.c_p,self.gender))

user=info("","","")
listt=[]

while 1:
    user.name=input("이름을 입력하세요 : ")

    if user.name=='그만':
        for x in listt:
            print(x)
        print("\n")
        break
        
    user.c_p=input("전화번호를 입력하세요 : ")

    user.gender=input("성별을 입력하세요(male이나 famale로 작성해주세요) : ")
    if user.gender=='male':
        user.gender="male"
    elif user.gender=='female':
        user.gender="female"
    else:
        user.gender="unknown"

    listt.append(user.info_list())
    for x in listt:
        print(x)
    print("\n")