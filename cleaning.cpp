#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main() {
    ifstream fin("raw_data.csv");
    ofstream fout("cleaned_d.csv");

    if (!fin.is_open()) {
        cout << "Error opening input file\n";
        return 1;
    }

    // Write header
    fout << "CGPA,Internships,Projects,Workshops"
         << "AptitudeTestScore,SoftSkillsRating,PlacementTraining,Placed\n";

    string line;
    getline(fin, line); 

    while (getline(fin, line)) {
        stringstream ss(line);
        string col[8];

        for (int i = 0; i < 8; i++) {
            getline(ss, col[i], ',');
        }

        // Converting Yes/No to 1/0
        int placementTraining = (col[6] == "Yes") ? 1 : 0;

        // Converting Placed / NotPlaced to 1 / 0
        int placed = (col[7] == "Placed") ? 1 : 0;

        // Write cleaned numeric data
        fout << col[0] << ","  
             << col[1] << ","  
             << col[2] << ","  
             << col[3] << ","  
             << col[4] << ","  
             << col[5] << ","   
             << placementTraining << ","
             << placed << "\n";
    }

    fin.close();
    fout.close();

    cout << "✅ Data cleaned successfully!\n";
    return 0;
}