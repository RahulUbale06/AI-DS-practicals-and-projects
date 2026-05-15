#include<stdio.h>

int main()
{
    int mutex = 1;
    int full = 0;
    int empty = 3;
    int x = 0;
    int choice;

    while(1)
    {
        printf("\n1. Producer");
        printf("\n2. Consumer");
        printf("\n3. Exit");

        printf("\nEnter choice: ");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1:

                if((mutex == 1) && (empty != 0))
                {
                    mutex = 0;
                    full++;
                    empty--;
                    x++;

                    printf("Produced item %d", x);

                    mutex = 1;
                }
                else
                {
                    printf("Buffer Full");
                }

                break;

            case 2:

                if((mutex == 1) && (full != 0))
                {
                    mutex = 0;
                    full--;
                    empty++;
                    printf("Consumed item %d", x);
                    x--;

                    mutex = 1;
                }
                else
                {
                    printf("Buffer Empty");
                }

                break;

            case 3:
                return 0;
        }
    }
}