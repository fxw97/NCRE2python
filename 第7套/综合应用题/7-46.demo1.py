fo = open("PY301-1.txt","w")
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
        fo.write(self.info + "，" + addr + str(self.speed) + "km/h.")
horse = Horse("阿拉伯", "公", 12)
horse.get_descriptive()
horse.write_speed(50)
fo.close()