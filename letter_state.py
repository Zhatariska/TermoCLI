class LetterState:
    def __init__(self, letra: str):
        self.letra: str = letra
        self.tem_na_palavra: bool = False
        self.ta_na_posicao: bool = False

    def __repr__(self):
        return f"[{self.letra} tem_na_palavra: {self.tem_na_palavra} ta_na_posicao: {self.ta_na_posicao}]"
        pass