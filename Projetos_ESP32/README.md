# ESP32
Introdução a linguagem C++ com ESP32.

# PROJETO 01 - ESP32 - LED Piscar 5 Vezes

Descrição

Este projeto faz com que um LED conectado a um ESP32 pisque 5 vezes e depois permaneça desligado. Foi desenvolvido em C++ usando o Arduino IDE.

Funcionamento

O código acende e apaga o LED com um intervalo de 500 milissegundos, repetindo esse ciclo 5 vezes. Após isso, o LED permanece desligado.

# PROJETO 02 - ESP32 - LED Sequencial

Descrição

Este projeto foi desenvolvido em C++ e faz com que três LEDs conectados ao ESP32 pisquem de forma sequencial. Cada LED acende e apaga em intervalos de 500 milissegundos.

Funcionamento

Os LEDs estão conectados aos pinos 2, 4 e 5 do ESP32.
Os LEDs acendem e apagam de forma sequencial com um intervalo de 500 milissegundos.
O processo de acender e apagar continua indefinidamente.

# PROJETO 03 - ESP32 - Pisca LED Aleatório

Descrição

Este projeto em C++ utiliza um ESP32 para fazer com que LEDs, conectados a diferentes pinos, pisquem de forma aleatória. A cada iteração do loop, um LED é escolhido aleatoriamente para acender e apagar após um intervalo fixo.

Funcionamento

Os LEDs estão conectados aos pinos 2, 4 e 5 do ESP32.
A cada ciclo do loop, um LED é escolhido aleatoriamente para acender.
O LED escolhido acende por um intervalo de 500 milissegundos (espera), depois apaga por mais 500 milissegundos antes de outro LED ser escolhido.


# PROJETO 04 - ESP32 - Semaforo Dragster

Descrição

Este projeto utiliza um microcontrolador ESP32 para controlar uma sequência de LEDs, onde alguns LEDs permanecem acesos enquanto outros piscam. A sequência é controlada por um código que define diferentes comportamentos para os LEDs com base em suas posições.

Funcionamento

Configuração dos Pinos: No setup, cada pino correspondente a um LED é configurado como saída.

Sequência Inicial: Uma sequência inicial acende cada LED em ordem com um atraso de 500ms entre eles. Após o quarto LED, os LEDs seguintes piscam antes de prosseguir na sequência.

Comportamento Especial: Quando o sétimo LED (pino 18) é aceso, todos os LEDs anteriores são apagados.

# PROJETO 05 - ESP32 - Controle de LED com Botão

Descrição

Este projeto utiliza um microcontrolador ESP32 para controlar um LED através de um botão. Quando o botão é pressionado, o LED acende; ao soltar o botão, o LED apaga.

Funcionamento

Configuração dos Pinos: No setup, o pino 21 é configurado como saída para controlar o LED e o pino 0 é configurado como entrada com resistor de pull-up interno para ler o estado do botão.

Loop Principal: No loop principal, o estado do botão é continuamente lido. Se o botão estiver pressionado (estado LOW), o LED acende. Caso contrário, o LED permanece apagado.

# PROJETO 06 - ESP32 - Controle de LEDs com Botão

Descrição

Este projeto utiliza um microcontrolador ESP32 para controlar uma série de LEDs, com um LED vermelho adicional que é acionado por um botão. Os LEDs piscam em sequência quando o botão é pressionado.

Funcionamento

Configuração dos Pinos: No setup, cada pino correspondente a um LED e o pino do botão são configurados como saída e entrada, respectivamente.

Interação com o Botão: No loop principal, o código aguarda até que o botão seja pressionado. Quando o botão é pressionado, o LED vermelho pisca.

Sequência de LEDs: Após o botão ser pressionado, os 5 LEDs piscam em sequência com um atraso de 500ms entre eles.

# PROJETO 07 e 08 - ESP32 - Controle de LEDs com Botão (WHILE e FOR)

Descrição

Este projeto utiliza um ESP32 para controlar dois grupos de LEDs. Através de um botão, os LEDs acendem e apagam em sequência, criando um efeito visual dinâmico.

Funcionamento

Quando o botão é pressionado (digitalRead(botao) == HIGH), os LEDs dos dois grupos acendem e apagam em sequência, criando um efeito de corrida.
Após a liberação do botão, todos os LEDs de ambos os grupos acendem e apagam simultaneamente em intervalos de 250ms.

