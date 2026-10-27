report_type = None
period = None
group_by = None

user_request = input("Введите запрос: ")
normalized_request = user_request.strip().lower()
if not normalized_request:
    print("Ошибка: запрос пустой")
    exit()
print(normalized_request)


if "продажи" in normalized_request:
    report_type = "продажи"
    print("Тип отчета: продажи")
else:
    print("Неизвестный тип отчета")

if "октябрь" in normalized_request:
    period = "октябрь"
    print("Период: октябрь")
else:
    print("Период не определен")

if "товар" in normalized_request:
    group_by = "товары"
    print("Группировка: товары")
elif "менеджер" in normalized_request:
    group_by = "менеджеры"
    print("Группировка: менеджеры")
else:
    print("Группировка не определена")

report_params = {
    "report_type": report_type,
    "period": period,
    "group_by": group_by
}
print(report_params)