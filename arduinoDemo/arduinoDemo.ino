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

void setup() {
  Serial.begin(9600);
  pinMode(potX, INPUT);
}

void loop() {
  inspPres = analogRead(potX);
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
}
