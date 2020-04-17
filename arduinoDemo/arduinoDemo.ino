int potX = A0;

char identifier = "$Breathein";
unsigned long dataTime;
int inspPres = 0;
int inspFlow = 0;
int expPres = 0;
int expFlow = 0;
int inspOxy = 0;
int expOxy = 0;
int roomAirFlow = 0;
int room02Flow = 0;
int comStatus = 0;
int mode = 1;

void setup() {
  Serial.begin(9600);
  pinMode(potX, INPUT);
}

void loop() {
  if (mode==0){
    inspPres = (analogRead(potX)-500)/12;
    dataTime = millis();
    Serial.print("$Breathein");
    Serial.print(",");
    Serial.print(dataTime);
    Serial.print(",");
    Serial.print(inspPres);
    Serial.print(",");
    Serial.print(inspFlow);
    Serial.print(",");
    Serial.print(expPres);
    Serial.print(",");
    Serial.print(expFlow);
    Serial.print(",");
    Serial.print(inspOxy);
    Serial.print(",");
    Serial.print(expOxy);
    Serial.print(",");
    Serial.print(roomAirFlow);
    Serial.print(",");
    Serial.print(room02Flow);
    Serial.print(",");
    Serial.println(comStatus);
    mode=1;
  } else if (mode==1){
      dataTime = millis();
      char data = Serial.read();
      char str[2];
      str[0] = data;
      str[1] = '\0';
      Serial.println(dataTime);
      mode=0;
  }
}
