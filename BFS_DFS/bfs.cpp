#include <iostream>
#include <queue>
#include <vector>

using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int start) {
    visited[start] = true;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int target = q.front();
        q.pop();
        cout << target << " ";
        for (int i = 0; i < graph[target].size(); ++i) {
            int node = graph[target][i];
            if (!visited[node]) {
                q.push(node);
                visited[node] = true;
            }
        }
    }
}

int main(void) {
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    graph[2].push_back(1);
    graph[2].push_back(7);
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    graph[4].push_back(3);
    graph[4].push_back(5);
    graph[5].push_back(3);
    graph[5].push_back(4);
    graph[6].push_back(7);
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(7);
    graph[8].push_back(1);
    graph[8].push_back(7);

    for (int i = 0; i < 9; ++i) {
        visited[i] = false;
    }
    bfs(1);
}
