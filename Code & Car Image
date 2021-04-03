////////////////////////////////////////////////
// Progetto ARDUINO ROBOT CAR EVITA OSTACOLI CON SERVO E HC-SR04
// Autore AMATO FRANCESCO 5G
/////////////////////////////////////////////////

#include <Servo.h> //Includo la libreria servo
Servo servo1;      //Nomino il nostro servomotore in "servo1"

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

/* Dichiarazione funzione avanti */
void avanti (void) 
{ 
digitalWrite(IN1,1);        // Attiva il pin IN1 
digitalWrite(IN2,0);        // Disattiva il pin IN2
digitalWrite(IN3,1);        // Attiva il pin IN3
digitalWrite(IN4,0);        // Disattiva il pin IN4
analogWrite(ENA, velocita); // Attiva il motore A 
analogWrite(ENB, velocita); // Attiva il motore B
} 

/* Dichiarazione funzione sinistra 90 gradi  */
void sx90 (void) 
{ 
digitalWrite(IN1,0);        // Attiva il pin IN1 
digitalWrite(IN2,1);        // Disattiva il pin IN2
digitalWrite(IN3,1);        // Attiva il pin IN3
digitalWrite(IN4,0);        // Disattiva il pin IN4
analogWrite(ENA, velocita); // Attiva il motore A 
analogWrite(ENB, velocita); // Attiva il motore B
delay (rotazione90);        // aspetta il tempo dichiarato nella variabile "rotazione90"
analogWrite(ENA,0);         // blocca il motore A 
analogWrite(ENB,0);         // blocca il motore B 
} 

/* Dichiarazione funzione destra 90 gradi  */
void dx90 (void) 
{ 
digitalWrite(IN1,1);        // Attiva il pin IN1 
digitalWrite(IN2,0);        // Disattiva il pin IN2
digitalWrite(IN3,0);        // Disattiva il pin IN3
digitalWrite(IN4,1);        // Attiva il pin IN4
analogWrite(ENA, velocita); // Attiva il motore A 
analogWrite(ENB, velocita); // Attiva il motore B
delay (rotazione90);        // aspetta il tempo dichiarato nella variabile "rotazione90"
analogWrite(ENA,0);         // blocca il motore A
analogWrite(ENB,0);         // blocca il motore B 
} 

/* Dichiarazione funzione sensore  */
void sensore (void)  
{ 
gradi = posprec;        
incremento = 1;      
if (pos <= posprec)     // se la variabile posizione è minore o uguale a posprec
incremento = -1;        // incrementa di -1
for(posprec = gradi; posprec != pos; posprec = posprec + incremento)  
{ 
servo1.write(posprec);  // sposto il servomotore nella posizione posprec 
delay(15);              //aspetto 15 millisecondi
} 
digitalWrite(2, LOW);   //disattivo il pin 2
delayMicroseconds(2);   //aspetto 2 microsecondi 
digitalWrite(2, HIGH);  //attivo il pin 2
delayMicroseconds(10);  //attendo 10 microsecondi
digitalWrite(2, LOW);   //disattivo il pin 2
cm = pulseIn(3, HIGH) / 58.0;  //funzione lettura distanza 
} 


void setup() 
{ 
delay (3000);            //aspetto 3 secondi
servo1.attach(5);        // servo1 sul pin 5 
servo1.write (45);       //fermo il servo a 90gradi
posprec = 90;            //imposto la variabile posprec a 90
pinMode(ENA,OUTPUT);     //Pin ENA come uscita
pinMode(ENB,OUTPUT);     //Pin ENB come uscita
pinMode(IN1,OUTPUT); 
pinMode(IN2,OUTPUT); 
pinMode(IN3,OUTPUT); 
pinMode(IN4,OUTPUT); 
pinMode(2, OUTPUT);     //Pin 2 come uscita
pinMode(3, INPUT);      //Pin 3 come entrata (lettura sensore)
analogWrite(ENA,0);     // blocca il motore A 
analogWrite(ENB,0);     // blocca il motore B 
} 

//Ciclo programma
void loop() 
{ 
pos = 45; //servo a 90 gradi
sensore ();   // ciclo descritto nel void sensore (void sensore (void) )

if (cm > 30)  // se cm superiore a 30
{ 
avanti();     // ciclo descritto nel void avanti (void avanti (void) )
} 
else          
{ 
analogWrite(ENA,0); // blocca il motore A 
analogWrite(ENB,0); // blocca il motore B 
pos = 0;        // imposto il servo a 0 gradi
sensore ();     // ciclo descritto nel void sensore
if (cm > 30)    // se cm superiore a 30
{ 
dx90 ();        // ciclo descritto nel void dx90
dx90 ();        // ciclo descritto nel void dx90
} 
else 
sensore ();   // ciclo descritto nel void sensore
if (cm > 30)  // se cm superiore a 30
{ 
sx90 ();      // ciclo descritto nel void sx90
} 
else 
{ 
sx90 ();    // ciclo descritto nel void sx90
sx90 ();    // rieseguo il ciclo descritto nel void sx90
   }     
   }   
   } 
