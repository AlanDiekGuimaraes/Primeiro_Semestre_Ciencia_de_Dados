#define leds 4
#define botao 15

int grupo1[leds] = {2, 0, 16, 5};
int grupo2[leds] = {19, 21, 22, 23};

void setup() {
  for(int i = 0; i < leds; i++){
    pinMode(grupo1[i], OUTPUT);
    pinMode(grupo2[i], OUTPUT);
  }
  pinMode(botao, INPUT_PULLUP);
}

void loop() {
while (digitalRead(botao) == HIGH){
  for(int i = 0; i < leds; i++){
    digitalWrite(grupo1[i], HIGH);
    digitalWrite(grupo2[leds - 1 - i], HIGH);
    delay(250);
     digitalWrite(grupo1[i], LOW);
    digitalWrite(grupo2[leds - 1 - i], LOW);
  }
}
for(int i = 0; i < leds; i++){
    digitalWrite(grupo1[i], HIGH);
    digitalWrite(grupo2[i], HIGH);
    delay(250);
     digitalWrite(grupo1[i], LOW);
    digitalWrite(grupo2[i], LOW);
  }
}
