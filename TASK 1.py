class Mobile:
   def __init__(self,mobile_name,version,battery_power,price):
    self.mobile_name=mobile_name
    self.version=version
    self.battery_power=battery_power
    self.__price=price
class Tecno(Mobile):
    def __init__(self,mobile_name,version,battery_power,price):
      super().__init__(mobile_name,version,battery_power,price)
           
class Samsung(Tecno):
    def __init__(self, mobile_name, version, battery_power, price):
        super().__init__(mobile_name, version, battery_power, price)

    def display_details(self):
        print("Mobile Name:", self.mobile_name)
        print("Version:", self.version)
        print("Battery Power:", self.battery_power)
        print("Price: Confidential")
       # Demonstrating Data Hiding:
        try:
            print("Price:", self.__price)
        except AttributeError:
            print("Price: [ACCESS DENIED] This data is hidden.")


phone = Samsung("Galaxy", "S23", "5000mAh", 70000)
phone.display_details()

