N = int(input())

total_sum_all_cards = N * (N + 1) // 2
sum_remaining_cards = 0
for _ in range(N - 1):
    card_number = int(input())
    sum_remaining_cards += card_number
lost_card = total_sum_all_cards - sum_remaining_cards

print("Потерянная карточка:", lost_card)