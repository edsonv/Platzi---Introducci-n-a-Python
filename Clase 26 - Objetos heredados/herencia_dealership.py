class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} {self.model} ha sido vendido.")
        else:
            print(f"El vehículo {self.brand} {self.model} no está disponible.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"


class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicileta {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"


class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"

    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"


class Customer:
    def __init__(self, name):
        self.name = name
        self.puchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.puchased_vehicles.append(vehicle)
        else:
            print(f"El vehículo {vehicle.brand} {vehicle.model} no está disponible.")

    def inquiry_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "Disponible"
        else:
            availability = "No disponible"
            print(
                f"El vehículo {vehicle.brand} {vehicle.model} está {availability} y cuesta {vehicle.get_price()}"
            )


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(
            f"El vehículo {vehicle.brand} {vehicle.model} ha sido añadido al inventario."
        )

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado.")

    def show_available_vehicles(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} {vehicle.model} - ${vehicle.get_price()}")
