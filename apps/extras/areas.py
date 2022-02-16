from unicodedata import name
from classes import *
import metrics as m

daylight = Topic()

daylight.name = 'Daylight'
daylight.sp_name = 'daylight'
daylight.desc = """## Daylight
    ."""

daylight.t_desc = """
    Technichal description
"""

daylight.metrics.extend([m.DA, m.UDI, m.DF])


solrad = Topic()

solrad.name = 'Solar Irradiation'
solrad.sp_name = 'rad'
solrad.desc = """
    ## Solar Gain 
    
    """
    
solrad.t_desc = """
    Technichal description
    """
    
solrad.metrics.extend([m.AnnualRad, m.SummerRad, m.SpringRad, m.WinterRad])

print(solrad.metrics[0].name)