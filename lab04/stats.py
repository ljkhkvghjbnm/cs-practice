from typing import List, Dict

def parse_record(line: str) -> Dict[str, any]:
    """
    Разбирает одну строку вида «город;температура;дата».
    Возвращает словарь: {"city": ..., "temp": ..., "date": ...}.
    Если строка некорректна — выбрасывает ValueError с понятным сообщением.
    """
    parts = line.split(";")
    
    # Проверка: ровно три поля
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидается 3, найдено {len(parts)}")
    
    city, temp_str, date = parts
    
    # Город и дата не должны быть пустыми
    if not city.strip():
        raise ValueError("Город не может быть пустым")
    if not date.strip():
        raise ValueError("Дата не может быть пустой")
    
    # Температура должна быть числом
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}'")
    
    return {
        "city": city.strip(),
        "temperature": temp,
        "date": date.strip()
    }


def read_valid(lines: List[str]) -> List[Dict[str, any]]:
    """
    Читает список строк, разбирает их через parse_record.
    Пустые строки пропускаются молча.
    Строки, которые не удалось распарсить, пропускаются (ошибки перехватываются),
    но функция не выбрасывает исключения наружу.
    Возвращает список только валидных записей.
    """
    valid_records = []
    
    for line in lines:
        # Пустые строки — пропускаем молча
        if not line.strip():
            continue
        
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Негодные строки просто пропускаем, не прерывая работу
            continue
    
    return valid_records


def average_by_city(records: List[Dict[str, any]]) -> Dict[str, float]:
    """
    Считает среднюю температуру по каждому городу.
    Результат округляется до одного знака после запятой.
    """
    total = {}
    count = {}
    
    for r in records:
        city = r["city"]
        temp = r["temperature"]
        
        total[city] = total.get(city, 0.0) + temp
        count[city] = count.get(city, 0) + 1
    
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    
    return averages


def warmest_city(records: List[Dict[str, any]]) -> str:
    """
    Находит город с наибольшей средней температурой.
    При равенстве средних — возвращает первый по алфавиту.
    Предполагается, что records непустой (если пустой — поведение не определено условием).
    """
    averages = average_by_city(records)
    
    # Находим максимальную среднюю температуру
    max_avg = max(averages.values())
    
    # Города с максимальной средней
    candidates = [city for city, avg in averages.items() if avg == max_avg]
    
    # При равенстве — первый по алфавиту
    return sorted(candidates)[0]