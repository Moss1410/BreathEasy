# This file contains classes for settings and data
# It also contains default values for both and these can be accessed within
# Use inspiratory_time.get_value() and other functions to access

#NOTE MUST CALL init_settings_and_data() before program begins
# contains data input interpretation and data output string creation

from kivy.properties import StringProperty

#Example Data String
data_string = '$Breathein,000.0,001.0,002.0,003.0,004.0,005.0,006.0,007.0,008.0,001.0,'

serial_in = ''
incomming_ERROR_count = 0
incoming_data_ERROR_min_threshold = 10 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_max_threshold = 20 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_flag = 0 # 0=fine, 1=some drop of signal, 2=frequent loss of signals

class Setting():
    # Initializer / Instance Attributes
    def __init__(self,name, default_value, units, min, max):
        self.name = name
        self.value = default_value
        self.units = units
        self.max = max
        self.min = min
        self.data = []

    def __repr__(self):
        return self.name

    # instance method
    def set_value(self, new_value):
        if (new_value > self.max):
            new_value = self.max
        elif (new_value < self.min):
            new_value =  self.min
        self.value = new_value

    def get_value(self):
        return self.value

    def get_units(self):
        return self.units


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


data_list = []
#Data(name,units)

class IncomingDatas():
    def __init__(self):
        self.time = IncomingData('Time','Seconds')
        self.inspiratory_pressure = IncomingData('Inspiratory Pressure', 'cmH2O')
        self.peak_inspiratory_pressure = IncomingData('Peak Inspiratory Pressure', 'cmH2O')
        self.peak_inspiratory_pressure.set_value(30)
        self.inspiratory_flow = IncomingData('Inspiratory Flow', 'L/min')
        self.expiratory_pressure = IncomingData('Expiratory Pressure', 'cmH2O')
        self.expiratory_flow = IncomingData('Expiratory Flow', 'L/min')
        self.PEEP = IncomingData('PEEP', 'cmH2O')
        self.PEEP.set_value(5)
        self.respiratory_rate = IncomingData('Respiratory Rate', 'Breaths/min')
        self.respiratory_rate.set_value(10)
        self.voltage = IncomingData("Voltage", "V")
        self.voltage.set_value(24)
        self.tidal_volume = IncomingData("Tidal Volume", "mL")
        self.Fi02 = IncomingData('Fi02','%')
        self.Fi02.set_value(1)
        self.Fe02 = IncomingData('Fe02','%')
        self.settings_recieved = IncomingData('Settings Recieved', '')


#Define Settings
settings_list = []
#Setting(Name, default_value, units, min, max)
class Settings():
    def __init__(self):
        self.ventilation_mode = Setting('Ventilation Mode',2.0,'',0,2)
        self.system_status = Setting('System Status',0.0,'',0,1)
        
        self.PEEP = Setting('PEEP',5.0,'cmH2O',5,12)
        self.FiO2 = Setting('FiO2',1.0,'%',0.3,1)
        self.min_RR = Setting('Min RR',10.0,'Breaths/min',4,14)
        self.max_RR = Setting('Max RR',25.0,'Breaths/min',12,40)
        self.IE_ratio = Setting('I:E Ratio',0.5,'Ratio',0,1)
        
        self.inspiratory_rise_time = Setting('Inspiratory Rise Time',0.2,'Seconds',0,5)
        self.inspiratory_time = Setting('Inspiratory Time',1.0,'Seconds',0.5,2)
        self.min_inspiratory_time =  Setting('Min Inspiratory Time',2.0,'Seconds',1,3)
        self.max_inspiratory_time = Setting('Max Inspiratory Time',2,'Seconds',0.8,3)
        self.max_inspiratory_pressure = Setting('Max Inspiratory Pressure',15.0,'cmH20',10,20)
        
        self.tidal_volume = Setting('Tidal Volume',600.0,'mL',200,800)
        self.max_inspiratory_tidal_volume = Setting('Max Inspiratory Tidal Volume',800.0,'mL',30,2000)
        self.min_inspiratory_tidal_volume = Setting('Min Inspiratory Tidal Volume',300.0,'mL',80,3000)
        self.max_expiratory_tidal_volume = Setting('Max Expiratory Tidal Volume',800.0,'mL',30,2000)
        self.min_expiratory_tidal_volume = Setting('Min Expriatory Tidal Volume',300.0,'mL',80,3000)
        
        self.min_leak = Setting('Min Leak',0.0,'mL/min',0,20)
        self.max_leak = Setting('Max Leak',50.0,'mL/min',10,100)
        self.apnoea_time = Setting('Apnoea Time',10.0,'Seconds',8,20)
        self.max_pressure = Setting('Max Pressure',40.0,'cmH2O',30,45)

    def create_settings_string(self):
        settings_list = self.get_settings()
        output = '$Breatheout'
        for x in settings_list:
            value = str(x.get_value())
            if len(value) != 5:
                while len(value) != 5:
                    value='0'+value
            output = output + ',' + value
        output = output + ','
        return output

    def get_settings(self):
        settings_list = []
        settings_list+= [self.ventilation_mode]
        settings_list+= [self.system_status]
        settings_list+= [self.PEEP]
        settings_list+= [self.FiO2]
        settings_list+= [self.min_RR]
        settings_list+= [self.max_RR]
        settings_list+= [self.IE_ratio]
        settings_list+= [self.inspiratory_rise_time]
        settings_list+= [self.inspiratory_time]
        settings_list+= [self.min_inspiratory_time]
        settings_list+= [self.max_inspiratory_time]
        settings_list+= [self.max_inspiratory_pressure]
        settings_list+= [self.tidal_volume]
        settings_list+= [self.max_inspiratory_tidal_volume]
        settings_list+= [self.min_inspiratory_tidal_volume]
        settings_list+= [self.max_expiratory_tidal_volume]
        settings_list+= [self.min_expiratory_tidal_volume]
        settings_list+= [self.min_leak]
        settings_list+= [self.max_leak]
        settings_list+= [self.apnoea_time]
        settings_list+= [self.max_pressure]
        return settings_list

