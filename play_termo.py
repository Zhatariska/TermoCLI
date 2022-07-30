from typing import List
from letter_state import LetterState
from termo import Termo
from colorama import Fore
import random


def main():
    word_set = load_word_set('secret_word.txt')
    secret = random.choice(list(word_set))
    termo = Termo(secret)

    while termo.can_attempt:
        x = input("\nType your guess:")


        if len(x) != termo.WORD_LEN:
            if x == "surrender":
                print("Mais sorte na próxima vez.")
                print(f'A palavra era {secret}...')
                exit()
            print(Fore.RED + f'A Palavra deve ter {termo.WORD_LEN} letras' + Fore.RESET)
            continue


        termo.attempt(x)
        display_results(termo)

    if termo.is_solved:
        print("Parabéns!")
    else:
        print("Mais sorte na próxima vez.")
        print(f'A palavra era {secret}...')


def display_results(termo: Termo):
    print("\n Your result so far...\n")

    lines = []

    for word in termo.attempts:
        result = termo.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(termo.tentativas_restantes):
        lines.append(' '.join(['_'] * termo.WORD_LEN))

    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[str]):
    result_with_color = []
    for letter in result:
        if letter.ta_na_posicao:
            color = Fore.GREEN
        elif letter.tem_na_palavra:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.letra + Fore.RESET
        result_with_color.append(colored_letter)
    return ' '.join(result_with_color)

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):

    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)



if __name__ == "__main__":
    main()