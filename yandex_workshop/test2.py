def get_selection(collection):
    delta_index = len(collection) // 10
    mod_delta_index = round(len(collection) % 10 * 2 / 10)
    return collection[delta_index : -delta_index - mod_delta_index]

# def get_selection(collection):
#     max_value, min_value = max(collection), min(collection)
#     delta_10_percent = (max_value - min_value) / 10
#     left, right = int(min_value + delta_10_percent), int(max_value - delta_10_percent)
#     return list(filter(
#         lambda value: left < value < right,
#         collection
#     ))


heights = [140.1, 150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1, 180]
# heights = [163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189]
selection = get_selection(heights)
print('Выборка:', selection)

# Ожидаемый вывод на печать:
# Выборка: [150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1]


# Выборка: [150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1]
# Вызов функции get_selection с аргументом:
# [163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189]
# вернул:
# [165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187]
# Ожидаемый результат:
# [165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185]