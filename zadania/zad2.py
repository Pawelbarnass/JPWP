# Zadanie 2: Zmiana dziedziczenia na kompozycję

class SimpleLogger:
    def log(self, message: str):
        print(f"[LOG] {message}")

# Wersja początkowa z dziedziczeniem (zakomentowana):
# class DataProcessor(SimpleLogger):
#     def process(self, data: str) -> str:
#         self.log(f"Rozpoczynam przetwarzanie danych: {data}")
#         processed_data = data.upper()
#         self.log(f"Zakończono przetwarzanie. Wynik: {processed_data}")
#         return processed_data

class DataProcessor:
    def __init__(self):
        # TODO: Zainicjalizuj obiekt SimpleLogger i przypisz go do atrybutu instancji,
        # np. self.logger
        self.logger = SimpleLogger()

    def process(self, data: str) -> str:
        # TODO: Użyj obiektu loggera (np. self.logger.log(...)) do logowania
        # informacji o rozpoczęciu przetwarzania.
        self.logger.log(f"Rozpoczynam przetwarzanie danych: {data}")

        processed_data = data.upper() # Symulacja przetwarzania

        # TODO: Użyj obiektu loggera do logowania informacji o zakończeniu przetwarzania.
        self.logger.log(f"Zakończono przetwarzanie. Wynik: {processed_data}")
        return processed_data

# Przykład użycia (po uzupełnieniu TODO):
# processor = DataProcessor()
# result = processor.process("przykladowe dane")
# print(f"Otrzymany wynik: {result}")