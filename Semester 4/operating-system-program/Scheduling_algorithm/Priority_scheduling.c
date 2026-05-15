#include<stdio.h>

int main()
{
    int n,i,j,temp;

    printf("Enter number of processes:\n");
    scanf("%d",&n);

    int bt[n],wt[n],tat[n],p[n],pr[n];

    printf("Enter burst times:\n");

    for(i=0;i<n;i++)
    {
        scanf("%d",&bt[i]);
        p[i] = i+1;
    }

    printf("Enter priorities:\n");

    for(i=0;i<n;i++)
    {
        scanf("%d",&pr[i]);
    }

    // Sorting according to priority
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(pr[j] > pr[j+1])
            {
                temp = pr[j];
                pr[j] = pr[j+1];
                pr[j+1] = temp;

                temp = bt[j];
                bt[j] = bt[j+1];
                bt[j+1] = temp;

                temp = p[j];
                p[j] = p[j+1];
                p[j+1] = temp;
            }
        }
    }

    wt[0] = 0;

    for(i=1;i<n;i++)
    {
        wt[i] = wt[i-1] + bt[i-1];
    }

    for(i=0;i<n;i++)
    {
        tat[i] = wt[i] + bt[i];
    }

    printf("\nProcess\tBT\tPR\tWT\tTAT\n");

    for(i=0;i<n;i++)
    {
        printf("P%d\t%d\t%d\t%d\t%d\n",
               p[i], bt[i], pr[i], wt[i], tat[i]);
    }

    return 0;
}