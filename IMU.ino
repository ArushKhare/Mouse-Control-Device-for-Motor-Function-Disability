#include <Wire.h>
#include <LSM6.h>

LSM6 imu;

const int iterations = 35;
// YAW
long lastYAW[iterations];
long indexYAW=0;
long sumYAW = 0;
long avgYAW = 0;

// PITCH
long lastPITCH[iterations];
long indexPITCH=0;
long sumPITCH = 0;
long avgPITCH = 0;

// ROLL
long lastROLL[iterations];
long indexROLL=0;
long sumROLL = 0;
long avgROLL = 0;

void setup() {

  Serial.begin(9600);
  Wire.begin();
  
  if (!imu.init())
  {
    Serial.println("Failed to detect and initialize LSM6 IMU!");
    while (1);
  }
  imu.enableDefault();
}

void loop() {
  
  imu.read();
  
  long yaw = imu.a.z;
  long pitch = imu.a.y;
  long roll = imu.a.x;
  
  // YAW Axis
  if (indexYAW < iterations){
    lastYAW[indexYAW] = yaw;
    sumYAW += yaw;
    indexYAW += 1;
  }
  else{
    sumYAW -= lastYAW[0];
    for (int i=1; i<iterations; i++){
      lastYAW[i-1] = lastYAW[i];
    }
    sumYAW += yaw;
    lastYAW[iterations-1] = yaw;
  }
  avgYAW = long(sumYAW / indexYAW);

  // PITCH Axis
  if (indexPITCH < iterations){
    lastPITCH[indexPITCH] = pitch;
    sumPITCH += pitch;
    indexPITCH += 1;
  }
  else{
    sumPITCH -= lastPITCH[0];
    for (int i=1; i<iterations; i++){
      lastPITCH[i-1] = lastPITCH[i];
    }
    sumPITCH += pitch;
    lastPITCH[iterations-1] = pitch;
  }
  avgPITCH = long(sumPITCH / indexPITCH);

  // ROLL Axis
  if (indexROLL < iterations){
    lastROLL[indexROLL] = roll;
    sumROLL += roll;
    indexROLL += 1;
  }
  else{
    sumROLL -= lastROLL[0];
    for (int i=1; i<iterations; i++){
      lastROLL[i-1] = lastROLL[i];
    }
    sumROLL += roll;
    lastROLL[iterations-1] = roll;
  }
  avgROLL = long(sumROLL / indexROLL);

  Serial.print(avgPITCH);
  Serial.print(" ");
  Serial.println(avgROLL);
  //Serial.print(" ");
  //Serial.println(avgYAW);
}
