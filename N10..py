#10.?????????????
total_cost = float(input())
silver_count = 96
silver_price = 48
gold_count = silver_count / 16

gold_price = (total_cost - (silver_count * silver_price)) / gold_count
print(gold_price)