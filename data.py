# This file contains classes for settings and data
# It also contains default values for both and these can be accessed within
# Use inspiratory_time.get_value() and other functions to access

#NOTE MUST CALL init_settings_and_data() before program begins
# contains data input interpretation and data output string creation

#Example Data String
data_string = '$Breathein,000.0,001.0,002.0,003.0,004.0,005.0,006.0,007.0,008.0,001.0,'

serial_in = ''
incomming_ERROR_count = 0
incoming_data_ERROR_min_threshold = 10 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_max_threshold = 20 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_flag = 0 # 0=fine, 1=some drop of signal, 2=frequent loss of signals

class Setting():
    # Initializer / Instance Attributes
    def __init__(self,name, default_value, units, max, min):
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
        self.inspiratory_flow = IncomingData('Inspiratory Flow', 'L/min')
        self.expiratory_pressure = IncomingData('Expiratory Pressure', 'cmH2O')
        self.expiratory_flow = IncomingData('Expiratory Flow', 'L/min')
        self.Fi02 = IncomingData('Fi02','%')
        self.Fe02 = IncomingData('Fe02','%')
        self.room_air_flow_rate = IncomingData('Room Air Flow Rate','L/min')
        self.O2_flow_rate = IncomingData('O2 Flow Rate','L/min')
        self.settings_recieved = IncomingData('Settings Recieved', '')


#Define Settings
settings_list = []
#Setting(Name, default_value, units, min, max)
class Settings():
    def __init__(self):
        self.ventilation_mode = Setting('Ventilation Mode',2.0,'','','')
        self.system_status = Setting('System Status',0.0,'','','')
        self.PEEP = Setting('PEEP',5.0,'cmH2O',5,12)
        self.Fi02 = Setting('Fi02',1.0,'%',0.3,0.6)
        self.min_RR = Setting('Min RR',10.0,'Breaths/min',4,14)
        self.max_RR = Setting('Max RR',25.0,'Breaths/min',12,40)
        self.IE_ratio = Setting('I:E Ratio',0.5,'Ratio','1:1.5','1:3')
        self.inspiratory_rise_time = Setting('Inspiratory Rise Time',0.2,'Seconds',0,5)
        self.inspiratory_time = Setting('Inspiratory Time',1.0,'Seconds',0.5,2)
        self.min_inspiratory_time =  Setting('Min Inspiratory Time',2.0,'Seconds',1,3)
        self.max_inspiratory_time = Setting('Max Inspiratory Time',4.0,'Seconds',0.8,3)
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

def init_settings_and_data():
    global settings_list
    global data_list
    datt = IncomingDatas()
    sett = Settings()
    settings_list+= [sett.ventilation_mode]
    settings_list+= [sett.system_status]
    settings_list+= [sett.PEEP]
    settings_list+= [sett.Fi02]
    settings_list+= [sett.min_RR]
    settings_list+= [sett.max_RR]
    settings_list+= [sett.IE_ratio]
    settings_list+= [sett.inspiratory_rise_time]
    settings_list+= [sett.inspiratory_time]
    settings_list+= [sett.min_inspiratory_time]
    settings_list+= [sett.max_inspiratory_time]
    settings_list+= [sett.max_inspiratory_pressure]
    settings_list+= [sett.tidal_volume]
    settings_list+= [sett.max_inspiratory_tidal_volume]
    settings_list+= [sett.min_inspiratory_tidal_volume]
    settings_list+= [sett.max_expiratory_tidal_volume]
    settings_list+= [sett.min_expiratory_tidal_volume]
    settings_list+= [sett.min_leak]
    settings_list+= [sett.max_leak]
    settings_list+= [sett.apnoea_time]
    settings_list+= [sett.max_pressure]

    data_list+= [datt.time]
    data_list+= [datt.inspiratory_pressure]
    data_list+= [datt.inspiratory_flow]
    data_list+= [datt.expiratory_pressure]
    data_list+= [datt.expiratory_flow]
    data_list+= [datt.Fi02]
    data_list+= [datt.Fe02]
    data_list+= [datt.room_air_flow_rate]
    data_list+= [datt.O2_flow_rate]
    data_list+= [datt.settings_recieved]

# Turn Current Settings into Output String
# Should be of the form:
# $Breatheout,002.0,000.0,005.0,001.0,010.0,025.0,000.5,000.2,001.0,002.0,004.0,015.0,600.0,800.0,300.0,800.0,300.0,000.0,050.0,010.0,040.0,
# Maximum digit length 000.0 for all settings
# String is of length 137 including initial $ #must check for this on reciept
def create_settings_string():
    output = '$Breatheout'
    for x in settings_list:
        value = str(x.get_value())
        if len(value) != 5:
            while len(value) != 5:
                value='0'+value
        output = output + ',' + value
    output = output + ','

    print(output)
    return output

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



