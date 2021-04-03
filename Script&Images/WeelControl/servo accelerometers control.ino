#include <Servo.h> //Includiamo la libreria servo
Servo servo1;      //Nominiamo il nostro servomotore in "servo1"

//  Variabili globali
int pos = 0;          
int posprec = 0;  
int gradi = 0;         
int incremento = 1;  // valore di incremento
int ENA=11; // ENABLE A sul pin 11
int IN1=10; // IN1 sul pin 10
int IN2=9;  // IN2 sul pin 9
int IN3=8;  // IN3 sul pin 8
int IN4=7;  // IN4 sul pin 7
int ENB=6;  // ENABLE B sul pin 6
int velocita = 120; // velocità motori (min 120 max 255, gap compreso) 
int rotazione90 = 300; // tempo ritardo rotazione
float cm;              // centimetri in numeri decimali e non interi

//Ciclo programma
void loop() 
{ 
digitalWrite(IN1,1);        // Attiva il pin IN1 
digitalWrite(IN2,0);        // Disattiva il pin IN2
digitalWrite(IN3,1);        // Attiva il pin IN3
digitalWrite(IN4,0);        // Disattiva il pin IN4
analogWrite(ENA, velocita); // Attiva il motore A 
analogWrite(ENB, velocita); // Attiva il motore B
} 

void setup() 
{ 
delay (3000);       //aspetto 3 secondi
servo1.attach(5);   // servo1 sul pin 5 
servo1.write (90);  //fermo il servo a 90gradi
posprec = 90;            //imposto la variabile posprec a 90
pinMode(ENA,OUTPUT);     //Pin ENA come uscita
pinMode(ENB,OUTPUT);     //Pin ENB come uscita
pinMode(IN1,OUTPUT); 
pinMode(IN2,OUTPUT); 
pinMode(IN3,OUTPUT); 
pinMode(IN4,OUTPUT); 
pinMode(2, OUTPUT);     //Pin 2 come uscita
pinMode(3, INPUT);      //Pin 3 come entrata (lettura sensore)
analogWrite(ENA,0); // blocca il motore A 
analogWrite(ENB,0); // blocca il motore B 
} 




