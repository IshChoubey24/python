#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int findUniqueElement(vector<vector<int>> &mat) {
    int n = mat.size();
    int m = mat[0].size();  // Assuming the matrix is non-empty and rectangular

    vector<unordered_set<int>> rowSets(n);
    vector<unordered_set<int>> colSets(m);

    // Fill rowSets and colSets with matrix elements
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            rowSets[i].insert(mat[i][j]);
            colSets[j].insert(mat[i][j]);
        }
    }

    // Check each element in the matrix
    for (int num : mat[0]) {
        bool unique = true;

        // Check rows
        for (int i = 0; i < n; i++) {
            rowSets[i].erase(num);
            if (rowSets[i].empty()) {
                return num;
            }
        }

        // Check columns
        for (int j = 0; j < m; j++) {
            colSets[j].erase(num);
            if (colSets[j].empty()) {
                return num;
            }
        }
    }

    return -1;
}

int main() {
    vector<vector<int>> mat = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int result = findUniqueElement(mat);

    cout << result << endl;

    return 0;
}