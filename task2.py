
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import IPython
from IPython.display import display


def show_diagram(join_df, areSurvived, title):
    vals = join_df[join_df["Survived"] == areSurvived]["Percent Of Surviving"]
    labels = join_df[join_df["Survived"] == areSurvived]["Pclass"]
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)
    ax.pie(vals, labels=labels, autopct='%1.1f%%')
    ax.axis("equal")


def main():
    csv = "titanic.csv"

    # 2.1. Загрузить данные в датафрейм с использованием функции read_csv
    titanik_df = pd.read_csv(csv)

    # 2.2. Вывести датафрейм на экран, ознакомиться с его содержанием.
    print("ДАТАФРЕЙМ:")
    print(titanik_df)
    print("\n")

    # 2.3. Вывести первые 5 строк датафрейма.
    print("ПЕРВЫЕ 5 СТРОК:")
    print(titanik_df.head())
    print("\n")

    # 2.4 Вывести всю информацию о датафрейме с использованием функции
    # Info. Проанализировать полученную информацию.
    print("ИНФО:")
    print(titanik_df.info())
    print("\n")

    # Индивидуальные задачи

    # в столбце Gender заменить значение ‘male’ на ‘man’, ‘female’ на
    # ‘woman’;
    print("ПЕРЕИМЕНОВАНИЕ ГЕНДЕРОВ:")
    titanik_df = titanik_df.replace({"male": "man", "female": "woman"})
    print(titanik_df["Gender"])
    print("\n")

    # вычислить максимальный возраст пассажира и вывести соответствующую строку (строки) датафрейма;
    print("MAX AGE ROW:")
    max_age = titanik_df.loc[titanik_df['Age'].idxmax()]
    print(max_age)
    print("\n")

    # - вычислить среднюю стоимость билета;
    print("СРЕДНЯЯ ЦЕНА БИЛЕТА:")
    average_ticket_price = titanik_df['Fare'].mean()
    print(average_ticket_price)
    print("\n")

    # - вывести информацию о пассажирах, которые ехали с родственниками -
    # супругами, родителями и т.д. (фрагмент датафрейма с соответствующими строками);
    print("ВСЕ, КТО БЫЛИ С РОДСТВЕННИКАМИ:")
    relatives_df = titanik_df[(titanik_df["SibSp"] > 0) | (titanik_df["Parch"] > 0)]
    print(relatives_df[["SibSp", "Parch"]])
    print("\n")

    # - вывести всех мужчин до 50 лет. Вычислить их количество
    print("МУЖЧИНЫ ДО 50:")
    men_under_fifty = titanik_df[(titanik_df["Age"] < 50) & (titanik_df["Gender"] == "man")]
    print(men_under_fifty)
    print("КОЛИЧЕСТВО МУЖЧИН ДО 50 = " + str(len(men_under_fifty.index)))
    print("\n")

    # провести сортировку по столбцу ‘Pclass’ в порядке возрастания;
    print("СОРТИРОВКА ПО PCLASS:")
    sorted_df = titanik_df.sort_values(by="Pclass")
    print(sorted_df)
    print("\n")

    # с использованием функции groupby вывести информацию о том, сколько
    # мужчин и женщин ехали в каютах каждого класса (1,2,3);
    print("МУЖЧИНЫ И ЖЕНЩИНЫ КАЖДОГО КЛАССА:")
    every_class_df = titanik_df.groupby(["Pclass", "Gender"])["Pclass"].count()
    print(every_class_df)
    print("\n")

    # провести анализ влияния класса пассажира на выживаемость при крушении.
    # Для этого определить процент выживших и не выживших пассажиров в
    # каютах 1, 2 и 3 класса. Вывести соответствующие числовые данные. Для
    # наглядности провести визуализацию результатов (построить столбиковые или
    # круговые диаграммы). Сделать выводы.
    print("ПРОЦЕНТ ВЫЖИВШИХ КАЖДОГО КЛАССА:")
    every_class_surviving_df = titanik_df.groupby(["Pclass", "Survived"], as_index=False).agg(Count=('Survived', 'count'))
    all_df = every_class_surviving_df.groupby(["Pclass"], as_index=False).agg(All=('Count', 'sum'))
    join_df = every_class_surviving_df.merge(all_df, on='Pclass', how='inner')
    join_df["Percent Of Surviving"] = round((join_df["Count"] / join_df["All"]) * 100, 2)
    print(every_class_surviving_df)
    print(all_df)
    print(join_df)
    print(join_df.columns)
    print("\n")

    print("ВЫВОД ДИАГРАММ")

    # Диаграмма не выживших
    show_diagram(join_df, 0, 'Процент не выживших')
    # Диаграмма выживших
    show_diagram(join_df, 1, 'Процент выживших')

    plt.show()


main()
