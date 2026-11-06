import sys
from stats import parse_record, average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records = read_valid(lines)
    
    # Подсчёт пропущенных непустых строк:
    # используем parse_record и ловим ValueError — это единственное место принятия решения
    skipped_count = 0
    for line in lines:
        if not line.strip():
            continue  # пустые строки не считаем
        try:
            parse_record(line)
        except ValueError:
            skipped_count += 1

    print(len(valid_records))
    print(skipped_count)
    
    if valid_records:
        warm_city = warmest_city(valid_records)
        avg_by_city = average_by_city(valid_records)
        print(avg_by_city[warm_city])
    else:
        print(0.0)

if __name__ == "__main__":
    main()