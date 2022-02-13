[_metadata_:author]:- "Pablo Arango"
[_metadata_:tags]:- "markdown metadata"

[_metadata_:tags]:- "what properties do I want here?"

sp_name = "daylight"

The convencion is
- H1 headers are `topics`
- H2 headers are `metrics`
- H3 headers are `details`(to be hidden in an expander)
- `[]` Would be parsed as short form

Metadata tags could be use to enrich parsing data to the python script.

# Daylight 
Daylight in buildings is composed of a mix – direct sunlight, diffuse skylight, and light reflected from the ground and surrounding elements. Daylighting design needs to consider orientation and building site characteristics, facade and roof characteristics, size and placement of window openings, glazing and shading systems, and geometry and reflectance of interior surfaces. Good daylighting design ensures adequate light during daytime

## Daylight Autonomy [DA]
Daylight autonomy (DA) is a daylight availability metric that corresponds to the percentage of the occupied time when the target illuminance at a point in a space is met by daylight (Reinhart, 2001). A target illuminance of 300 lux and a threshold DA of 50%, meaning 50% of the time daylight levels are above the target illuminance, are values that are currently promoted in the Illuminating Engineering Society of North America (IESNA, 2013), see section 1.9.4. 

Metrics: (WIP) - Average DA300 - Mean DA300 - Uniformity Dmin/Dav

### Detailed Description
Explain what is a grid-based simulation, what is lumens, and lux

## Useful Daylight Illuminance [UDI] 
Useful daylight illuminance (UDI) is a daylight availability metric that corresponds to the percentage of the occupied time when a target range of illuminances at a point in a space is met by daylight. Daylight illuminances in the range 100 to 300 lux are considered effective either as the sole source of illumination or in conjunction with artificial lighting. Daylight illuminances in the range 300 to around 3 000 lux are often perceived as desirable (Mardaljevic et al, 2012). Recent examples in school daylighting design in the UK have led to recommendations to achieve UDI in the range 100-3 000 lux for 80% of occupancy hours.

### Detailed Description
Explain what is a grid-based simulation, what is lumens, and lux

## Daylight Factor [DF]
Daylight factor (DF) is a daylight availability metric that expresses as a percentage the amount of daylight available inside a room (on a work plane) compared to the amount of unobstructed daylight available outside under overcast sky conditions (Hopkins,1963). The key building properties that determine the magnitude and distribution of the daylight factor in a space are (Mardaljevic, J. (2012)): 
- The size, distribution, location and transmission properties of the facade and roof windows. 
- The size and configuration of the space. 
- The reflective properties of the internal and external surfaces. 
- The degree to which external structures obscure the view of the sky. 

The higher the DF, the more daylight is available in the room. Rooms with an average DF of 2% or more can be considered daylit, but electric lighting may still be needed to perform visual tasks. A room will appear strongly daylit when the average DF is 5% or more, in which case electric lighting will most likely not be used during daytime (CIBSE, 2002).

### Detailed Description
Explain what is a grid-based simulation, what is lumens, and lux


## Vertical Sky Component [VSC]
The Building Research Establishment (BRE) have set out in their handbook ‘Site Layout Planning for Daylight and Sunlight a Guide to Good Practice (2011)’, guidelines and methodology for the measurement and assessment of daylight and sunlight within proposed buildings. One of the methods mentioned within section 2.1 and Appendix C of the handbook is the Vertical Sky Component (VSC). 

The VSC is a unit of measurement that represents the amount of available daylight from the sky, received at a particular window. It is measured on the outside face of the window. This unit is expressed as a percentage as it is the ratio between the amount of sky visible at the given reference point compared to the amount of light that would be available from a totally unobstructed hemisphere of sky. To put this unit of measurement into perspective, the maximum percentage value for a window with a completely unobstructed view through 90° in every direction is close to 50%. In order to maintain good levels of daylight the BRE guidance recommend that the VSC of a window should be 27% or greater. 

However, the 2011 BRE Handbook makes allowance for different target values in cases where a higher degree of obstruction may be unavoidable such as historic city centres or modern high rise buildings. *Source: BRE 2011* While most planning authorities now require these assessments, it is noted in the BRE Guidelines that they should be treated as guidelines as opposed to rules. The guidelines state that if the VSC is: 

- **At least 27%**, then conventional window design will usually give reasonable results. 
- **Between 15% and 27%**, then special measures (larger windows, changes to room layout) are usually needed to provide adequate daylight. 
- **Between 5% and 15%**, then it is very difficult to provide adequate daylight unless very large windows are used.
- **Less than 5%**, then it is often impossible to achieve reasonable daylight, even if the whole window wall is glazed.

# Solar Irradiation
Solar gain is short wave radiation from the sun that heats a building, either directly through an opening such as a window, or indirectly through the fabric of the building. Solar design (or passive solar design) is an aspect of passive building design that focusses on maximizing the use of heat energy from solar radiation. 

Very broadly, solar gain can be beneficial in cooler climates when it can be used as a passive way of heating buildings. However, too much solar gain can cause overheating and for this reason, Part L of the UK building regulations places restrictions on the amount of glazing that can be used in buildings.

## Annual Solar Irradiation
Cumulative Solar Irradiation between 1st of January and 31 of December
## Sunny Summer Day
Considers a sunny day between Jun 10th to Jun 30th
## Sunny Spring Day
Considers a sunny day between March 10th to March 30th
## Sunny Winter Day
Considers a sunny day between December 10th to December 30th

# Outdoor Wind Comfort
Pedestrian wind comfort studies take into consideration meteorological data, aerodynamics, and comfort criteria. The data regarding the latter two is provided by wind tunnel testing (physical experiments) and numerical simulation with computational fluid dynamics (CFD) software. 

Simulation can digitally model the airflow over and around a building or urban area and is a faster and less costly approach than physical experiments, but it is not meant to exclude them. Both techniques are used together in a construction project in order to ensure all required data is provided and adequate testing ensured. 

By assessing pedestrian wind comfort with CFD, urban master planners, civil engineers, and architects can predict the behavior of wind flow around buildings early, and benefit from an iterative design process. Wind speeds and other parameters can be calculated at pedestrian levels, and comfort can be evaluated based on given criteria. 

## Wind Velocity
- x
- y
- z
### Detailed Description
Explain what is a grid-based simulation, what is lumens, and lux

## Lawson Criteria
- x
- y
- z
### Detailed Description
Explain what is a grid-based simulation, what is lumens, and lux
                    
# Outdoor Thermal Comfort
## Universal Thermal Comfort Index [UTCI]
Here goes the descrition on the UTCI metric
### Detailed Description
- x
- y
- z

## Psychological Equivalent Temperature [PET]
Here goes the descrition on the UTCI metric
### Detailed Description
- x
- y
- z


# Air Quality
Here goes the description on the importance of the Air quality in buildings 
## Vehicle pollutants concentration
Talk about how it's done
### Detailed Description
ADMS and how it works
- x
- y
- z


# Sun Availability (Sun Hours)