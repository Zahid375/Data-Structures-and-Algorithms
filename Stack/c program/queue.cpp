#include <iostream>
using namespace std;
#define SIZE 5
int rear = -1;
int font = 0;
int arr[SIZE];

void push(int v)
{
    if (rear == SIZE - 1)
    {
        cout << "Array dont have empty space";
    }
    else
    {
        rear++;
        arr[rear] = v;
    }
}

int pop()
{
    if (font > rear)
    {
        cout << "array is empty";
    }
    else
    {
        int value = arr[font];
        font++;
        return value;
    }
    return 0;
}

void dispaly()
{
    for (int i = font; i <= rear; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    pop();
    dispaly();
}