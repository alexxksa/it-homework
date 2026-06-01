import json
import os

FILENAME = "planner.json"


def load_data():
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Помилка читання файлу конфігурації. Створено новий планувальник.")
        return {}


def save_data(data):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")


def add_event(data):
    print("\n--- Додавання нової події ---")
    title = input("Назва події: ").strip()
    date = input("Дата (YYYY-MM-DD): ").strip()
    time = input("Час (HH:MM): ").strip()
    description = input("Опис: ").strip()

    if data:
        new_id = str(max(int(k) for k in data.keys()) + 1)
    else:
        new_id = "1"

    data[new_id] = {
        "title": title,
        "date": date,
        "time": time,
        "description": description,
    }

    save_data(data)
    print("Подію успешно додано!")


def view_events(data):
    print("\n--- Список всіх подій ---")
    if not data:
        print("Подій немає")
        return

    for event_id, info in data.items():
        print(f"ID: {event_id}")
        print(f"Назва: {info['title']}")
        print(f"Дата: {info['date']}")
        print(f"Час: {info['time']}")
        print(f"Опис: {info['description']}")
        print("-" * 20)


def delete_event(data):
    print("\n--- Видалення події ---")
    event_id = input("Введіть ID події для видалення: ").strip()

    try:
        if event_id in data:
            del data[event_id]
            save_data(data)
            print("Подію успішно видалено!")
        else:
            print("Подію не знайдено")
    except Exception:
        print("Сталася помилка при спробі видалення.")


def search_by_date(data):
    print("\n--- Пошук подій за датою ---")
    search_date = input("Введіть дату для пошуку (YYYY-MM-DD): ").strip()

    found = False
    for info in data.values():
        if info["date"] == search_date:
            print(f"{info['time']} — {info['title']} ({info['description']})")
            found = True

    if not found:
        print("Подій на цю дату немає")


def main():
    events = load_data()

    while True:
        print("\n--- Персональний планувальник ---")
        print("1. Додати подію")
        print("2. Переглянути всі події")
        print("3. Видалити подію")
        print("4. Знайти події за датою")
        print("5. Вийти")

        choice = input("Оберіть пункт меню (1-5): ").strip()

        if choice == "1":
            add_event(events)
        elif choice == "2":
            view_events(events)
        elif choice == "3":
            delete_event(events)
        elif choice == "4":
            search_by_date(events)
        elif choice == "5":
            print("Дякуємо за використання планувальника. Бувай!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз (введіть число від 1 до 5).")


if __name__ == "__main__":
    main()
