class Ingredient:
    # Отдельные ингредиенты рецепта
    # ing = Ingredient(name, volume, measure)
    def __init__(self, name, volume, measure) -> None:
        self.name = name  # название ингредиента (строка);
        self.volume = volume  #  объем ингредиента в рецепте (вещественное число);
        self.measure = measure  # единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

    def __str__(self):
        # название: объем, ед. изм.
        return f"{self.name}: {self.volume}, {self.measure}"

    def __repr__(self):
        # название: объем, ед. изм.
        return f"{self.name}: {self.volume}, {self.measure}"


# ing = Ingredient("Соль", 1, "столовая ложка")
# print(str(ing))  # Соль: 1, столовая ложка


class Recipe:
    def __init__(self, *args) -> None:
        self._list_ingredients = list(args)

    def add_ingredient(self, ing):
        # добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
        if type(ing) == Ingredient:
            self._list_ingredients.append(ing)

    def remove_ingredient(self, ing):
        # удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
        if ing in self._list_ingredients:
            self._list_ingredients.remove(ing)

    def get_ingredients(self):
        # получение кортежа из объектов класса Ingredient текущего рецепта.
        return tuple(self._list_ingredients)

    def __len__(self):
        # возвращает число ингредиентов в рецепте.
        return len(self._list_ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
print(ings)
n = len(recipe)  # n = 3
print(n)


class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords


poly = PolyLine((1, 2), (3, 5))
poly.add_coord(5, 4)

print(len(poly.get_coords()))
print(poly.get_coords())
