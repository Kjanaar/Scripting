import datetime

def print_factuur(total):
    """
    Print een factuur met de huidige datum en tijd en het totaalbedrag.
    
    Args:
        total (float): Het totaalbedrag van de factuur.
    """
    # Afdrukken van de kop van de factuur
    print("\n========== Factuur ==========")
    
    # Afdrukken van de bedrijfsnaam en de huidige datum en tijd
    print("XYZ Solutions")
    print(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-----------------------------")

    # Afdrukken van het totaalbedrag
    print(f"Totaal\t\t${total:.2f}\n")


while True:
    totaleprijs = 0

    # Welkomstbericht en instructies voor de gebruiker
    input("Welkom bij de factuurberekening van XYZ Solutions. Druk op enter om te beginnen...")

    while True:
        # Vraag om het product dat moet worden toegevoegd of om te stoppen
        product = input("Voer het product in dat je wilt toevoegen, typ 'klaar' om de totale prijs te tonen: ")
        if product.lower() == "klaar":
            break

        # Vraag om de prijs van het product en tel deze op bij het totaalbedrag
        prijs = float(input("Wat is de prijs van het product? "))
        totaleprijs += prijs

    # Print de factuur met het totaalbedrag
    print_factuur(totaleprijs)
