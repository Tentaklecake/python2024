# Task2: Преобразовании числа в строку
# Перевести число в строку минимум 3 способами

bd_id = 555

bd_id_str1 = str(bd_id)
bd_id_str2 = f"{bd_id}"
bd_id_str3 = format(bd_id)

# Task3: Работа с байтовой последовательностью
# Task3.1: Преобразование в utf-8
# С оборудования получили следующий вывод, нужно преобразовать его в unicode (utf-8) строку.

output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"
output = output.decode()

# Task3.2: Возврат каретки (CR)
# У полученной в Task3.1 строки избавится от символа возврата каретки.
output = output.replace("\r", "")

# Task3.3: Пробельные символы
# У полученной в Task3.2 строки удалить пробельные символы только с начала строки.
output = output.lstrip()
