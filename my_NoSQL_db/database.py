import os
import json
from typing import List, Dict, Optional

class Database:
    #Инициализация папки data и создание внутри нашей NoSQL базы данных 
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.data_path = f"./data/{db_name}"
        os.makedirs(self.data_path, exist_ok=True)


    #Создание таблицы, таблица представляет собой json файл
    """
        table_name указывает на имя таблицы, которую мы хотим создать, 
        columns - это список строк, 
        каждая из которых представляет собой название столбца таблицы.
    """
    def create_table(self, table_name: str, columns:List[str]):
        table_path = f"{self.data_path}/{table_name}.json"
        if not os.path.exists(table_path):
            with open(table_path, "w") as f:
                json.dump([], f)
            
            # #Чтение заголовка таблицы
            # """Заголовок таблицы это dict в котором ключи это названия столбцов а значения None"""    
            # with open(table_path, "r") as f:
            #     data = json.load(f)
            
            # #? Все что ниже нужно для того случая когда создается таблица которая уже существует, и чтобы поверх обновлять новые данные если это нужно  
            # #Создание заголовка таблицы, если он отсутствует
            # if not data:
            #     header = {}
            #     for column in columns:
            #         header[column] = None
            #     data.append(header)
            
            # with open(table_path, "w") as f:
            #     json.dump(data, f, indent = 4)

    
    #Добавление данных в таблицу
    def insert(self, table_name: str, row:Dict):
        table_path = f"{self.data_path}/{table_name}.json"
        
        with open(table_path, "r") as f:
            data = json.load(f)
        
        data.append(row)
        
        with open(table_path, "w") as f:
            json.dump(data, f, indent=4)
            
            
    def select(self, table_name: str, condition=None, order_by=None):
        table_path = f"{self.data_path}/{table_name}.json"
        with open(table_path, "r") as f:
            data = json.load(f)
        
        #Условие для фильтра если он обьявлен 
        if condition:
            filtered_data = []
            for row in data:
                if condition(row):
                    filtered_data.append(row)
            data = filtered_data
        
        #Если передан order_by, то данные сортируются по указанному столбцу
        """
            Параметр order_by должен быть словарем с ключом "column" и,
            необязательным, ключом "reverse". Если "reverse" равен True, 
            то сортировка будет в обратном порядке.
        """
        if order_by:
            column = order_by["column"]
            reverse = order_by.get("reverse", False)
            data = sorted(data, key=lambda row: row[column], reverse=reverse)
            
        return data
    
    
    #Обновление данных 
    """
        В параметр 'condition' должен передаваться словарь,
        благодаря которому можно найти нужный row в таблице.
        В параметр 'new_values' передается словарь с новыми значениями
    """
    def update(self, table_name: str, condition: Dict, new_values: Dict):
        table_path = f"{self.data_path}/{table_name}.json"
        with open(table_path, "r") as f:
            data = json.load(f)
        
        # Проходим по каждой записи в таблице    
        for row in data:
            # Проверяем, удовлетворяет ли запись условию condition
            for key, value in condition.items():
                if row[key] != value:
                    break
                else:
                    row.update(new_values)
                    
        # Записываем обновленные данные обратно в файл
        with open(table_path, "w") as f:
            json.dump(data, f, indent=4)
    
    
    #Удаление данных в таблице
    def delete(self, table_name: str, condition: Dict):
        table_path = f"{self.data_path}/{table_name}.json"
        with open(table_path, "r") as f:
            data = json.load(f)
    
        new_data = []
        for row in data:
            match = True
            for k, v in condition.items():
                if row[k] != v:
                    match = False
                    break
            if not match:
                new_data.append(row)
        data = new_data
        
        with open(table_path, "w") as f:
            json.dump(data, f, indent=4)


    #Удаление таблицы
    def drop_table(self, table_name: str):
        table_path = f"{self.data_path}/{table_name}.json"
        os.remove(table_path)
        
    
    def get_table_names(self) -> List[str]:
        # Получаем список всех файлов в директории базы данных
        files = os.listdir(self.data_path)
        # Из списка файлов выбираем только те, которые заканчиваются на ".json"
        json_files = [file for file in files if file.endswith(".json")]
        # Каждое имя файла в списке json_files будет иметь расширение ".json"
        # Поэтому отбрасываем расширение, используя метод splitext модуля os
        table_names = [os.path.splitext(file)[0] for file in json_files]
        return table_names
    

