const int pResistor   =  A1;
const int buzzer      =  10;
int value;
unsigned long time_now = 0;
int delay_period = 1000;


void setup() {
 Serial.begin(9600);      // open the serial port at 9600 bps:
 pinMode(pResistor,INPUT);
 pinMode(buzzer, OUTPUT);
}

void loop() {  
 value = analogRead(pResistor);
 time_now = millis();
 Serial.println(value);

 if (value < 1000) {
   while(millis() < time_now + delay_period){
     tone(buzzer, 1000);
     Serial.println("ALARM");
   }
   
   
   
 }
 else{
   noTone(buzzer);
 }
}