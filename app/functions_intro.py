def describe_user(name, role="User", *skills, **details):
    try:
        print(f"Имя: {name}")
        print(f"Роль: {role}")
        print(f"Навыки: {', '.join(skills)}")
        if details:
            print("Дополнительно:")
            for key, value in details.items():
                print(f"  {key}: {value}")

    except Exception as e:
        print(e)


describe_user("Иван", "Админ", "Python", "Django", "JS", age=25, city="Москва")

count = 0


def increment():
    global count
    count += 1


increment()
print(count)
