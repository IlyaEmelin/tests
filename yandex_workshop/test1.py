# Пропишите нужные импорты.
from datetime import time, datetime

# Допишите код функции.
def get_results(your_time, leader_time):
    # Сохраните формат времени как строку в переменную time_format:
    time_format = '%H:%M:%S'
    # Преобразуйте полученные в аргументах строки в объекты datetime:
    leader_time_object = datetime.strptime(leader_time, time_format)
    your_time_object = datetime.strptime(your_time, time_format)

    # Если два объекта datetime равны, то получатель сообщения – лидер.
    # Составьте и верните строку c сообщением для лидера.
    if leader_time_object == your_time_object:
        return f"Вы пробежали за {leader_time} и победили!"
    else:
        # В противном случае вычислите разницу
        # между временем лидера и временем участника.
        # Результатом будет значение типа timedelta.
        difference = leader_time_object - your_time_object

        # Верните сообщение с указанием времени участника
        # и его отставания от лидера:
        total_sec = difference.seconds
        sec = total_sec % 60
        minute = total_sec // 60 % 60
        hour = total_sec // 60 // 60
        return f'Вы пробежали за {your_time} с отставанием от лидера на {hour}:{minute:02}:{sec:02}.'


# Проверьте работу программы. Здесь вы можете подставить свои значения.
print(get_results('02:02:02', '03:04:05'))
