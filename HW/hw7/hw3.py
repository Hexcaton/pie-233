def determine_winner(votes):
    candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]
    votes_count = {candidate: 0 for candidate in candidates}
    for vote in votes:
        if vote in candidates:
            votes_count[vote] += 1
    max_votes = max(votes_count.values())
    winners = [candidate for candidate, count in votes_count.items() if count == max_votes]
    if len(winners) == 2:
        winners.sort(key=len)
        winner = winners[0]
    else:
        winner = winners[0]
    return winner, max_votes

votes_list = []
while True:
    vote = input("Вы отдаете голос за (или введите 'стоп' для завершения): ").capitalize()
    if vote == "Стоп":
        break
    votes_list.append(vote)
winner_name, winner_votes = determine_winner(votes_list)
print("Победитель выборов:", winner_name, "с количеством голосов",winner_votes)