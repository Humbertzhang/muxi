#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main()
{
    cout << "Queue:" <<endl;
    queue<int> q;
    for(int i = 1; i <= 10; i++) {
        q.push(i);
    }
    while(!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }

    cout << "\r\n\r\n" << endl;

    cout << "Stack:" <<endl;
    stack<int> s;
    for(int i = 1; i <= 10; i++) {
        s.push(i);
    }
    while(!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}
