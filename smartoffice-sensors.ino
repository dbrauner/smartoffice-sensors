#define BRIGTHNESS_MAX 1000
#define BRIGHTNESS_MIN 0
#define BRIGHTNESS_GOOD 350

//Função setup, executado uma vez ao ligar o Arduino.
void setup(){
  //Ativando o serial monitor que exibirá os valores lidos no sensor.
  Serial.begin(9600);
}

//Função loop, executado enquanto o Arduino estiver ligado.
void loop(){
char newLine [100];

sprintf(newLine, "%i|%i|%i", lightSensor(), soundSensor(), distanceSensor());

Serial.println(newLine);

delay(1500);
} 

int lightSensor(){
  //Lendo o valor do sensor.
  int valorSensor = analogRead(A0);

  return valorSensor;
}

int distanceSensor(){
  //Lendo o valor do sensor.
  int distance = analogRead(A2);

  return distance;
}

int soundSensor(){
  int volume;
  volume = analogRead(A3); // Reads the value from the Analog PIN A3

  return volume;
}
