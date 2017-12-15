#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*namespace 命名空间，可以把一些全局的变量、函数、类等分别放在各个命名空间中，从而与其他全局的变量、函数、类变分隔开来。以减少命名的冲突。*/

void coutvec(vector<int> v)
{
    cout << "Vector 输出:" << endl;
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << "\r\n\r\n";
}


int main()
{
    vector<int> v;
    v.reserve(20);
    for(int i = 20; i > 0; i--){
        v.push_back(i);
    }
    coutvec(v); 

    cout << "reverse(v.begin()+10, v.end()+20):" << endl;
    reverse(v.begin()+10, v.begin()+20);
    coutvec(v);

    cout << "sort(v.begin(), v.end()):" <<endl;
    sort(v.begin(), v.end());
    coutvec(v);
    
    cout << "fill(v.begin(), v.begin+5, -1):" <<endl;
    fill(v.begin(), v.begin()+5, -1);
    coutvec(v);

    cout << "copy(v.begin(), v.begin()+5, v.begin()+6):" <<endl;
    copy(v.begin(), v.begin()+5, v.begin()+5);
    coutvec(v);

    cout << "replace(v.begin(), v.begin()+5, -1, 233):" << endl;
    replace(v.begin(), v.begin()+5, -1, 233);
    coutvec(v);
    
    cout << "unique(v.begin(), v.end()):" <<endl;
    std::vector<int>::iterator it;
    it = unique(v.begin(), v.end());
    v.resize(distance(v.begin(), it));
    coutvec(v);
    return 0;
}
