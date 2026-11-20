from logstats import parse_event, count_levels, top_errors, format_report

file_name = input('Введите имя файла:')

with open(file_name, 'r', encoding='utf-8') as log:
    counts = count_levels(log)

with open(file_name, 'r', encoding='utf-8') as log:
    errors = top_errors(log, 3)

total = 0

for level in counts:
    total += counts[level]

error_count = counts['ERROR']
broken = counts['BROKEN']

print(total)
print(error_count)
print(broken)

report = format_report(counts, errors)

with open('report.txt', 'w', encoding='utf-8') as file:
    file.write(report)