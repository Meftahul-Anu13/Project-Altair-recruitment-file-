// Online C++ compiler to run C++ program online
#include <iostream>
#include <unordered_map>
#include <vector>
#include <set>
#include <list>
#include <queue>

using namespace std;
///@brief 
/// @param visited  
///@param vertex 
/// @return 
// BREIF DISCUSSION :

/*here BFS is used as a traversal technique to identify the vertices are covered are not ,by using visited vector
we keep the survey of the vertex along with the adjacency list and fifo ds using queue.The problem is indicating also disconnecting graph 
along with bi-directional indicating undirected graph with covering all vertices in a common pathway like Hamiltonian path*/
/* 1.valid function checks all the visited node is true or not .
2.preparing_adj_list creats all the edges and vertices adjacency list .
3.void bfs travers all the vertices .
4.vector BFS creats the full code perfect by calling all the function with its neccessary use ;
*/

bool valid(unordered_map<int, bool> &visited, int vertex)
{
    // for ( auto& entry : visited) {
    //     if (!entry.second) {
    //         return false;
    //     }
    // }
    // return true;
    // Check if all locations are visited or not !!
    for (int i = 0; i < vertex; ++i)
    {
        if (!visited[i])
        {
            return false;
        }
    }
    return true;
}

void preparing_adj_list(unordered_map<int, set<int>> &adj, const vector<pair<int, int>> &edges)
{
    for (const auto &edge : edges)
    {
        int u = edge.first;//u & v are the vertices connecting both by edge;
        int v = edge.second;
        //since the graph is bi directional its indicate the undirected graph; so putting u edges to v and vice versa;
        adj[u].insert(v);
        adj[v].insert(u);
    }
}

void bfs(unordered_map<int, set<int>> &adj, unordered_map<int, bool> &visited, int node, vector<int> &ans, int vertex)
{
    queue<int> q; // for FIFO ALGO ;
    q.push(node);
    // q.push(0);
    visited[node] = true;
    // visited[0] = true;

    while (!q.empty())
    {
        int front_node = q.front();
        q.pop();
        // storing frontnode into ans vector;

        ans.push_back(front_node);
        // traversing all the neighbours of frontnode
        for (int i : adj[front_node])
        {
            if (!visited[i])
            {
                visited[i] = 1;
                q.push(i);
            }
        }
    }

    // true false result:
    bool result = valid(visited, vertex);
    if (result)
        cout << "True" << endl;
    else
        cout << "False " << endl;
}

vector<int> BFS(int vertex, const vector<pair<int, int>> &edges)
{
    unordered_map<int, set<int>> adj;
    // here for sorting order we take set ,we can take list also
    unordered_map<int, bool> visited;

    vector<int> ans;
    preparing_adj_list(adj, edges);

    bfs(adj, visited, 0, ans, vertex);

    return ans;
}

int main()
{
    int Vertices = 7;//to change the edge and vertex also change the vertices variable otherwise return false will be deducted 
    vector<pair<int, int>> Edges = {{0, 1}, {1, 2}, {2, 0}, {3, 4}, {4, 5}, {5, 6}, {6, 3}};
// to change this edges change the element of the pair vector ;
    BFS(Vertices, Edges);
    // unordered_map<int, bool> visit;
    // traversal of the graph
    // for (int vertex : traversal) {
    //     visit[vertex] = true;
    // }

    return 0;
}

// Dry run
//  n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
//  Output: false
//  n = 3, edges = [[0,1],[1,2],[2,0]]
//  Output: true
//  Vertices = 7
//  Edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]
