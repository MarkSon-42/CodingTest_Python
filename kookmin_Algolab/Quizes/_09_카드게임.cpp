#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
struct s{
    int start,d;
};

struct cmp{
    bool operator()(s a, s b){
        if(a.d == b.d){
            return a.start < b.start;
        }
        return a.d > b.d;
    }
};

int main(int argc, const char * argv[]) {
    int T;
    cin>>T;
    while(T--){
        int n,m,k;
        cin>>n>>m>>k;
        vector<int> v;
        int a;
        for(int i=0 ; i<m ; i++){
            cin>>a;
            v.push_back(a);
        }
        sort(v.begin(), v.end());
        int groupMin=v[0];
        int result=groupMin;
        priority_queue<s, vector<s>, cmp> q;
        for(int i=1 ; i<v.size() ; i++){
            //연속됨
            if(v[i-1]+1 == v[i]){
//                arr[i] = groupMin;
            } else { //연속안됨
                groupMin = v[i];
                result+=v[i];
                q.push({v[i], v[i]-v[i-1]-1});
            }
        }

        for(int i=0 ; i<k ; i++){
            if(q.empty()){
                cout<<result<<" ";
                continue;
            }
            s top = q.top();
            q.pop();
            v.push_back(top.start-1);
            if(top.d==1){
                result-=top.start;
            }
            else{
                result--;
                q.push({top.start-1, top.d-1});
            }
            cout<<result<<" ";
        }
        cout<<"\n";
    }
}
