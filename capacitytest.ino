#include<Servo.h>
Servo motorX;
Servo motorY;
int aci;
 
void setup() {
 motorX.attach(10);
 motorY.attach(11);
}
 
void loop() {
 
for(aci=0;aci<=180;aci+=1){
motorX.write(aci);
motorY.write(aci);
delay(5);
}
for(aci=180;aci>=0;aci-=1){
motorX.write(aci);
motorY.write(aci);
delay(5);
}
 
}
