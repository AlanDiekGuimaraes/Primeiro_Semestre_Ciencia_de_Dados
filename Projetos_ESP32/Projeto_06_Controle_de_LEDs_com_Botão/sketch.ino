#define qtd_led 5
#define botao 15
#define led_vermelho 2

int pinos_leds[qtd_led] = {0, 16, 5, 19, 21};

void setup() {
  for (int i = 0; i < qtd_led; i++){
   pinMode(pinos_leds[i], OUTPUT);
  }
  pinMode(led_vermelho, OUTPUT);
  pinMode(botao, INPUT_PULLUP);
}

void loop() {
while (digitalRead(botao) == LOW){
  digitalWrite(led_vermelho, HIGH);
  digitalWrite(led_vermelho, LOW); 
  //enquanto não aperta o botão nada acontece.
}  
for (int i = 0; i < qtd_led; i++){
  digitalWrite(pinos_leds[i], HIGH);
  delay(500);
  digitalWrite(pinos_leds[i], LOW);
  }
}
  
