#include <MD_MAX72xx.h>
 
#define HARDWARE_TYPE MD_MAX72XX::DR0CR0RR1_HW
#define NUM_OF_MATRIX 1
 
#define CLK_PIN   4
#define DATA_PIN  2
#define CS_PIN    3
 
String tokens[8]; // Array para almacenar los tokens separados
byte arrays[8][8]; // Arrays de 8 elementos para guardar los byte

String inputString = "";
 
MD_MAX72XX mx = MD_MAX72XX(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, NUM_OF_MATRIX);
 
 
void setup() {
  Serial.begin(9600);
  // inicializar el objeto mx
  mx.begin();
 
 
  // Establecer intencidad a un valor de 5
  mx.control(MD_MAX72XX::INTENSITY, 5);
  
 
}
 

 

void misc(byte arrays[8][8]){
  // limpiar la matriz
  mx.clear();

  for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 8; col++) {
      
      mx.setPoint(col, row, arrays[row][col]);
    }
    
  }
  
 
  
}
 
void loop() {
 bool flag = 1;
  while (flag){
    while (Serial.available()) {
    char c = Serial.read(); // Lee el siguiente carácter disponible

    // Si el carácter es un retorno de carro ('\r') o un salto de línea ('\n'), termina la lectura
    if (c == '\n' || c == '\r') {
      flag = 0;
      break;
    }
    if (c== '1'){
      Serial.print(c);
      }

    // Agrega el carácter al string de entrada}
    
    inputString += c;
    }
  }
  
    
 
    //Tratamiento del string------------------------------------
    // Separa la cadena por ";"
    int i = 0;
    char token = strtok(const_cast<char>(inputString.c_str()), ";");
    while (token != NULL && i < 8) {
      tokens[i] = token;
      token = strtok(NULL, ";");
      i++;
    }
  
    // Convierte los tokens en bytes y almacénalos en arrays de 8 elementos
    for (int row = 0; row < 8; row++) {
      for (int col = 0; col < 8; col++) {
        arrays[row][col] = tokens[row][col] == '1' ? 1 : 0; // Convierte el carácter '1' en 1, de lo contrario, en 0
      }
    }
    //------------------------------------------------------
  
    
    
    misc(arrays);
    inputString = "";
  
  
  
  
   
}
