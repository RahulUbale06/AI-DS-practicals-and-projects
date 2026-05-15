#include<stdio.h>

int main()
{
    int n, tq;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n], rem_bt[n], wt[n], tat[n];

    printf("Enter burst times:\n");

    for(int i=0; i<n; i++)
    {
        scanf("%d", &bt[i]);
        rem_bt[i] = bt[i];
    }

    printf("Enter time quantum: ");
    scanf("%d", &tq);

    int time = 0;

    while(1)
    {
        int done = 1;

        for(int i=0; i<n; i++)
        {
            if(rem_bt[i] > 0)
            {
                done = 0;

                if(rem_bt[i] > tq)
                {
                    time += tq;
                    rem_bt[i] -= tq;
                }
                else
                {
                    time += rem_bt[i];

                    wt[i] = time - bt[i];

                    rem_bt[i] = 0;
                }
            }
        }

        if(done == 1)
        {
            break;
        }
    }

    for(int i=0; i<n; i++)
    {
        tat[i] = wt[i] + bt[i];
    }

    printf("\nProcess\tBT\tWT\tTAT\n");

    for(int i=0; i<n; i++)
    {
        printf("P%d\t%d\t%d\t%d\n",
               i+1, bt[i], wt[i], tat[i]);
    }

    return 0;
}