class Root:
    def action(self):
        print("Root: action")

class Left(Root):
    def action(self):
        print("Left: action, calling Root directly")
        # TODO 1: Wywołaj metodę action() z klasy Root bezpośrednio.
        #          Pamiętaj o przekazaniu 'self'.
        # __________
        super().action() # Dodatkowe wywołanie z super() dla porównania później

class Right(Root):
    def action(self):
        print("Right: action, calling Root directly")
        # TODO 2: Wywołaj metodę action() z klasy Root bezpośrednio.
        #          Pamiętaj o przekazaniu 'self'.
        # __________
        super().action() # Dodatkowe wywołanie z super() dla porównania później


class DiamondUnmanaged(Left, Right):
    def action(self):
        print("DiamondUnmanaged: action")
        # TODO 3: Wywołaj metodę action() z następnej klasy w MRO używając super().
        #          Co się stanie z wywołaniami Root.action()?
        # __________

class LeftSuper(Root):
    def action(self):
        print("LeftSuper: action")
        super().action()

class RightSuper(Root):
    def action(self):
        print("RightSuper: action")
        super().action()

class DiamondManaged(LeftSuper, RightSuper):
    def action(self):
        print("DiamondManaged: action")
        super().action()


# --- Testy ---
# print("--- Test DiamondUnmanaged (z bezpośrednimi wywołaniami) ---")
# d_unmanaged = DiamondUnmanaged()
# d_unmanaged.action()
# print("\nMRO dla DiamondUnmanaged:", [cls.__name__ for cls in DiamondUnmanaged.mro()])
# OCZEKIWANY EFEKT (przybliżony, zależy od super() w Left/Right):
# Root.action() będzie wywołane wielokrotnie z powodu bezpośrednich wywołań.
# Analiza: Ile razy Root.action() zostało wywołane i dlaczego?


# TODO bonus 4: W komentarzu opisz, ile razy Root.action() zostało wywołane dla d_unmanaged.action()
#         i dlaczego. Weź pod uwagę zarówno bezpośrednie wywołania, jak i te przez super()
#         dodane w klasach Left i Right.

# print("\n--- Test DiamondManaged (z konsekwentnym super()) ---")
# d_managed = DiamondManaged()
# d_managed.action()
# print("\nMRO dla DiamondManaged:", [cls.__name__ for cls in DiamondManaged.mro()])
# OCZEKIWANY EFEKT:
# Root.action() będzie wywołane tylko raz.

# TODO bonus 5: W komentarzu opisz, ile razy Root.action() zostało wywołane dla d_managed.action()
#         i dlaczego.