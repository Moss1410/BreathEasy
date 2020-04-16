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

    def show_warning(self):
        #DISPLAY OR DO SOMTHING???
        return

inc = data.IncomingDatas()
sett= data.Settings()
warnings_list = []

class Warnings():
    def __init__(self):
        self.peek_pressure_high = Warning('Peak Pressure High', 4,0,40,1,'cmH20',inc.inspiratory_pressure)
        self.peek_pressure_low = Warning('Peak Pressure Low',4,0,10,0,'cmH20',inc.inspiratory_pressure)
        self.PEEP_high = Warning('PEEP High',4,0,10,1,'cmH20',inc.expiratory_pressure) # i was changing these, but i think youve been removing them liv
        self.PEEP_low = Warning('PEEP High',4,0,10,1,'cmH20',inc.expiratory_pressure)
        self.loss_of_data_transfer = Warning('PEEP High',4,0,10,1,'cmH20',inc.expiratory_flow)
        self.respiratory_rate_low = Warning('Respiratory Rate Low',4,0,sett.min_RR.get_value(),0,'Breaths/min',inc.expiratory_flow)
        self.ventilator_power_level = Warning('Ventilator Power Level',5,0,10,0,'Voltage',inc.expiratory_flow)
        self.eTv_not_achieved = Warning('eTv not achieved',4,0,sett.min_expiratory_tidal_volume,2,'%',inc.expiratory_flow)
        self.iTv_not_achieved = Warning('iTv not achieved',4,0,sett.max_inspiratory_tidal_volume,2,'%',inc.expiratory_flow)
        self.min_leak = Warning('Min Leak',4,0,0,0,'mL/min',inc.expiratory_flow)
        self.max_leak = Warning('Max Leak',4,0,50,1,'mL/min',inc.expiratory_flow)
        self.low_FiO2 = Warning('Low FiO2',4,0,0.9,0,'mL/min', inc.expiratory_flow,)
        self.high_Fi02 = Warning('High Fi02',4,0,0.3,1,'mL/min',inc.expiratory_flow)

warn = Warnings()

def init_warnings():
    global warnings_list
    warnings_list += [warn.peek_pressure_high]
    warnings_list += [warn.peek_pressure_low]
    warnings_list += [warn.PEEP_high]
    warnings_list += [warn.PEEP_low]
    warnings_list += [warn.loss_of_data_transfer]
    warnings_list += [warn.respiratory_rate_low]
    warnings_list += [warn.eTv_not_achieved]
    warnings_list += [warn.iTv_not_achieved]
    warnings_list += [warn.min_leak]
    warnings_list += [warn.max_leak]
    warnings_list += [warn.low_FiO2]
    warnings_list += [warn.high_Fi02]

# Warning Management -Know when to display warnings
def update_all_warning_status():
    global warnings_list
    for warning in warnings_list:
        comparison_type = warning.get_comparison_type()
        if comparison_type == 0:
            #need to check if less than
            if warning.get_sensor_data().get_value() < warning.get_threshold():
                warning.set_status(1)
            else:
                warning.set_status(0)
        elif comparison_type == 1:
            #needs to be less than
            if warning.get_sensor_data().get_value() > warning.get_threshold():
                warning.set_status(1)
            else:
                warning.set_status(0)
        else:
            #needs to be within 10% of threshold
            vmin = 0.9*warning.get_threshold()
            vmax = 1.1*warning.get_threshold()
            if warning.get_sensor_data().get_value() < vmin:
                warning.set_status(1)
            if warning.get_sensor_data().get_value() > vmax:
                warning.set_status(2)

def check_all_warning_status():
    for w in warnings_list:
        if w.get_status !=0:
            w.show_warning()



