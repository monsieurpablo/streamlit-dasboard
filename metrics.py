from classes import * 

## Daylight Autonomy 
DA = Metric()

DA.name = 'Daylight Autonomy'
DA.sp_name = 'da'
DA.period = 'Annual'
DA.unit = '% area above 300 lux in occupied hours'
DA.desc = """
    ### Daylight Autonomy 
    [DA] Daylight autonomy (DA) is a daylight
    availability metric that corresponds to the percentage of the occupied
    time when the target illuminance at a point in a space is met by
    daylight (Reinhart, 2001).
    
    A target illuminance of 300 lux and a threshold DA of 50%, meaning 50%
    of the time daylight levels are above the target illuminance, are values
    that are currently promoted in the Illuminating Engineering Society of
    North America (IESNA, 2013), see section 1.9.4.
    
    Metrics: (WIP) - Average DA300 - Mean DA300 - Uniformity Dmin/Dav
    """
DA.t_desc = """
    ## Technichal Description
    - Explain what is a grid-based simulation, what is lumens, and lux
    """


# UDI
UDI = Metric()

UDI.name = 'Useful Daylight Illuminance'
UDI.sp_name = 'udi'
UDI.desc = """
    ### Useful Daylight Illuminance [UDI] 
    Useful daylight illuminance (UDI)
    is a daylight availability metric that corresponds to the percentage of
    the occupied time when a target range of illuminances at a point in a
    space is met by daylight.

    Daylight illuminances in the range 100 to 300 lux are considered
    effective either as the sole source of illumination or in conjunction
    with artificial lighting. Daylight illuminances in the range 300 to
    around 3 000 lux are often perceived as desirable (Mardaljevic et al,
    2012).

    Recent examples in school daylighting design in the UK have led to
    recommendations to achieve UDI in the range 100-3 000 lux for 80% of
    occupancy hours.
    """
UDI.t_desc = """
    ## Technichal Description
    - Explain what is a grid-based simulation, what is lumens, and lux
    """

# Daylight Factor    
DF = Metric()

DF.name = 'Daylight Factor'
DF.sp_name = 'df'
DF.period = 'Point in time'
DF.unit = '%'
DF.desc = """
    ### Daylight Factor [DF] 
    Daylight factor (DF) is a daylight availability
    metric that expresses as a percentage the amount of daylight available
    inside a room (on a work plane) compared to the amount of unobstructed
    daylight available outside under overcast sky conditions (Hopkins,1963).
    The key building properties that determine the magnitude and
    distribution of the daylight factor in a space are (Mardaljevic, J.
    (2012)):

    - The size, distribution, location and transmission properties of the
        facade and roof windows.
    - The size and configuration of the space.
    - The reflective properties of the internal and external surfaces.
    - The degree to which external structures obscure the view of the sky.

    The higher the DF, the more daylight is available in the room. Rooms
    with an average DF of 2% or more can be considered daylit, but electric
    lighting may still be needed to perform visual tasks. A room will appear
    strongly daylit when the average DF is 5% or more, in which case
    electric lighting will most likely not be used during daytime (CIBSE,
    2002).
    """
DF.t_desc = """
    ## Technichal Description
    - Explain what is a grid-based simulation, what is lumens, and lux
    """

# VSC -> Vertical Sky Component

VSC = Metric()

VSC.name = 'Vertical Sky Component'
VSC.sp_name = 'vsc'
VSC.period = 'Point in time'
VSC.unit = '%'
VSC.desc = """
        ### Vertical Sky Component (VSC)
        The Building Research Establishment
        (BRE) have set out in their handbook ‘Site Layout Planning for Daylight
        and Sunlight a Guide to Good Practice (2011)’, guidelines and
        methodology for the measurement and assessment of daylight and sunlight
        within proposed buildings. One of the methods mentioned within section
        2.1 and Appendix C of the handbook is the Vertical Sky Component (VSC).

        The VSC is a unit of measurement that represents the amount of available
        daylight from the sky, received at a particular window. It is measured
        on the outside face of the window. This unit is expressed as a
        percentage as it is the ratio between the amount of sky visible at the
        given reference point compared to the amount of light that would be
        available from a totally unobstructed hemisphere of sky. To put this
        unit of measurement into perspective, the maximum percentage value for a
        window with a completely unobstructed view through 90° in every
        direction is close to 50%. In order to maintain good levels of daylight
        the BRE guidance recommend that the VSC of a window should be 27% or
        greater. However, the 2011 BRE Handbook makes allowance for different
        target values in cases where a higher degree of obstruction may be
        unavoidable such as historic city centres or modern high rise buildings.
        *Source: BRE 2011*

        While most planning authorities now require these assessments, it is
        noted in the BRE Guidelines that they should be treated as guidelines as
        opposed to rules. 

        The guidelines state that if the VSC is:

        - **At least 27%**, then conventional window design will usually give
          reasonable results.
        - **Between 15% and 27%**, then special measures (larger windows,
          changes to room layout) are usually needed to provide adequate
          daylight.
        - **Between 5% and 15%**, then it is very difficult to provide adequate
          daylight unless very large windows are used.
        - **Less than 5%**, then it is often impossible to achieve reasonable
          daylight, even if the whole window wall is glazed
        """

# ANNUAL RAD
AnnualRad = Metric()

AnnualRad.name = 'Annual Solar Irradiation'
AnnualRad.sp_name = 'annual'
AnnualRad.period = 'Annual'
AnnualRad.desc = """
    WIP
    Annual Solar Irradiation Description
    """
AnnualRad.t_desc= """
    Technichal description
    """

# SUMMER RAD    
SummerRad = Metric()

SummerRad.name = 'Typical Summer Day Solar Irradiation'
SummerRad.sp_name = 'summer'
SummerRad.period = 'day'
SummerRad.desc = """
    WIP
    Typical Summer Day Solar Irradiation
    """
SummerRad.t_desc= """
    Technichal description
    """

# WINTER RAD
SpringRad = Metric()

SpringRad.name = 'Typical Spring Day Solar Irradiation'
SpringRad.sp_name = 'spring'
SpringRad.period = 'day'
SpringRad.desc = """
    WIP
    Typical Spring Day Solar Irradiation
    """
SpringRad.t_desc= """
    Technichal descrition
    """

# WINTER RAD
WinterRad = Metric()

WinterRad.name = 'Typical Winter Day Solar Irradiation'
WinterRad.sp_name = 'winter'
WinterRad.period = 'day'
WinterRad.desc = """
    WIP
    Typical Winter Day Solar Irradiation
    """
WinterRad.t_desc= """
    TechnichaL
    """
    

