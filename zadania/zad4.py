class LoggingMixin:
    def log(self, message):
        print(f"[LOG - {self.__class__.__name__}] {message}")

class EnsureLoggingMeta(type):
    def __new__(mcs, name, bases, attrs):
        # TODO 1: Sprawdź, czy LoggingMixin jest już w `bases` lub czy którakolwiek
        #         klasa w `bases` dziedziczy po LoggingMixin.
        #         Jeśli nie, dodaj LoggingMixin na koniec krotki `bases`.
        #         Wskazówka: issubclass(cls, LoggingMixin) może być pomocne dla istniejących baz.
        #                  Aby dodać, utwórz nową krotkę.
        
        needs_mixin = True
        if LoggingMixin in bases:
            needs_mixin = False
        else:
            for base_cls in bases:
                if issubclass(base_cls, LoggingMixin):
                    needs_mixin = False
                    break
        
        if needs_mixin:
            # __________ # Uzupełnij tworzenie nowej krotki `bases`
            pass # Usuń to 'pass' po uzupełnieniu

        print(f"Tworzenie klasy '{name}' z bazami: {[b.__name__ for b in bases]}")
        return super().__new__(mcs, name, bases, attrs)

class ServiceBase:
    def perform_action(self):
        # self.log("Rozpoczęto akcję w ServiceBase") # Ta linia dałaby błąd, gdyby nie było log
        print("ServiceBase: Wykonuję podstawową akcję.")

# Klasa, która powinna automatycznie otrzymać LoggingMixin
class MyService(ServiceBase, metaclass=EnsureLoggingMeta):
    def specific_task(self):
        self.log("Wykonuję specyficzne zadanie w MyService.") # Oczekujemy, że self.log będzie dostępne
        super().perform_action()
        self.log("Zakończono specyficzne zadanie.")

# Klasa, która już ma LoggingMixin (bezpośrednio lub pośrednio)
class AnotherService(LoggingMixin, ServiceBase, metaclass=EnsureLoggingMeta):
    def other_task(self):
        self.log("Wykonuję inne zadanie w AnotherService.")
        super().perform_action() # super() tutaj odniesie się do ServiceBase lub LoggingMixin w zależności od MRO
        self.log("Zakończono inne zadanie.")


# --- Testy ---
# TODO 2: Uruchom kod i zaobserwuj MRO oraz działanie.
#         Czy metoda log() jest dostępna w instancjach MyService?
#         Co się dzieje z AnotherService?

# print("\n--- Test MyService ---")
# s1 = MyService()
# s1.specific_task()
# print("MRO dla MyService:", [cls.__name__ for cls in MyService.mro()])

# print("\n--- Test AnotherService ---")
# s2 = AnotherService()
# s2.other_task()
# print("MRO dla AnotherService:", [cls.__name__ for cls in AnotherService.mro()])

# TODO bonus 3: W komentarzu wyjaśnij, dlaczego `self.log` działa w `MyService`.
#         Jak metaklasa wpłynęła na dziedziczenie `MyService`?