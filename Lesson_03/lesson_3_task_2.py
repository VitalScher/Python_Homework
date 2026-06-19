from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy Note 24", "+7(900)111-22-33"),
    Smartphone("Nokia", "X100", "+7(900)111-22-44"),
    Smartphone("Google", "Pixel 7", "+7(900)000-55-22"),
    Smartphone("Oppo", "A5", "+7(900)777-11-88"),
    Smartphone("Vivo", "V60", "+7(900)888-99-00"),
]

for smartphon in catalog:
    print(f"{smartphon.brand} - {smartphon.model}. {smartphon.number}")
