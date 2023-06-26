#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double cal_angle(double x, double y)
{
    double theta_x = atan2(y, x) * 180 / M_PI;
    if (theta_x < 0)
    {
        return theta_x + 360;
    }
    return theta_x;
}

int main()
{
    srand(time(NULL));
    double a = 3.0;
    double b = 3.0;

    // printf("%f \n", theta_x);
    double x,y,z;
    double theta_x;
    double x_range,y_range,z_range;
    x_range = 7;
    y_range = 7;
    z_range = 0;

    printf("%d ", rand() % 10);

    for (int i = 0; i < 30; i++)
    {
        
        x = rand() % 3 + (rand() / (double) RAND_MAX);
        y = rand() % 3 + (rand() / (double) RAND_MAX);
        z = rand() % 3 + (rand() / (double) RAND_MAX);
        
        double temp = cal_angle(x,y);
        // printf("%f %f %f\n",x, y, z);
        // printf("%f\n",temp);
        
        // if (((x - 3)*(x - 3)) + ((y - 3)*(y - 3)) <= (a * a) && temp < 30 && z < 1)
        // {
        //     printf("1 부채꼴 안에 있다\n");
        // }
        // else if (((x - 3)*(x - 3)) + ((y - 3)*(y - 3)) <= (a * a) && temp < 60 && z < 2)
        // {
        //     printf("2 부채꼴 안에 있다\n");
        // } 
        // else if (((x - 3)*(x - 3)) + ((y - 3)*(y - 3)) <= (a * a) && temp < 90 && z < 3)
        // {
        //     printf("3 부채꼴 안에 있다\n");
        // } 
        // else
        // {
        //     printf("부채꼴 밖에 있다\n");
        // }
    }
    // Object 1 
    // x : 7 ~ 10
    // y : 7 ~ 10
    // z : 0 ~ 3
    double x1 = 7 + rand() % 3 + (rand() / (double) RAND_MAX);
    double y1 = 7 + rand() % 3 + (rand() / (double) RAND_MAX);
    double z1 = rand() % 3 + (rand() / (double) RAND_MAX);
    // theta_x = cal_angle(x1, y1);
    // printf("%f \n", theta_x);

    // Object 2 
    // x : 7 ~ 10
    // y : 4 ~ 7
    // z : 3 ~ 6
    double x2 = 7 + rand() % 3 + (rand() / (double) RAND_MAX);
    double y2 = 4 + rand() % 3 + (rand() / (double) RAND_MAX);
    double z2 = 3 + rand() % 3 + (rand() / (double) RAND_MAX);
    // theta_x = cal_angle(x2, y2);

    // Object 3
    // x : 4 ~ 7
    // y : 7 ~ 10
    // z : 6 ~ 9
    double x3 = 4 + rand() % 3 + (rand() / (double) RAND_MAX);
    double y3 = 7 + rand() % 3 + (rand() / (double) RAND_MAX);
    double z3 = 6 + rand() % 3 + (rand() / (double) RAND_MAX);



    // if ( (((x*x) + (y*y)) <= (a * a)) && (theta_x < 90))
    // {
    //     printf("It is in 부채꼴");
    // }
    // else
    // {
    //     printf("부채꼴 밖에 있습니다.");
    // }

    return 0;
}