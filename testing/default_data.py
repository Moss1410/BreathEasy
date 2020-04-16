import dataClasses
import incomingData
import warnings

#Data(name,units)
time = IncomingData('Time','Seconds')
inspiratory_pressure = dataClasses.IncomingData('Inspiratory Pressure', 'cmH2O')
inspiratory_flow = dataClasses.IncomingData('Inspiratory Flow', 'L/min')
expiratory_pressure = dataClasses.IncomingData('Expiratory Pressure', 'cmH2O')
expiratory_flow = dataClasses.IncomingData('Expiratory Flow', 'L/min')
Fi02 = dataClasses.IncomingData('Fi02','%')
Fe02 = dataClasses.IncomingData('Fe02','%')
room_air_flow_rate = dataClasses.IncomingData('Room Air Flow Rate','L/min')
O2_flow_rate = dataClasses.IncomingData('O2 Flow Rate','L/min')
settings_recieved = dataClasses.IncomingData('Settings Recieved', '')

#Define Settings
#Setting(Name, default_value, units, min, max)
ventilation_mode = dataClasses.Setting('Ventilation Mode',2.0,'','','')
system_status = dataClasses.Setting('System Status',0.0,'','','')
PEEP = dataClasses.Setting('PEEP',5.0,'cmH2O',5,12)
Fi02 = dataClasses.Setting('Fi02',1.0,'%',0.3,0.6)
min_RR = dataClasses.Setting('Min RR',10.0,'Breaths/min',4,14)
max_RR = dataClasses.Setting('Max RR',25.0,'Breaths/min',12,40)
IE_ratio = dataClasses.Setting('I:E Ratio',0.5,'Ratio','1:1.5','1:3')
inspiratory_rise_time = dataClasses.Setting('Inspiratory Rise Time',0.2,'Seconds',0,5)
inspiratory_time = dataClasses.Setting('Inspiratory Time',1.0,'Seconds',0.5,2)
min_inspiratory_time =  dataClasses.Setting('Min Inspiratory Time',2.0,'Seconds',1,3)
max_inspiratory_time = dataClasses.Setting('Max Inspiratory Time',4.0,'Seconds',0.8,3)
max_inspiratory_pressure = dataClasses.Setting('Max Inspiratory Pressure',15.0,'cmH20',10,20)
tidal_volume = dataClasses.Setting('Tidal Volume',600.0,'mL',200,800)
max_inspiratory_tidal_volume = dataClasses.Setting('Max Inspiratory Tidal Volume',800.0,'mL',30,2000)
min_inspiratory_tidal_volume = dataClasses.Setting('Min Inspiratory Tidal Volume',300.0,'mL',80,3000)
max_expiratory_tidal_volume = dataClasses.Setting('Max Expiratory Tidal Volume',800.0,'mL',30,2000)
min_expiratory_tidal_volume = dataClasses.Setting('Min Expriatory Tidal Volume',300.0,'mL',80,3000)
min_leak = dataClasses.Setting('Min Leak',0.0,'mL/min',0,20)
max_leak = dataClasses.Setting('Max Leak',50.0,'mL/min',10,100)
apnoea_time = dataClasses.Setting('Apnoea Time',10.0,'Seconds',8,20)
max_pressure = dataClasses.Setting('Max Pressure',40.0,'cmH2O',30,45)
