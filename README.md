# Monitoramento na IoT
## Atividade da Disciplina de Sistemas Operacionais II

- **Embarcado utilizado:** [ESP32](https://pt.wikipedia.org/wiki/ESP32)
- **Linguagem de Programação:** [MicroPython](https://micropython.org/)
- **Ambiente de Desenvolvimento:** [uPyCraft](http://docs.dfrobot.com/upycraft/)
- **Plataforma de Nuvem na IoT utilizada:** [GroveStreams](https://grovestreams.com)
- **Tutoriais utilizados:**
  - [MicroPython na ESP32](https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/)
  - [Upload MicroPython Firmware to ESP32](https://randomnerdtutorials.com/flash-upload-micropython-firmware-esp32-esp8266/)
  - [GroveStreams](https://grovestreams.com/developers/tutorial_temp.html)
  
### Resumo das Funcionalidades:

  - **Funcionalidades no embarcado**
    - A esp32, neste projeto, tem a função de ler os valores analógicos lidos do ambiente pelos sensores de temperatura e de luminosidade e transformando-los em valores digitais para que possamos em nosso projeto.

  - **Funcionalidades na Plataforma de Nuvem na IoT**
    - Nossa plataforma receberá dados enviados por nossa ESP32 e nos fornecerá gráficos com as variações sofridas pelos nossos sensores.

  ### Projeto
   Abaixo está listado os materias necessários para a execução desse projeto.
   
  - **Materiais**
   
    - Softwares:
      - Cloud IoT: GroveStreams
      - IDE: uPyCraft

    - Hardware:
      - Esp32
      - LDR (sensor de luminosidade)
      - LM35 (sensor de temperatura)
      - Protoboard
      - Cabo de alimentação
      - Resistor de 3,3K
      - fios jumper (usei 4 fios)
  
   ### uPyCraft 
   ### Hardware
   ### GroveStreams 
   ### Montagem da protoboard 
   ### Código
