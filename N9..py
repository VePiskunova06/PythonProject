#9.
flight = input("номер рейса: ")
company_ru = input("название авиакомпании (на русском языке): ")
company_en = input("название авиакомпании (на английском языке): ")
city_ru = input("город прилета (на русском языке): ")
city_en = input("город прилета (на английском языке): ")

print(f"Заканчивается посадка на рейс {flight} {company_ru} до {city_ru}")
print(f"This is the final boarding call for {company_en} flight {flight} to {city_en}")