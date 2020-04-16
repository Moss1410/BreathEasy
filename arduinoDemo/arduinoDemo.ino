int potX = A0;
int potXVal = 0;
unsigned long time;

void setup() {
  Serial.begin(9600);
  pinMode(potX, INPUT);
}

void loop() {
  potXVal = analogRead(potX);
  time = millis();
  Serial.print(time);
  Serial.print(",");
  Serial.println(potXVal);
}
