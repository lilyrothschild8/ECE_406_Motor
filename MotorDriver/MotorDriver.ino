//Emmanuel Quaye
//RPI 4B
//This code drives the NEMA 17 motor stepper motor using the TB6600 Driver
//5 -> to the controller "+" input for each: ENA, PUL+, and DIR+
//ARDUINO VERSION
//
int PUL = 8;  // Stepper Drive Pulses
int DIR = 9;  // Controller Direction port (High for Controller default / LOW to Force a Direction Change).
int Enable = 10;  // The enable port
int rotation = 0;// rotations completed
int dTT = 0; // the distance to travel
// NOTE: if you leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.

//
void setup() {
Serial.begin(9600);
pinMode(PUL, OUTPUT);
pinMode(DIR, OUTPUT);
pinMode(Enable, OUTPUT);  


Serial.println("PUL = Pin 2 ");
Serial.println("DIR = Pin 3 ");
Serial.println("Enable = Pin 4 ");
Serial.println("Ready");

digitalWrite(Enable, LOW); //for enable LOW == Enabled, HIGH = disabled.
Serial.println("Enable set to LOW - Controller Enabled");
}

void loop() {
//The Distance per revolution = 200 steps/rev you can look on the mototr driver to verify.
//we know that the diameter of the 16 tooth belt pulley is 0.200" the radious is then .100"/10 = 0.01"
//with (200 * 12)/0.01 = 240000 steps/ft or 20000 steps/inch
//due to calculations Max spped = 10, Min speed = 600 dont use anything slower for better stability

forward(10,60000);
//reverse(100,40000);
}

void forward(int speed, int distance)
{
  rotation++; //increment the rotation integer.
  dTT = distance;//distance to travel;
  
  digitalWrite(DIR, HIGH); //set rotation clock-wise
  
  //use simple PWM to drive motor by enabeling disabling PUL pin at speed
  digitalWrite(PUL, HIGH); 
  digitalWrite(PUL, LOW);
  delayMicroseconds(speed); // This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
  
  //check if the distance was traveled.
  if((rotation) == dTT)
  {
    stopMotor(); //stop the motor
    //delay(1); //delay 1milisecond for stability
    rotation = dTT = 0;
  }
}

void reverse(int speed, int distance)
{
  rotation++; //increment the rotation integer.
  dTT = distance;//distance to travel;
  
  digitalWrite(DIR, LOW); //set rotation counter clock-wise
  
  //use simple PWM to drive motor by enabeling disabling PUL pin at speed
  digitalWrite(PUL, HIGH); 
  digitalWrite(PUL, LOW);
  delayMicroseconds(speed); // This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
  
  //check if the distance was traveled.
  if((rotation) == dTT)
  {
    stopMotor(); //stop the motor
    delay(1); //delay 1milisecond for stability
  }
}

void stopMotor()
{
  digitalWrite(Enable, HIGH); // Disable Motor
  rotation = dTT = 0;// reset the rotation.
  Serial.println("Enable set to LOW - Controller Disabled");
}
