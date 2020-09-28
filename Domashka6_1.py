# Домашка №1. 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time


class TrafficLight:  # Вообщем я сделал "правильный" светофор,
    # так как после красного или зеленого всегда должен следовать желтый
    __color = ["\033[31m {}".format("Red"), "\033[33m {}".format("Yellow"),
               "\033[32m {}".format("Green"), "\033[33m {}".format("Yellow")]

    def running(self):
        i = 0
        while True:  # Бесконечный светофор
            print(self.__color[i] + " - " + str(o[i]) + " Second")
            time.sleep(o[i])  # Заморозка времени
            if i != 4:  # Такой замудренный бесконечный цикл =)
                i += 1
            if i == 4:
                i = 0


c = input("Сколько секунд будет гореть зеленый сигнал светофора ? ")
while not c.isnumeric():  # Здесь я хочу чтобы пользователь вводил только цифру.
    c = input("Нужна цифра ! Сколько секунд будет гореть зеленый сигнал светофора ? ")
o = [7, 2, int(c), 2]
sv = TrafficLight()
sv.running()