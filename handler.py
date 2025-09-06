# Base class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        """
        Constructor to initialize the smartphone with unique values.
        - brand: str, e.g., "Samsung"
        - model: str, e.g., "Galaxy S21"
        - price: float, e.g., 799.99
        """
        self.brand = brand
        self.model = model
        self.price = price
        self._battery_level = 100  # Private attribute for encapsulation (battery level in %)
        self.is_on = False  # Public attribute to track if the phone is on

    # Method to turn on the phone
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now turned on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    # Method to turn off the phone
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now turned off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    # Method to charge the phone (demonstrates modification of private attribute)
    def charge(self, amount):
        if amount > 0:
            self._battery_level = min(100, self._battery_level + amount)
            print(f"{self.brand} {self.model} charged by {amount}%. Current battery: {self._battery_level}%")
        else:
            print("Charge amount must be positive.")

    # Getter method for battery level (encapsulation)
    def get_battery_level(self):
        return self._battery_level

    # Method to make a call (common behavior)
    def make_call(self, number):
        if self.is_on and self._battery_level > 0:
            print(f"{self.brand} {self.model} is calling {number}...")
            self._battery_level -= 5  # Simulate battery drain
        else:
            print(f"Cannot make call: Phone is off or battery is dead.")

    # Method to send a message (common behavior)
    def send_message(self, recipient, message):
        if self.is_on and self._battery_level > 0:
            print(f"{self.brand} {self.model} sending message to {recipient}: '{message}'")
            self._battery_level -= 1  # Simulate battery drain
        else:
            print(f"Cannot send message: Phone is off or battery is dead.")

    # Method to be overridden in subclasses (polymorphism)
    def update_os(self):
        print(f"Updating OS on {self.brand} {self.model}... (Generic update process)")


# Subclass for Android smartphones (inheritance)
class AndroidSmartphone(Smartphone):
    def __init__(self, brand, model, price, android_version):
        """
        Constructor extending the base class.
        - android_version: str, e.g., "Android 12"
        """
        super().__init__(brand, model, price)
        self.android_version = android_version

    # Overriding the update_os method (polymorphism)
    def update_os(self):
        print(f"Updating Android OS on {self.brand} {self.model} to the latest version via Google Play Services...")


# Subclass for iOS smartphones (inheritance)
class iOSSmartphone(Smartphone):
    def __init__(self, brand, model, price, ios_version):
        """
        Constructor extending the base class.
        - ios_version: str, e.g., "iOS 15"
        """
        super().__init__(brand, model, price)
        self.ios_version = ios_version

    # Overriding the update_os method (polymorphism)
    def update_os(self):
        print(f"Updating iOS on {self.brand} {self.model} to the latest version via Apple servers...")


# Demonstration of the classes
if __name__ == "__main__":
    # Create instances with unique values
    android_phone = AndroidSmartphone("Samsung", "Galaxy S21", 799.99, "Android 12")
    ios_phone = iOSSmartphone("Apple", "iPhone 13", 999.99, "iOS 15")

    # Using methods
    android_phone.turn_on()
    android_phone.make_call("123-456-7890")
    android_phone.send_message("Friend", "Hello!")
    print(f"Battery level: {android_phone.get_battery_level()}%")  # Encapsulation: accessing via getter

    ios_phone.turn_on()
    ios_phone.charge(20)
    ios_phone.make_call("987-654-3210")

    # Polymorphism: same method call, different behavior
    android_phone.update_os()
    ios_phone.update_os()


#PolymorphismChallenge

# Base class representing a Vehicle
class Vehicle:
    def __init__(self, brand, model):
        """
        Constructor to initialize the vehicle with unique values.
        - brand: str, e.g., "Toyota"
        - model: str, e.g., "Camry"
        """
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty string")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string")
        self.brand = brand
        self.model = model

    def move(self):
        """Base method to be overridden by subclasses."""
        print(f"{self.brand} {self.model} is moving... (Generic movement)")

    def modify_brand(self, prefix):
        """Modify the brand by adding a prefix."""
        if not isinstance(prefix, str) or not prefix.strip():
            raise ValueError("Prefix must be a non-empty string")
        self.brand = f"{prefix}{self.brand}"


# Subclass for Cars
class Car(Vehicle):
    def move(self):
        """Override move to represent driving."""
        print(f"{self.brand} {self.model} is driving 🚗")


# Subclass for Planes
class Plane(Vehicle):
    def move(self):
        """Override move to represent flying."""
        print(f"{self.brand} {self.model} is flying ✈️")


# Subclass for Boats
class Boat(Vehicle):
    def move(self):
        """Override move to represent sailing."""
        print(f"{self.brand} {self.model} is sailing ⛵")


# Subclass for Motorcycles
class Motorcycle(Vehicle):
    def move(self):
        """Override move to represent riding."""
        print(f"{self.brand} {self.model} is riding 🏍️")


# Subclass for Trains
class Train(Vehicle):
    def move(self):
        """Override move to represent rolling."""
        print(f"{self.brand} {self.model} is rolling 🚂")


def process_vehicle_file():
    """Read a vehicle file, modify brands, and write to a new file."""
    # Get input filename and prefix from user
    input_filename = input("Enter the filename to read (e.g., vehicles.txt): ").strip()
    brand_prefix = input("Enter prefix to add to vehicle brands (e.g., Super_): ").strip()

    try:
        vehicles = []
        # Read the input file
        try:
            with open(input_filename, 'r') as infile:
                for line in infile:
                    # Parse each line: vehicle_type,brand,model
                    data = line.strip().split(',')
                    if len(data) != 3:
                        print(f"Skipping invalid line: {line.strip()}")
                        continue

                    vehicle_type, brand, model = data
                    try:
                        # Create appropriate vehicle object based on type
                        vehicle_type = vehicle_type.lower()
                        if vehicle_type == "car":
                            vehicle = Car(brand, model)
                        elif vehicle_type == "plane":
                            vehicle = Plane(brand, model)
                        elif vehicle_type == "boat":
                            vehicle = Boat(brand, model)
                        elif vehicle_type == "motorcycle":
                            vehicle = Motorcycle(brand, model)
                        elif vehicle_type == "train":
                            vehicle = Train(brand, model)
                        else:
                            print(f"Skipping line with unknown vehicle type: {line.strip()}")
                            continue

                        # Apply brand modification
                        vehicle.modify_brand(brand_prefix)
                        vehicles.append(vehicle)
                    except ValueError as e:
                        print(f"Error processing line '{line.strip()}': {e}")
                        continue

        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist.")
            return
        except PermissionError:
            print(f"Error: Permission denied to read '{input_filename}'.")
            return
        except IOError as e:
            print(f"Error: An I/O error occurred while reading '{input_filename}': {e}")
            return

        # Write modified data to a new file
        output_filename = f"modified_{input_filename}"
        try:
            with open(output_filename, 'w') as outfile:
                for vehicle in vehicles:
                    outfile.write(f"{vehicle.__class__.__name__},{vehicle.brand},{vehicle.model}\n")
            print(f"Modified data written to '{output_filename}'.")
        except PermissionError:
            print(f"Error: Permission denied to write to '{output_filename}'.")
            return
        except IOError as e:
            print(f"Error: An I/O error occurred while writing '{output_filename}': {e}")
            return

        # Demonstrate polymorphism with move()
        for vehicle in vehicles:
            vehicle.move()

    except Exception as e:
        print(f"Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    process_vehicle_file()
