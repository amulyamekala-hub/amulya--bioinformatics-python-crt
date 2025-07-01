#write a python program to cerate a mobile class and declare the states of mobile as color price brand series version features storage battery capacity ram,processer create 10 objects and initialize using constructor print the details of the individual obeject using fumction
class Mobile:
    def __init__(self,colour,price,brand,series, version, features, storage, battery_capacity):
        self.colour= colour
        self.price= price
        self.brand= brand
        self.series=series
        self.version=version
        self.features=features
        self.storage=storage
        self.battery_capacity=battery_capacity
def display_details(self):
    print(f"Colour: {self.colour}")
    print(f"Price: ₹{self.price}")
    print(f"Brand: {self.brand}" )
    print(f"Series: {self.series}")
    print(f"Version: {self.version}")
    print(f"Features: {', '.join(self.features)}")
    print(f"Storage: {self.storage}GB")
    print(f"Battery: {self.battery_capacity}mAh")
    print("-" * 60)
M1=Mobile("Black", 69999, "Samsung", "Galaxy S", "S23 Ultra", ["5G", "AMOLED", "QuadCamera"], 256, 5000)
M2=Mobile("White", 79999, "Apple", "iPhone", "14 Pro", ["Face ID", "Retina Display", "A16 Chip"], 128, 3200)
M3=Mobile("Blue", 29999, "Xiaomi", "Redmi Note", "12 Pro", ["Fast Charging", "120Hz Display"], 128, 5000)
M4=Mobile("Grey", 34999, "OnePlus", "Nord", "3 5G", ["OxygenOS", "HDR10+"], 256, 4500),
M5=Mobile("Silver", 114999, "Apple", "iPhone", "15 Pro Max", ["Titanium Body", "USB-C", "LiDAR"], 512, 4422)
M6=Mobile("Green", 24999, "Realme", "Narzo", "60x", ["AI Camera", "Ultra Savings Mode"], 128, 5000)
M7=Mobile("Purple", 55999, "Samsung", "Galaxy A", "54 5G", ["No Charger", "Knox Security"], 256, 5000)
M8=Mobile("Red", 14999, "Motorola", "G Series", "G73", ["Stereo Speakers", "Dolby Atmos"], 128, 5000)
M9=Mobile("Gold", 99999, "Google", "Pixel", "8 Pro", ["Tensor G3", "Material You"], 256, 5050)
M10=Mobile("Midnight", 15999, "Lava", "Blaze", "5G", ["Glass Back", "Clean UI"], 128, 5000)
display_details(M1)
display_details(M2)
display_details(M3)
display_details(M5)
display_details(M6)
display_details(M7)
display_details(M8)
display_details(M9)
display_details(M10)
