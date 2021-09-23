fo = open("PY301-2.txt","w")
class Horse():
    def __init__(self, category, gender, age):
        self.category = category
        self.gender = gender
        self.age = age
        self.speed = 0
    def get_descriptive(self):
        self.info = "一匹" + self.category + str(self.age) + "岁的" + self.gender + "马"
    def write_speed(self, new_speed):
        self.speed = new_speed
        addr = "在草原上奔跑的速度为"
        fo.write(self.info + "，" + addr + str(self.speed) + "km/h。")

class Camel(Horse):
    def __init__(self, category, gender, age):
        super().__init__(category, gender, age)
    def write_speed(self,new_speed):
        addr = "在沙漠上奔跑的速度为"
        self.speed=new_speed
        fo.write(self.info.replace("马","骆驼") + "，" + addr + str(self.speed) + "km/h。")
camel = Camel("双峰驼","母",20)
camel.get_descriptive()
camel.write_speed(40)
fo.close()
