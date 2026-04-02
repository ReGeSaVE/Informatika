import json


def task() -> float:
    # Чтение JSON файла
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Вычисление суммы произведений score * weight
    summm = sum(item['score'] * item['weight'] for item in data)

    # Возврат результата, округленного до 3 знаков после запятой
    return round(summm, 3)


print(task())