#include <LedControl.h>

// Pin configuración para MAX7219
const int DIN_PIN = 2;  // Conectar a DIN del MAX7219
const int CS_PIN = 3;   // Conectar a CS del MAX7219
const int CLK_PIN = 4;  // Conectar a CLK del MAX7219
bool matriz[8][8];

int row_index = 0;
int col_index = 0;
bool flag = false;
LedControl lc = LedControl(DIN_PIN, CLK_PIN, CS_PIN, 1); // Parámetros: (DIN, CLK, CS, número de MAX7219)

void setup() {
  lc.shutdown(0, false);  // Iniciar el MAX7219 (SHUTDOWN register)
  lc.setIntensity(0, 8);  // Establecer la intensidad del brillo (0-15)
  lc.clearDisplay(0);     // Borrar la matriz
  zero();
  Serial.begin(9600);
  Serial.print("R\n");
}

void loop() {
  if(flag){
    flag = false;
    Serial.print("R\n");
  }
  actualizar();
}


void zero() {
  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 8; col++) {
      matriz[row][col] = LOW; // Encender un LED en la posición (row, col)
    }
  }
}

void actualizar() {
  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 8; col++) {
      lc.setLed(0, row, col, matriz[row][col]);  // Encender un LED en la posición (row, col)
    }
  }
}

void serialEvent() {
  // Esta función se ejecutará automáticamente cuando lleguen datos al puerto serie
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '1'){
      matriz[row_index][col_index]= HIGH;
      col_index++;
    }
    else if(c == '0'){
      matriz[row_index][col_index]= LOW;
      col_index++;
    }
    else if(c == ';'){
      row_index++;
      col_index = 0;
    }
    else if (c = '\n'){
      flag = true;
      col_index = 0;
      row_index = 0;
    }
  }
}
