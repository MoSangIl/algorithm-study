#include <iostream>

using namespace std;

int main(void) {
    int tc;
    cin >> tc;

    int *ans = new int[tc];
    for (int i = 0; i < tc; i++) {
        int size;
        cin >> size;

        int **game_table;
        game_table = new int *[size];
        for (int j = 0; j < size; j++) {
            game_table[j] = new int[size];
        }
        for (int k = 0; k < size; k++) {
            for (int l = 0; l < size; l++) {
                cin >> game_table[k][l];
            }
        }

        int **path;
        path = new int *[size];
        for (int j = 0; j < size; j++) {
            path[j] = new int[size];
        }
        path[0][0] = 1;

        for (int j = 0; j < size; j++) {
            for (int row = 0; row < j + 1; row++) {
                for (int col = 0; col < j + 1; col++) {
                    if (path[row][col] == 1) {
                        int val = game_table[row][col];

                        if (row + val <= j) {
                            path[row + val][col] = 1;
                        }
                        if (col + val <= j) {
                            path[row][col + val] = 1;
                        }
                    }
                }
            }
        }
        if (path[size - 1][size - 1] == 1) {
            ans[i] = 1;
        } else {
            ans[i] = 0;
        }
    }

    for (int i = 0; i < tc; i++) {
        if (ans[i] == 1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
