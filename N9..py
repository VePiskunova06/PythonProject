#9.
answer = input("Собака короткошерстной породы? ").lower()

if answer == "да":
    answer = input("Рост собаки менее 50 см? ").lower()

    if answer == "да":
        answer = input("У собаки короткий хвост? ").lower()

        if answer == "да":
            print("английский бульдог")
        else:
            answer = input("У собаки длинные уши? ").lower()

            if answer == "да":
                print("гончая")
            else:
                answer = input("У собаки короткое тело? ").lower()

                if answer == "да":
                    print("мопс")
                else:
                    print("чихуахуа")

    else:
        answer = input("Собака весит более 50 кг? ").lower()

        if answer == "да":
            print("датский дог")
        else:
            print("фоксхаунд")

else:
    answer = input("Рост собаки менее 50 см? ").lower()

    if answer == "да":
        answer = input("У собаки доброжелательный характер? ").lower()

        if answer == "да":
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")

    else:
        answer = input("У собаки рост менее 70 см? ").lower()

        if answer == "да":
            answer = input("У собаки длинные уши? ").lower()

            if answer == "да":
                print("большой вандейский грифон")
            else:
                print("колли")

        else:
            answer = input("Окрас рыжий с белыми отметинами? ").lower()

            if answer == "да":
                print("сенбернар")
            else:
                answer = input("Белоснежный окрас? ").lower()

                if answer == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")