#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int n, price;
    cin >> n >> price;

    vector<int> coins;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        coins.push_back(x);
    }

    vector<int> dp(price + 1, price); // DP 초기화
    // cpp의 벡터 초기화 (크기, 값)

    for (int i = 1; i < price + 1; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == coins[j]) {
                dp[i] = 1;
            } else if (i < coins[j]) {
                dp[i] = -1;
            } else if (i > coins[j]) {
                int remainder = i - coins[j];
                if (dp[remainder] != -1) {
                    dp[i] = min(dp[i], dp[remainder] + 1);
                } else {
                    dp[i] = -1;
                }
            }
        }
    }
}
