class IncomingData:
    # Initializer / Instance Attributes
    def __init__(self,name,units):
        self.name = name
        self.units = units
        self.value = 0.0

    def __repr__(self):
        return self.name +':'+ str(self.value)

    # instance method
    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def return_data(self):
        return self.data

    def get_units(self):
        return self.units
    
    def store_current_value(self):
        self.data = self.data +[self.value]