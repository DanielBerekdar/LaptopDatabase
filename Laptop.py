class Laptop:
    #Laptop Attributes
    Model = None
    Manufacturer = None
    YearBuilt = None
    Condition = None
    Purchase_Price = None
    Selling_Price = None
    Serial = None
    Name = None
    #Constructor
    def __init__(self, Serial):
        self.Serial = Serial

    # Getters + Setters

    def SetName(self, Name):
        self.Name = Name

    def GetName(self):
        return self.Name

    def SetManufacturer(self, Manufacturer):
        self.Manufacturer = Manufacturer

    def GetManufacturer(self):
        return self.Manufacturer

    def SetYearBuilt(self, YearBuilt):
        self.YearBuilt = YearBuilt

    def GetYearBuilt(self):
        return self.YearBuilt

    def SetCondition(self, Condition):
        self.Condition = Condition

    def GetCondition(self):
        return self.Condition

    def SetPurchasePrice(self, Purchase_Price):
        self.Purchase_Price = Purchase_Price

    def GetPurchasePrice(self):
        return self.Purchase_Price

    def SetSellingPrice(self, Selling_Price):
        self.Selling_Price = Selling_Price

    def GetSellingPrice(self):
        return self.Selling_Price

    def SetSerial(self, Serial):
        self.Serial = Serial

    def GetSerial(self):
        return self.Serial

    def GetInfo(self):
        return self.Name, self.Manufacturer, self.YearBuilt, self.Condition, self.Purchase_Price, self.Selling_Price, self.Serial
