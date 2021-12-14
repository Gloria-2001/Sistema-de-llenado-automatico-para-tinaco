#include <16f877a.h>
#device adc=10
#include <stdio.h>
#fuses XT,NOWDT,NOPROTECT,NOLVP,PUT,BROWNOUT
#use DELAY (CLOCK=4MHz)
#use rs232 (baud=9600,parity=N,xmit=pin_c6,rcv=pin_c7,bits=8)

float distancia,tiempo;
float aux = -1.00;

#define trigger pin_B1
#define echo pin_B0

int Timer2,Postcaler;
//int16 duty;

void main(){
   setup_timer_1(T1_internal|T1_div_by_1);
   Timer2=124;
   Postcaler=1;
   setup_timer_2(t2_div_by_4,Timer2,Postcaler);
   setup_ccp1(ccp_pwm);
   while(true){
      output_high(trigger);
      delay_us(10);
      output_low(trigger);
      
      while(!input(echo));
      set_timer1(0);
      
      while(input(echo));
      tiempo = get_timer1();
      distancia=(tiempo/2)*(0.0343);
      
      if(aux != distancia){
         aux = distancia-3;
         printf("\r%f\n", aux);
         if(aux<=99.54 && aux>=4){
            set_pwm1_duty(1023);
         
         //if(distancia != aux){
         //putc('E');
         //}
         }
         else if(aux>99.54){
            set_pwm1_duty(0);
            printf("\rTinaco vacio\n");
            //if(distancia != aux){
            //putc('A');
            //}
         }
         else{
            set_pwm1_duty(0);
            printf("\rTinaco lleno\n");
         }
      
      }
      
      
      //duty = distancia*1023/400; //Se toman 1023bit de la resolucion max con 400mts
     
      
      //printf("\rDistancia = %f",distancia);
      //printf("\rTiempo = %f",tiempo);
      
      delay_ms(150);
   }
}
