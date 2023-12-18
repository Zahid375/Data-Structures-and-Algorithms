#include <iostream>
using namespace std;
#define SIZE 5
int top = -1;
int arr[SIZE];

void push(int v)
{
    if (top == SIZE - 1)
    {
        cout << "Array dont have empty space";
    }
    else
    {
        top++;
        arr[top] = v;
    }
}

int pop()
{
    if (top == -1)
    {
        cout << "array is empty";
    }
    else
    {
        int value = arr[top];
        top--;
        return value;
    }
    return 0;
}

void dispaly()
{
    for (int i = top; i >= 0; i--)
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
    dispaly();
}