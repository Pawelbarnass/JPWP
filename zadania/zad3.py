class A:
    def process(self, data: list):
        print("A: processing")
        data.append("A")
        # TODO 1: Jeśli A nie jest ostatnią klasą w MRO (co jest rzadkie, ale możliwe),
        #         super().process(data) byłoby tutaj. W naszym przypadku A jest korzeniem,
        #         więc tu nie ma potrzeby wywoływania super().
        return data

class B(A):
    def process(self, data: list):
        print("B: processing")
        data.append("B")
        # TODO 2: Wywołaj metodę process() z następnej klasy w MRO dla B
        #          używając super(). Pamiętaj o przekazaniu argumentu `data`.
        # __________ # Uzupełnij tę linię
        return data

class C(A):
    def process(self, data: list):
        print("C: processing")
        data.append("C")
        # TODO 3: Wywołaj metodę process() z następnej klasy w MRO dla C
        #          używając super(). Pamiętaj o przekazaniu argumentu `data`.
        # __________ # Uzupełnij tę linię
        return data

class D(B, C): # Kolejność (B, C) ma znaczenie dla MRO
    def process(self, data: list):
        print("D: processing")
        data.append("D")
        # TODO 4: Wywołaj metodę process() z następnej klasy w MRO dla D
        #          używając super(). Pamiętaj o przekazaniu argumentu `data`.
        # __________ # Uzupełnij tę linię
        return data

# Sprawdzenie MRO (Method Resolution Order) dla klasy D
# print("MRO dla D:", [cls.__name__ for cls in D.mro()])
# Oczekiwane MRO dla D: ['D', 'B', 'C', 'A', 'object']

# Kod testowy (powinien działać po uzupełnieniu TODO)
# d_instance = D()
# result = d_instance.process([])
# print(f"\nKońcowy wynik przetwarzania: {result}")

# Oczekiwany wynik konsoli (kolejność printów):
# D: processing
# B: processing
# C: processing
# A: processing

# Oczekiwany końcowy wynik przetwarzania (lista):
# ['D', 'B', 'C', 'A']