'''Функция для нахождения индекса первого вхождения элемента в списке, в случае
ненахождения элемента выдает None'''
def index_item(item):
    try:
        return items_list.index(item)
    except ValueError:
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  #Список продуктов

for find_item in ['банан', 'груша', 'персик']:
    index = index_item(find_item)  #Даем перемеенной index значение индекса элемента или None
    if index is not None: #Вывод ответа
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
