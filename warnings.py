# This file contains all warnings and the functions for checking if alarms should be thrown

# Severity ranges from 0-5 (5 being the worst)
# Threshold comparison from 0-2, 0=less than, 1=greater than, 2=either direction of set
import data

class Warning:
    def __init__(self, name, severity, status, threshold, comparison_type, units,incoming_data):
        self.name = name
        self.severity = severity
        self.status = status
        self.threshold = threshold
        self.comparison_type = comparison_type
        self.units = units
        self.incoming_data = incoming_data
    
    def __repr__(self):
        return self.name + ': ' + self.status

    def set_status(self, new_status):
        self.status = new_status

    def get_name(self):
        return self.name
    
    def set_threshold(self, new_threshold):
        self.threshold = new_threshold

    def get_status(self):
        return self.status
    
    def get_severity(self):
        return self.severity
    
    def get_threshold(self):
        return self.threshold
    
    def get_comparison_type(self):
        return self.comparison_type
    
    def get_sensor_data(self):
        return self.incoming_data


warnings_list = []
# Define Warnings and Initial Settings based on standards
peek_pressure_high = Warning('Peak Pressure High', 4,0,40,1,'cmH20',data.expiratory_flow)
peek_pressure_low = Warning('Peak Pressure Low',4,0,10,0,'cmH20',data.expiratory_flow)
PEEP_high = Warning('PEEP High',4,0,10,1,'cmH20',data.expiratory_flow,)
PEEP_low = Warning('PEEP High',4,0,10,1,'cmH20',data.expiratory_flow)
loss_of_data_transfer = Warning('PEEP High',4,0,10,1,'cmH20',data.expiratory_flow)
respiratory_rate_low = Warning('Respiratory Rate Low',4,0,data.min_RR.get_value(),0,'Breaths/min',data.expiratory_flow)
ventilator_power_level = Warning('Ventilator Power Level',5,0,0,0,'Voltage',data.expiratory_flow)
eTv_not_achieved = Warning('eTv not achieved',4,0,10,2,'%',data.expiratory_flow)
iTv_not_achieved = Warning('iTv not achieved',4,0,10,2,'%',data.expiratory_flow)
min_leak = Warning('Min Leak',4,0,0,0,'mL/min',data.expiratory_flow)
max_leak = Warning('Max Leak',4,0,50,1,'mL/min',data.expiratory_flow)
low_FiO2 = Warning('Low FiO2',4,0,0.9,0,'mL/min', data.expiratory_flow,)
high_Fi02 = Warning('High Fi02',4,0,0.3,1,'mL/min',data.expiratory_flow)

def init_warnings():
    global warnings_list
    warnings_list += [peek_pressure_high]
    warnings_list += [peek_pressure_low]
    warnings_list += [PEEP_high]
    warnings_list += [PEEP_low]
    warnings_list += [loss_of_data_transfer]
    warnings_list += [respiratory_rate_low]
    warnings_list += [eTv_not_achieved]
    warnings_list += [iTv_not_achieved]
    warnings_list += [min_leak]
    warnings_list += [max_leak]
    warnings_list += [low_FiO2]
    warnings_list += [high_Fi02]


# Warning Management -Know when to display warnings
def check_all_warning_status():
    global warnings_list
    for warning in warnings_list:
        return
    #this is undeveloped functionality, must check warning limits against corresonding sensor information



