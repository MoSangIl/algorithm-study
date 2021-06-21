#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; ++i) {
        int row, col;
        cin >> row >> col;

        vector<vector<int>> gold_mine(20, vector<int>(20, 0));

        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                cin >> gold_mine[r][c];
            }
        }
        vector<vector<int>> dp(20, vector<int>(20, 0));
        for (int c = 0; c < col; ++c) {
            for (int r = 0; r < row; ++r) {
                if (c == 0) {
                    dp[r][c] = gold_mine[r][c];
                } else {
                    dp[r][c] = 0;
                    int gold = gold_mine[r][c];
                    // 위
                    if (r - 1 >= 0) {
                        dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + gold);
                    }
                    // 아래
                    if (r + 1 <= row) {
                        dp[r][c] = max(dp[r][c], dp[r + 1][c - 1] + gold);
                    }
                    // 옆
                    dp[r][c] = max(dp[r][c], dp[r][c - 1] + gold);
                }
            }
        }
        int result = 0;
        for (int r = 0; r < row; ++r) {
            result = max(result, dp[r][col - 1]);
        }
        cout << result;
    }
}
