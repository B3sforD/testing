valid_responce = {
    "да",
    "lf",
    "yes",
    "угу",
    "eue",
    "верно",
    "согласен",
    "конечно",
    "абсолютно",
    "естественно",
    "подтверждаю",
    "точно",
    "ок",
    "jr",
    "ага",
    "fuf",
    "уверен",
    "безусловно",
    "правильно"
}
otkas = {
    "нет",
    "ytn",
    "no",
    "неправильно",
    "не согласен",
    "не хочу",
    "не уверен",
    "ни в коем случае",
    "неа",
    "ytf",
    "не готов",
    "не верю",
    "не понимаю",
    "не могу",
    "ни в коем случае"
}

dreams = {
    "похудеть",
    "похудение",
    "сбросить вес",
    "устранить лишний вес",
    "снизить массу тела",
    "избавиться от жировых отложений",
    "пролечить ожирение",
    "уменьшить объемы тела",
    "достичь желаемой фигуры",
    "подтянуть фигуру",
    "сделать тело стройнее"
}

Life = input("Начало Квеста для похудения, Вы готовы?: ").lower()
if Life in valid_responce:
    print("Начнем наш квест по развитию!")
    a = input('Определите свою главную цель: ').lower()
elif Life in otkas:
    print("Извини ты слишком слаб для квеста.")

else:
    print("Извините, в ответ принимается только 'Да', 'Окей', 'Готов' или 'Ready'.")

if a in dreams:
    print("Первое что вам надо сделать это не только цель но и желание этого достичь")
print('начнем с банальщины ты пьешь 4 литра колы в день,Ограничь это колличество ровно на литр')

eda = (
    "мясо", "фрукты",
    "овощи", "крупы",
    "рыба", "гарнир",
    ""
)
print(eda)

print("ты можешь выбрать 1 просто нажав enter ниче не написав")

first = input("выбери первое что добавить в рацион: ").lower()
second = input("выбери второе что добавить в рацион: ").lower()

if first in eda and second in eda and first == "мясо" and second == "овощи":
    print('https://www.gastronom.ru/search?search=%D0%BC%D1%8F%D1%81%D0%BE+%D0%B8+%D0%BE%D0%B2%D0%BE%D1%89%D0%B8&pageType=recipepage')
elif first in eda and second in eda and first == "мясо" and second == "крупы" or second == "мясо" and first == "крупы":
    print("https://www.gastronom.ru/search?search=%D0%BC%D1%8F%D1%81%D0%BE+%D1%81+%D0%BA%D1%80%D1%83%D0%BF%D0%BE%D0%B9&pageType=recipepage")
elif first in eda and second in eda and first == "крупы" and second == "крупы" or second == "крупы" and first == "крупы":
    print("https://www.gastronom.ru/search?search=%D0%BA%D1%80%D1%83%D0%BF%D1%8B+%D1%81+%D1%84%D1%80%D1%83%D0%BA%D1%82%D0%B0%D0%BC%D0%B8&pageType=recipepage")
elif first in eda and second in eda and first == "рыба" and second == "овощи" or second == "рыба" and first == "овощи":
    print("https://www.gastronom.ru/search?search=%D1%80%D1%8B%D0%B1%D0%B0+%D1%81+%D0%BE%D0%B2%D0%BE%D1%89%D0%B0%D0%BC%D0%B8&pageType=recipepage")
elif first in eda and second in eda and first == "рыба" and second == "крупы" or second == "рыба" and first == "крупы":
    print("https://www.gastronom.ru/search?search=%D1%80%D1%8B%D0%B1%D0%B0+%D1%81+%D0%BA%D1%80%D1%83%D0%BF%D0%B0%D0%BC%D0%B8&pageType=recipepage")
elif first in eda and second in eda and first == "рыба" and second == "гарнир" or second == "рыба" and first == "гарнир":
    print("https://www.gastronom.ru/search?search=%D1%80%D1%8B%D0%B1%D0%B0+%D1%81+%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC&pageType=recipepage")
elif first in eda and second in eda and first == "мясо" and second == "гарнир" or second == "мясо" and first == "гарнир":
    print("https://www.gastronom.ru/search?search=%D0%BC%D1%8F%D1%81%D0%BE+%D1%81+%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC&pageType=recipepage")
elif first in eda and second in eda and first == "овощи" and second == "крупы" or second == "овощи" and first == "крупы":
    print("https://www.gastronom.ru/search?search=%D0%BE%D0%B2%D0%BE%D1%89%D0%B8+%D1%81+%D0%BA%D1%80%D1%83%D0%BF%D0%B0%D0%BC%D0%B8&pageType=recipepage")
elif first in eda and second in eda and first == "мясо" and second == "" or second == "мясо" and first == "":
    print("https://www.gastronom.ru/search?search=%D0%BC%D1%8F%D1%81%D0%BE&pageType=recipepage")
elif first in eda and second in eda and first == "фрукты" and second == "" or second == "фрукты" and first == "":
    print("https://www.gastronom.ru/search?search=%D1%84%D1%80%D1%83%D0%BA%D1%82%D1%8B&pageType=recipepage")
elif first in eda and second in eda and first == "овощи" and second == "" or second == "овощи" and first == "":
    print("https://www.gastronom.ru/search?search=%D0%BE%D0%B2%D0%BE%D1%89%D0%B8&pageType=recipepage")
elif first in eda and second in eda and first == "крупы" and second == "" or second == "крупы" and first == "":
    print("https://www.gastronom.ru/search?search=%D0%BA%D1%80%D1%83%D0%BF%D1%8B&pageType=recipepage")
elif first in eda and second in eda and first == "рыба" and second == "" or second == "рыба" and first == "":
    print("https://www.gastronom.ru/search?search=%D1%80%D1%8B%D0%B1%D0%B0&pageType=recipepage")
elif first in eda and second in eda and first == "гарнир" and second == "" or second == "гарнир" and first == "":
    print("https://www.gastronom.ru/search?search=%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80&pageType=recipepage")

print("записывай все что сьел и скок каллорий")
print("отлично с едой ты разобрался малясь")
print("давай приступим к твоим тренировкам")
print("по началу тренироваться надо с малого")
print("встань и пройди 5 киллометров без музыки")
print("это не скучно если всматриваться в людей в животных можешь по лесу погулять")
street = input("но ты должен пройти минимум 5 км так что давай удачи: ")

if street in otkas:
    print("Ты чо, вставай и иди... ")
elif street in valid_responce:
    print("красава ты реально верен своим словам")

input("напиши как прогуляешься: ")

print("харош на сегодня хватит!")


