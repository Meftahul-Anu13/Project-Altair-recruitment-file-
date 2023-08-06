#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
tuple<int, int, char> last_position(string &str, pair<int, int> &grid)
{
    int i = 0, j = 0;
    int x, y;
    vector<char> directions = {'N', 'E', 'S', 'W'}; // North, East, South, West
    int k = 0;                                      // Index to keep track of the direction
    // 3D vector vitualization
    // N-> k=0; , E-> k=1, S-> k=2, W-> k=3;
    for (char s : str)
    {
        if (s == 'F')
        {
            if (directions[k] == 'N')
            {
                j++;
            }
            else if (directions[k] == 'E')
            {
                i++;
            }
            else if (directions[k] == 'S')
            {
                j--;
            }
            else if (directions[k] == 'W')
            {
                i--;
            }
        }
        else if (s == 'R')
        {
            k = (k + 1) % 4;
        }
        else if (s == 'L')
        {
            k = (k - 1 + 4) % 4;
        }
        // Ensure positions within the grid boundaries

        if (i < 0)
        {
            x = 0;
        }
        else if (i >= grid.first)
        {
            x = grid.first - 1;
        }
        else
        {
            x = i;
        }

        if (j < 0)
        {
            y = 0;
        }
        else if (j >= grid.second)
        {
            y = grid.second - 1;
        }
        else
        {
            y = j;
        }

        // cout<<x<<" "<<y<<" "<<k<<endl;
    }
    // cout << x << " " << y << " " << directions[k] << endl;
    char direction = directions[k];
    return make_tuple(x, y, direction);
}

int main()
{
    string str;
    cin >> str;
    int x1, y1;
    cin >> x1 >> y1;
    pair<int, int> grid(x1, y1);
    tuple<int, int, char> result = last_position(str, grid);
    cout << get<0>(result) << " " << get<1>(result) << " " << get<2>(result) << endl;

    return 0;
}
