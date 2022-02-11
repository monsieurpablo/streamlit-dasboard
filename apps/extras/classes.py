# Create common Classess
class Topic:
    def __init__(self, name = '', sp_name = '', desc = '', t_desc = ''):
        self.name = name # Topic Name 
        self.sp_name = sp_name # Speckle Branch Name
        self.desc = desc # Simple Description 
        self.t_desc = t_desc # Technical description -> Expander 
        self.metrics = [] # list of metrics 
        
class Metric:
    def __init_(self, name, sp_name, desc, t_desc, unit, period, remarks = ''):
        self.name = name  # Display Name TODO should I set a variable name?
        self.sp_name = sp_name # Speckle Name 
        self.desc = desc # Simple Description
        self.t_desc = t_desc # Technichal Description -> Expander
        self.unit = unit # Unit for each analysis
        self.period = period # Period [Annual, Hourly, Day, Weekly]
        self.remarks = remarks # Consultant specific remarks for each project
            

        