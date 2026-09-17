n = int(input())
c = int(input())
k = int(input())#ищем запись

position = k - 1  #место внутри страницы

page = position // (n * c) + 1

position_on_page = position % (n * c)

column = position_on_page // n + 1#столбец
row = position_on_page % n + 1#строка

print("страница", page, "столбец", column, "строка", row)