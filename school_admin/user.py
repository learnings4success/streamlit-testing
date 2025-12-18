class User:
    def __init__(self, name, age, address, phone_number):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"""
            Name:       {self.name},
            Age:        {self.age},
            Address:    {self.address},
            Phone:      {self.phone_number}
        """