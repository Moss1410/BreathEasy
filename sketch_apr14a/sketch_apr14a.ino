int potX = A0;
int potXVal = 0;


void setup() {
  Serial.begin(9600);
  pinMode(potX, INPUT);
}

void loop() {
  potXVal = analogRead(potX);
  Serial.println(potXVal);
}
