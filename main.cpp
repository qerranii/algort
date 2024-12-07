#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> process(int N, vector<string>& arr, int Q, vector<pair<int, pair<int, int>>>& qq) {
    vector<string> res;

    for (auto& query : qq) {
        if (query.first == 1) {
            int K = query.second.first;
            string result = "";
            for (int i = 0; i < N; ++i) {
                result += arr[i].substr(0, min(K, (int)arr[i].size()));
            }
            res.push_back(result);
        }
        else if (query.first == 2) {
            int L = query.second.first;
            int R = query.second.second;
            string result = "";
            for (int i = 0; i < N; ++i) {
                if (L - 1 < arr[i].size()) {
                    result += arr[i].substr(L - 1, min(R - L + 1, (int)arr[i].size() - (L - 1)));
                }
            }
            res.push_back(result);
        }
    }

    return res;
}

int main() {
    int N, Q;
    cin >> N;
    vector<string> arr(N);

    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }

    cin >> Q;
    vector<pair<int, pair<int, int>>> qq(Q);

    for (int i = 0; i < Q; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int K;
            cin >> K;
            qq[i] = { 1, {K, 0} };
        }
        else if (type == 2) {
            int L, R;
            cin >> L >> R;
            qq[i] = { 2, {L, R} };
        }
    }

    vector<string> res = process(N, arr, Q, qq);

    for (const string& r : res) {
        cout << r << endl;
    }

    return 0;
}
