def find_common_participants(uch1, uch2, raz=','):
    """
    Функция для поиска общих участников в двух группах.
        uch1: строка с участниками первой группы
        uch2: строка с участниками второй группы
        raz: разделитель (по умолчанию ',')
    """
    # Разбиваем строки на списки участников
    uch_1 = uch1.split(raz)
    uch_2 = uch2.split(raz)

    #множество для хранения общих участников
    common_set = set()

    # Ищем общих участников
    for uch in uch_1:
        if uch in uch_2:
            common_set.add(uch)

    # Преобразуем множество в список и сортируем
    common_list = sorted(common_set)

    return common_list


# Исходные данные
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем "|"
common = find_common_participants(participants_first_group, participants_second_group, '|')
print(f"Общие участники: {common}")
