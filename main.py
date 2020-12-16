f_o = open("testfile.txt", "w")
f_o.write("Первая строка\n")
f_o.write("Вторая строка\n")
f_o.write("Третья строка\n")
f_o.write("Четвертая строка\n")
f_o.write("---------------\n")
f_o.close()

l = ["Первая строка ", "Вторая строка ", "Третья строка\n"]
f_o = open("testfile.txt", "a")
f_o.writelines(l)
f_o.write("---------------\n")
f_o.close()

f_o = open("Методичка. Урок 5.pdf", "rb")
pdf_o = f_o.read()    # бинарное чтение

class SomeClassWithContext:
    def __enter__(self):
        print("Метод запускается, когда мы передаем объект в менеджер контекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Этот метод запускается, когда мы заканчиваем работу с объектом в менеджере контекста")
    def some_meth(self):
        pass

some_obj = SomeClassWithContext()
with some_obj:
    print("Какая-то логика")
    some_obj.some_meth()
#    raise ValueError("Ошибка!!!")   # При генерации ошибки выполняется EXIT из контекстного метода
    c = 1           # До это строке не доходит в случае ошибки
с = 1

from logging import getLogger
logger = getLogger(__name__)

with open("Методичка. Урок 5.pdf", "rb") as f_o:
    content = f_o.read()
    logger.info("Читаем PDF")
    f_o.seek(0)
    logger.error("Ошибка!!!")
    print(f_o.tell())
    print(content)

import json

with open("json_test.json", "w") as json_obj:
    some_data = {"user_id": 123456, "position": "developer"}
    json.dump(some_data, json_obj)
