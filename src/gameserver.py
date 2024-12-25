from random import randint
from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.gamestate import GameState
from src.player import Player
import enum
from src.price import Price


class GamePhase(enum.StrEnum):
    BEGIN_ROUND = "Deal cards"
    CHOOSE_CARD = "Choose card"
    NEXT_PLAYER = "Switch current player"
    END_ROUND = "Price change"
    DECLARE_WINNER = "Winner"
    GAME_END = "End"


class GameServer:
    def __init__(self, player_types, gamestate):
        self.gamestate = gamestate
        self.player_types = player_types

    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()
        names = set()
        player_types = {}
        for i in range(player_count):
            while True:
                name, kind = cls.request_player()
                if name in names:
                    print("Имя должно быть уникальным. Попробуйте ещё раз.")
                else:
                    names.add(name)
                    player = Player(name, Hand())
                    player_types[player] = kind.lower()
                    break
        return player_types

    def new_game(self, player_types: dict):
        deck = Deck(cards=None)
        deck.shuffle()
        price = Price()
        player_list = list(player_types.keys())
        empty_cards = []
        self.gamestate = GameState(player_list, deck, price, cards=empty_cards)

    def run(self):
        current_phase = GamePhase.BEGIN_ROUND
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.BEGIN_ROUND: self.begin_round_phase,
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.END_ROUND: self.end_round_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def begin_round_phase(self) -> GamePhase:
        self.gamestate.deal_cards()
        print(f"****** {self.gamestate.round_index}-й раунд ******\n")
        print(f"Цена: {self.gamestate.price.save()}\n")
        return GamePhase.CHOOSE_CARD

    def choose_card_phase(self) -> GamePhase:
        current_player = self.gamestate.current_player()
        print("------ Ход игрока " + current_player.name + " ------")
        print("Карты на столе: " + str(self.gamestate.cards))
        while True:
            if self.player_types[current_player] == "human":
                card = input(current_player.name + ", какую карту тянем?: ")
                try:
                    card = Card.load(card)
                except ValueError:
                    print("Пожалуйста, введите корректное число.")
                    continue

                if card in self.gamestate.cards:
                    choose_card = card
                    self.gamestate.cards.remove(choose_card)
                    current_player.hand.card_list.append(choose_card)
                    print("Игрок " + current_player.name + " выбрал " + str(choose_card))
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, выберите номер карты из доступных.")

            if self.player_types[current_player] == "bot":
                choose_card = self.gamestate.cards[randint(0, len(self.gamestate.cards) - 1)]
                self.gamestate.cards.remove(choose_card)
                current_player.hand.card_list.append(choose_card)
                print("Игрок " + current_player.name + " (бот) выбрал " + str(choose_card))
                break
        return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        cards_length = len(self.gamestate.cards)  # Получаем длину списка карт
        if cards_length == GameState.MIN_PLAYABLE_CARD:
            remaining_card = self.gamestate.cards[0]  # Сохраняем оставшуюся карту
            print("На столе осталась карта " + str(remaining_card) + "\n")  # Упрощенный вывод с конкатенацией
            return GamePhase.END_ROUND
        else:
            self.gamestate.next_player()  # Переходим к следующему игроку
            return GamePhase.CHOOSE_CARD  # Возвращаем выбор карты

    def end_round_phase(self) -> GamePhase:
        print(f"****** {self.gamestate.round_index}-й раунд завершён ******\n")

        remaining_card = self.gamestate.cards[0]
        self.gamestate.price.add(remaining_card)

        self.gamestate.round_index += 1
        self.gamestate.cards.clear()  # Очистка стола от карт после раунда

        # Если раунд достиг максимального значения, конец игры
        if self.gamestate.round_index > GameState.MAX_ROUND:
            print(f'=== Итоговая цена ===\n {self.gamestate.price.save()}')
            return GamePhase.DECLARE_WINNER

        return GamePhase.BEGIN_ROUND  # Переход к следующему раунду (по умолчанию)

    def declare_winner_phase(self) -> GamePhase:
        max_score = 0
        winner = None
        player_score = {}
        players = self.gamestate.players
        for player in players:
            current_score = 0
            for card in player.hand.card_list:
                current_score += card.score(self.gamestate.price)
            player_score[player.name] = current_score
            if current_score > max_score:
                max_score = current_score
                winner = player
        for name in player_score.keys():
            score = player_score[name]
            print(name + ": " + str(score) + " очков")
        if winner != None:
            print(winner.name + " - Победитель: " + str(max_score) + " очков!")

        return GamePhase.GAME_END

    @staticmethod
    def request_player_count() -> int:
        count = 0
        while True:
            print("Введите количество игроков: ")
            player_input = input()
            try:
                count = int(player_input)
                if count >= 2 and count <= 6:  # Проверка на количество игроков
                    print(f'В игру играют {count} игрока')
                    return count
            except ValueError:
                print("Это не число, попробуйте еще раз.")
            print("Пожалуйста, введите число от 2 до 6: ")

    @staticmethod
    def request_player() -> (str, str):
        name = ""
        while True:
            name = input("Введите имя игрока: ")
            if name.isalpha():
                break
            print("Имя должно быть одним словом и не совпадать с предыдущими именами игроков")

        kind = ""
        while True:
            kind = input("Кто играет? (введите 'human' или 'bot') ")
            if kind.lower() == 'human' or kind.lower() == 'bot':
                break
            print("Допустимые типы игроков: 'human' или 'bot' \n")
            print("Повторите ввод заново: \n")

        return name, kind


def __main__():
    player_types = GameServer.get_players()
    server = GameServer(player_types, gamestate=None)
    server.new_game(player_types)
    server.run()


if __name__ == "__main__":
    from random import seed
    seed(7)
    __main__()
