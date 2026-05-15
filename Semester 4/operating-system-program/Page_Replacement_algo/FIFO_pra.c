#include<stdio.h>

int main()
{
    int pages, frames;

    printf("Enter number of pages: ");
    scanf("%d",&pages);

    int p[pages];

    printf("Enter page reference string:\n");

    for(int i=0;i<pages;i++)
    {
        scanf("%d",&p[i]);
    }

    printf("Enter number of frames: ");
    scanf("%d",&frames);

    int f[frames];

    for(int i=0;i<frames;i++)
    {
        f[i] = -1;
    }

    int page_faults = 0, index = 0;

    for(int i=0;i<pages;i++)
    {
        int found = 0;

        for(int j=0;j<frames;j++)
        {
            if(f[j] == p[i])
            {
                found = 1;
                break;
            }
        }

        if(found == 0)
        {
            f[index] = p[i];
            index = (index + 1) % frames;
            page_faults++;
        }
    }

    printf("Page Faults = %d\n", page_faults);

    return 0;
}