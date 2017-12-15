#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    cout << "Map:" <<endl;
    map<char, string> m;
    m['a'] = "apple";
    m['b'] = "banana";
    m['c'] = "cheery";
    
    std::map<char, string>::iterator it;
    for(it = m.begin(); it != m.end(); ++it) {
        cout << it->first << "=>" << it->second << endl;
    }
    cout << "\r\n\r\n" << endl;
    cout << "MultiMap:" <<endl;
    multimap<char, string> mm;
    mm.insert(make_pair('a', "apple"));
    mm.insert(make_pair('a', "avocado"));
    mm.insert(make_pair('b', "banana"));
    mm.insert(make_pair('b', "berry"));
    mm.insert(make_pair('b', "blueberry"));
    mm.insert(make_pair('c', "cherry"));
    mm.insert(make_pair('c', "core"));
    mm.insert(make_pair('c', "chestnut"));
    mm.insert(make_pair('c', "cumquat"));
    multimap<char, string>::iterator itlow, ithigh;
    itlow = mm.lower_bound('a');
    ithigh = mm.upper_bound('c');
    for(it = itlow; it!=ithigh; ++it){
        cout << (*it).first << "=>" << (*it).second << endl;
    }
    return 0;
}
