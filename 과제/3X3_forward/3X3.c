#include <stdio.h>
#include <math.h>

int main()
{
   double input[3] = {0.9, 0.1, 0.8};
   double Winput_hidden[3][3] = {{0.9, 0.3, 0.4}, {0.2, 0.8, 0.2}, {0.1, 0.5, 0.6}};
   double Whidden_output[3][3] = {{0.3, 0.7, 0.5}, {0.6, 0.5, 0.2}, {0.8, 0.1, 0.9}};
   
   // double Winput_hidden[3][3] = {{0.9, 0.8, 0.9}, {0.1, 0.2, 0.3}, {0.8, 0.1, 0.9}};
   // double Whidden_output[3][3] = {{0.8, 0.7, 0.9}, {0.1, 0.2, 0.1}, {0.1, 0.5, 0.6}};

   double Xhidden[3] = {0,};
   double Ohidden[3] = {0,};
   double Xoutput[3] = {0,};
   double Ooutput[3] = {0,};

   // Weight input to hidden
   for(int i = 0; i < 3; i++)
   {
      for(int j = 0; j < 3; j++)
      {
         Xhidden[i] += input[j] * Winput_hidden[i][j];
         
      }
      Ohidden[i] = 1 / (1 + exp(-Xhidden[i]));
      
   }
   
   // Weight hidden to output
   for(int i = 0; i < 3; i++)
   {
      for(int j = 0; j < 3; j++)
      {
         Xoutput[i] += Ohidden[j] * Whidden_output[i][j];
      }
      Ooutput[i] = 1 / (1 + exp(-Xoutput[i]));
   }

   printf("input     Ohidden     Ooutput\n");
   for(int i = 0; i < 3; i++)
   {
      printf("%.2f  --> %.4f  --> %.4f\n", input[i], Ohidden[i], Ooutput[i]);
      // .3f 시 반올림으로 인해 0.7086 --> 0.709
   }


   return 0;
}