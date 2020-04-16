# Required Settings to Send with Defaults
settings_dict = {}

serial_in = ''
incomming_ERROR_count = 0
incoming_data_ERROR_min_threshold = 10 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_max_threshold = 20 # number of incorrect data streams in a row allowed before triggering warning
incoming_data_ERROR_flag = 0 # 0=fine, 1=some drop of signal, 2=frequent loss of signals

incoming_data = {
    'time':(0.0,'Seconds'),
    'inspiratory_pressure':(0.0,'cmH2O'),
    'inspiratory_flow':(0.0,'L/min'),
    'expiratory_pressure':(0.0,'cmH2O'),
    'expiratory_flow':(0.0,'L/min'),
    'Fi02':(0.0,'%'),
    'Fe02':(0.0,'%'),
    'room_air_flow_rate':(0.0,'L/min'),    
    '02_flow_rate':(0.0,'L/min'),
    'settings_recieved':(1.0,'')       
}

#Example Data String
data_string = '$Breathein,000.0,001.0,002.0,003.0,004.0,005.0,006.0,007.0,008.0,001.0,'

# Probably should make this list from the dictionary itself
key_list = ['time','inspiratory_pressure','inspiratory_flow','expiratory_pressure',
    'expiratory_flow','Fi02','Fe02','room_air_flow_rate','02_flow_rate', 'settings_recieved']

def make_setttings_default():
    global settings_dict
    settings_dict = {
        'ventilation_mode' : (2.0,'',('','')), #of the form: (value, units, (min,max))
        'system_status' : (0.0,'',('','')),
        'PEEP' : (5.0,'cmH2O',(5,12)),
        'Fi02' : (1.0,'%',(0.3,0.6)),
        'min_RR' : (10.0,'Breaths/min',(4,14)),
        'max_RR' : (25.0,'Breaths/min',(12,40)),
        'IE_ratio' : (0.5,'Ratio',('1:1.5','1:3')),
        'inspiratory_rise_time' : (0.2,'Seconds',(0,5)), # these hashtags mean the default wasnt specified
        'inspiratory_time' : (1.0,'Seconds',(0.5,2)), #
        'min_inspiratory_time' : (2.0,'Seconds',(1,3)),
        'max_inspiratory_time' : (4.0,'Seconds',(0.8,3)),
        'max_inspiratory_pressure' : (15.0,'cmH20',(10,20)),
        'tidal_volume' : (600.0,'mL',(200,800)), #
        'max_inspiratory_tidal_volume' : (800.0,'mL',(30,2000)),
        'min_inspiratory_tidal_volume' : (300.0,'mL',(80,3000)),
        'max_expiratory_tidal_volume' : (800.0,'mL',(30,2000)),
        'min_expiratory_tidal_volume' : (300.0,'mL',(80,3000)),
        'min_leak' : (0.0,'mL/min',(0,20)),
        'max_leak' : (50.0,'mL/min',(10,100)),
        'apnoea_time' : (10.0,'Seconds',(8,20)),
        'max_pressure' : (40.0,'cmH2O',(30,45))
    }

# Turn Current Settings into Output String
# Should be of the form:
# $Breatheout,002.0,000.0,005.0,001.0,010.0,025.0,000.5,000.2,001.0,002.0,004.0,015.0,600.0,800.0,300.0,800.0,300.0,000.0,050.0,010.0,040.0,
# Maximum digit length 000.0 for all settings
# String is of length 137 including initial $ #must check for this on reciept
def create_settings_string():
    output = '$Breatheout'
    for x in settings_dict:
        value = str(settings_dict[x][0])
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
        #Strip off the extra zeros at the beginning
        while x[0] == 0 & len(x)>3:
            x=x[1:]
        #find the units from the dictionary
        units = incoming_data[key_list[i]][1]
        incoming_data.update({key_list[i]:(float(x),units)})
        i+=1
    print(incoming_data)
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


#if __name__ == "__main__":
    #make_setttings_default()
    #create_settings_string()
    #interpret_input()