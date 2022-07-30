from pygame import init

from letter_state import LetterState


class Termo:

    MAX_ATTEMPTS = 6
    WORD_LEN = 5
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)


    def guess(self, word: str):
        word = word.upper()
        result = []

        for i in range(self.WORD_LEN):
            character = word[i]
            letter = LetterState(character)
            letter.tem_na_palavra = character in self.secret
            letter.ta_na_posicao = character == self.secret[i]
            result.append(letter)

        return result


    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret


    @property
    def tentativas_restantes(self) -> init:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return len(self.attempts) < self.MAX_ATTEMPTS and not self.is_solved