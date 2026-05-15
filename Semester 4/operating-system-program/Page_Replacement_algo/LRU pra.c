#include<stdio.h>

int main()
{
    int n, frames;

    printf("Enter number of pages: ");
    scanf("%d",&n);

    int pages[n];

    printf("Enter page reference string:\n");

    for(int i=0;i<n;i++)
    {
        scanf("%d",&pages[i]);
    }

    printf("Enter number of frames: ");
    scanf("%d",&frames);

    int frame[frames], time[frames];

    for(int i=0;i<frames;i++)
    {
        frame[i] = -1;
    }

    int counter = 0, faults = 0;

    for(int i=0;i<n;i++)
    {
        int found = 0;

        for(int j=0;j<frames;j++)
        {
            if(frame[j] == pages[i])
            {
                counter++;
                time[j] = counter;
                found = 1;
                break;
            }
        }

        if(found == 0)
        {
            int pos = 0;

            for(int j=1;j<frames;j++)
            {
                if(time[j] < time[pos])
                {
                    pos = j;
                }
            }

            frame[pos] = pages[i];

            counter++;
            time[pos] = counter;

            faults++;
        }
    }

    printf("Page Faults = %d\n", faults);

    return 0;
}