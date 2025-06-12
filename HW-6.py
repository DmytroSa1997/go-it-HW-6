class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """Додає номер телефону до списку phones"""
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        """Видаляє номер телефону зі списку phones"""
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
        """Редагує номер телефону, замінюючи старий на новий"""
        # Перевіряємо, чи існує старий номер
        if not any(phone.value == old_phone for phone in self.phones):
            raise ValueError(f"Phone number {old_phone} not found")
        # Видаляємо старий номер і додаємо новий (з валідацією)
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone_number):
        """Шукає номер телефону у списку phones"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"