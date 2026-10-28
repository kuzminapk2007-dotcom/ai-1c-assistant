import json


def normalize_request(text):
    return text.strip().lower()


def detect_report_type(text):
    if "продажи" in text:
        return "продажи"
    return None


def detect_period(text):
    if "октябрь" in text:
        return "октябрь"
    return None


def detect_group_by(text):
    if "товар" in text:
        return "товары"
    elif "менеджер" in text:
        return "менеджеры"
    return None


def parse_request(text):
    normalized_text = normalize_request(text)
    return {
        "report_type": detect_report_type(normalized_text),
        "period": detect_period(normalized_text),
        "group_by": detect_group_by(normalized_text)
    }


if __name__ == "__main__":
    user_request = input("Введите запрос: ")
    normalized_request = normalize_request(user_request)

    if not normalized_request:
        print("Ошибка: запрос пустой")
        exit()
    print(normalized_request)

    report_params = parse_request(user_request)
    print(report_params)

    json_result = json.dumps(report_params, ensure_ascii=False)
    print(json_result)

    with open("report_params.json", "w", encoding="utf-8") as file:
        file.write(json_result)
