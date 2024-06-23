const int ledPins[] = {0, 2, 4, 5, 19, 16, 17, 18};
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);
const int espera = 500;

void setup() {
  for (int contador = 0; contador < numLeds; contador++){
     pinMode(ledPins[contador], OUTPUT);
  }
 
 
  for (int contador = 0; contador < numLeds; contador++){
    
    digitalWrite(ledPins[contador], HIGH);
    delay(espera);
    if (contador > 3){
      if (contador == 7){
        digitalWrite(ledPins[contador], HIGH);
        delay(espera);
        for(int i = 0; i < 4; i++){
           digitalWrite(ledPins[i], LOW);
        }
        break;
      } 
      digitalWrite(ledPins[contador], HIGH);
      delay(espera);
      digitalWrite(ledPins[contador], LOW);
      
    }
   
  }
 
}

void loop() {
    

}

