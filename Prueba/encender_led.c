#INCLUDE <16f877a.h>
#USE DELAY (CLOCK=4000000)
#FUSES XT, NOPROTECT, NOWDT
#DEFINE SW PORTA, 1 //entrada
#DEFINE LED BORTB, 0 //salida
#BYTE PORTA = 0x05
#BYTE BORTB= 0x06
#use rs232(baud=9600,xmit=pin_c6,rcv=pin_c7,bits=8)


void main(){
   Set_Tris_A(0b00000010); //se indica que el bit 1 del puerto A se configura como entrada
   Set_Tris_B(0b11111110); //se configura el bit 0 del puerto B como salida
   char valorRecibido;
   Bit_clear(LED);
   while(true){
      valorRecibido=getc(); 
      switch(valorRecibido){
         case 'E':
            //output_toggle(pin_b0);
            bit_set(LED); 
         break;
         case 'A':
            //output_toggle(pin_b0);
            Bit_clear(LED);
         break; 
      }
      
      /*if(bit_test(SW))
      { //si SW está activado
         bit_set(LED);   //enciende el LED
      }
      else
      {
         Bit_clear(LED);   //apagar el led
      }
      */
   }
}

