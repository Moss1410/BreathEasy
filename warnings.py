# This file contains all warnings and the functions for checking if alarms should be thrown

import dataTransferStorage as data


# Dictionary with warnings names and their range for trigger
# (Name: (Severity, Status, threshold, threshold comparison, units))
# Severity ranges from 0-5 (5 being the worst)
# Threshold comparison from 0-2, 0=less than, 1=greater than, 2=either direction of set
warnings = {
    ('Peak Pressure High':(4,0,40,1,'cmH20')), 
    ('Peak Pressure Low':(4,0,10,0,'cmH20')),
    ('PEEP High':(4,0,10,1,'cmH20')),
    ('PEEP Low':(4,0,5,0,'cmH20')),
    ('Loss of Data Transfer':(5,0,10,0,'')),
    ('Respiratory Rate Low':(4,0,data.settings_dict['min_RR'],0,'Breaths/min')),
    ('Ventilator Power Level':(5,0,0,0,'Voltage')),
    ('eTv not achieved':(4,0,10,2,'%')),
    ('iTv not achieved':(4,0,10,2,'%')),
    ('Min Leak':(4,0,0,0,'mL/min')),
    ('Max Leak':(4,0,50,1,'mL/min')),
    ('Low FiO2':(4,0,0.9,0,'mL/min')),
    ('High Fi02':(4,0,0.3,1,'mL/min'))
}