# Turn Current Settings into Output String
# Should be of the form:
# $Breatheout,002.0,000.0,005.0,001.0,010.0,025.0,000.5,000.2,001.0,002.0,004.0,015.0,600.0,800.0,300.0,800.0,300.0,000.0,050.0,010.0,040.0,
# Maximum digit length 000.0 for all settings
# String is of length 137 including initial $ #must check for this on reciept


# Intake Serial Data
# Something similar will have to be done in Arduino/C for interpretting the user settings
# Example expected string $Breathein,000.0,001.0,002.0,003.0,14.0,005.0,006.0,007.0,008.0,001.0,
# Length must be 71
def interpret_input():
    # data string is ready for processing
    lst = data_string.split(',')
    lst=lst[1:len(lst)-1]
    i=0
    for x in lst:
        data_list[i].set_value(float(x))
        i+=1
    return

# WORK OUT HOW TO CHECK IF DATA HAS BEEN LOST- PROBS NEED EXPECTED LENGTH, MEANS MIGHT NEED TO PAD VALUES TO THEIR MAX SIZE
# Storage of comlete data strings - then to be used for updates
def serial_storing():
    global data_string
    global incomming_ERROR_count
    global incoming_data_ERROR_flag
    if serial_in == '$':
        data_string = ''
        if len(data_string) != 71:
            incomming_ERROR_count+=1
            # Signal qualilty is very poor
            if incomming_ERROR_count >= incoming_data_ERROR_max_threshold:
                #Maybe throw exceptoin????
                incoming_data_ERROR_flag = 2
            # Signal quality is reasonable but losses are being seen
            elif incomming_ERROR_count >= incoming_data_ERROR_min_threshold:
                #Maybe throw exceptoin????
                incoming_data_ERROR_flag = 1
            else:
                incoming_data_ERROR_flag = 0
        else:
            interpret_input()
            # reduce error count - min zero
            incomming_ERROR_count-=1
            if incomming_ERROR_count < incoming_data_ERROR_min_threshold:
                incoming_data_ERROR_flag = 0
    else:
        data_string += serial_in



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


class Warnings():
    def __init__(self, inc, sett):
        self.peek_pressure_high = Warning('Peak Pressure High', 4,0,40,1,'cmH20',inc.peak_inspiratory_pressure)
        self.peek_pressure_low = Warning('Peak Pressure Low',4,0,10,0,'cmH20',inc.peak_inspiratory_pressure)
        self.PEEP_high = Warning('PEEP High',4,0,10,1,'cmH20',inc.PEEP)
        self.PEEP_low = Warning('PEEP Low',4,0,5,0,'cmH20',inc.PEEP)
        #self.loss_of_data_transfer = Warning('PEEP High',4,0,10,1,'cmH20',inc.expiratory_flow)
        self.respiratory_rate_low = Warning('Respiratory Rate Low',4,0,sett.min_RR.get_value(),0,'Breaths/min',inc.respiratory_rate)
        self.ventilator_power_level = Warning('Ventilator Power Level',5,0,24,2,'Voltage',inc.voltage)
        #self.Tv_not_achieved = Warning('Tidal volume not achieved',4,0,300,0,'%',inc.tidal_volume)
        #self.iTv_not_achieved = Warning('iTv not achieved',4,0,sett.max_inspiratory_tidal_volume,2,'%',inc.expiratory_flow)
        self.min_leak = Warning('Min Leak',4,0,-50,0,'mL/min',inc.inspiratory_flow)
        self.max_leak = Warning('Max Leak',4,0,50,1,'mL/min',inc.inspiratory_flow)
        self.low_FiO2 = Warning('Low FiO2',4,0,0.3,0,'mL/min', inc.Fi02)
        #self.high_Fi02 = Warning('High Fi02',4,0,0.9,1,'mL/min',inc.Fi02)
    
    # Warning Management -Know when to display warnings
    def update_all_warning_status(self):
        warnings_list = self.get_warnings()
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
                    warning.set_status(1)

    def get_warnings(self):
        warnings_list = []
        warnings_list += [self.peek_pressure_high]
        warnings_list += [self.peek_pressure_low]
        warnings_list += [self.PEEP_high]
        warnings_list += [self.PEEP_low]
        #warnings_list += [self.loss_of_data_transfer]
        warnings_list += [self.respiratory_rate_low]
        #warnings_list += [self.Tv_not_achieved]
        #warnings_list += [self.iTv_not_achieved]
        warnings_list += [self.min_leak]
        warnings_list += [self.max_leak]
        warnings_list += [self.low_FiO2]
        #warnings_list += [self.high_Fi02]
        return warnings_list