# 1. Розбити текст по словам
# 2. В кожному слові: знайти 1-ий символ, що не повторюється в слові
# 3. Прибрати усі дублікати (2 і більше разів) -> список
# 4. Взяти перший символ -> символ
import re


# обробка тексту: видалення розділових знаків, пробілів
def get_input() -> list:
    text = input("Введіть текст: ")
    text = text.lower().strip()
    if text:
        punctuation = ['.', ',', '"', "'", ';', ':', '[', ']', '>', '<', '!', '-', '\n', '\t']
        for p in punctuation:
            text = text.replace(p, '')
        return re.sub(' +', ' ', text.strip()).split(' ')
    return []


# пошук першого не-дублікату
def find_symbol(word: str) -> str:
    try:
        return remove_duplicates(li=[*word])[0]
    except Exception:
        print()


# видалення дублікатів
def remove_duplicates(li: list) -> list:
    d = dict.fromkeys(li)
    d.update({i: li.count(i) for i in li})
    res = [k for k in d if d[k] == 1]
    return [] if not res else res


if __name__ == '__main__':
    words = get_input()
    if words:
        symbols = [find_symbol(word=word) for word in words]
        removed_dupl = remove_duplicates(li=symbols)
        if removed_dupl:
            symbol = removed_dupl[0]
        else:
            symbol = "Не знайдено такого символу"
        print(symbol)
    else:
        print("Помилка в тексті")
