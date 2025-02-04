from удобства import *


def быстрая_сортировка(список_для_сортировки: список,
                        ключ_сортировки: Вызываемый = тождественное_отображение) -> список | Ничего:
    if длина(список_для_сортировки) < 2:
        return список_для_сортировки

    опорный_элементы = ключ_сортировки(список_для_сортировки[длина(список_для_сортировки)//2])
    левый, средний, правый = список(), список(), список()
    for элемент in список_для_сортировки:
        характеристика_элемента = ключ_сортировки(элемент)
        if характеристика_элемента < опорный_элементы:
            левый.добавить(элемент)
        elif характеристика_элемента > опорный_элементы:
            правый.добавить(элемент)
        else:
            средний.добавить(элемент)

    return быстрая_сортировка(левый) + средний + быстрая_сортировка(правый)


мой_список = список([5, 4, -5, -1, 1, 3, 7])
печатать(
    *быстрая_сортировка(
        список_для_сортировки=мой_список,
        ключ_сортировки=модуль
    )
)