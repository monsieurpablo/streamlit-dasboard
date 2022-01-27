from unicodedata import name
from classes import *
import metrics as m

daylight = Topic()

daylight.name = 'Daylight'
daylight.sp_name = 'daylight'
daylight.desc = """## Daylight
    Daylight in buildings is composed of a mix – direct sunlight,
    diffuse skylight, and light reflected from the ground and surrounding
    elements. Daylighting design needs to consider orientation and building site
    characteristics, facade and roof characteristics, size and placement of
    window openings, glazing and shading systems, and geometry and reflectance
    of interior surfaces. Good daylighting design ensures adequate light during
    daytime."""

daylight.t_desc = """
    Technichal description
"""

daylight.metrics.extend([m.DA, m.UDI, m.DF])


solrad = Topic()

solrad.name = 'Solar Irradiation'
solrad.sp_name = 'rad'
solrad.desc = """
    ## Solar Gain 
    Solar gain is short wave radiation from the sun that heats a
    building, either directly through an opening such as a window, or indirectly
    through the fabric of the building. Solar design (or passive solar design)
    is an aspect of passive building design that focusses on maximizing the use
    of heat energy from solar radiation. 
    
    Very broadly, solar gain can be beneficial in cooler climates when it can be
    used as a passive way of heating buildings. However, too much solar gain can
    cause overheating and for this reason, Part L of the UK building regulations
    places restrictions on the amount of glazing that can be used in buildings.
    """
    
solrad.t_desc = """
    Technichal description
    """
    
solrad.metrics.extend([m.AnnualRad, m.SummerRad, m.SpringRad, m.WinterRad])

print(solrad.metrics[0].name)