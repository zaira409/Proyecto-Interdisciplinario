#define led1 7
#define led2 6

void setup()
{
pinMode(led1, OUTPUT);
pinMode(led2, OUTPUT);
Serial.begin(9600);
}

void loop()
{
  
  Serial. println(" la secuencia ha comenzado.");
  delay(1000);
  digitalWrite(led1, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  analogWrite(led2, 120);
  delay(1000); // Wait for 1000 millisecond(s)
  analogWrite(led2, 40);
  delay(1000);
  Serial.println("la nave esta en orbita.");
  analogWrite(led2, 0);
  digitalWrite(led1, LOW);
  delay(1000);
  
}