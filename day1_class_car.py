class Car:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        result = f"{self.color}차가 {self.speed}km/h로 달립니다." ## f-string 사용법!!
        return result ## return은 꼭 적어야지!

my_car = Car("파란색", 60)

print(my_car.drive())
