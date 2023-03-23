//Wyznaczyć kolejne elementy ciągu xk+1 = xk + 3xk (1 - xk), x0 = 0.1, i porównać
//otrzymane wartości dla różnej precyzji zmiennych (float, double, long double).
//Powtórzyć doświadczenie dla przekształconej postaci wzoru: xk+1 = 4xk - 3xk xk.
//Spróbować wyjaśnić otrzymane wyniki.

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void fdouble(int k, double x,double tab[]) {
    tab[0] = x;
    for (int i = 1; i < k; i++) {
        x = x+3*x*(1-x);
        tab[i] = x;
    }
}

void fdoubleC(int k,double x,double tab[]) {
    tab[0] = x;
    for (int i = 1; i < k; i++) {
        x = 4 * x - 3 * x * x;
        tab[i] = x;
    }
}

void flongdouble(int k, long double x, long double tab[]) {
    tab[0] = x;

    for (int i = 1; i < k; i++) {
        x = x+3*x*(1-x);
        tab[i] = x;
    }
}

void flongdoubleC(int k, long double x, long double tab[]) {
    tab[0] = x;
    for (int i = 1; i < k; i++) {
        x = 4 * x - 3 * x * x;
        tab[i] = x;
    }
}

void ffloat(int k, float x, float tab[]) {
    tab[0] = x;
    for (int i = 1; i < k; i++) {
        x = x+3*x*(1-x);
        tab[i] = x;
    }
}

void ffloatC(int k, float x, float tab[]) {
    tab[0] = x;
    for (int i = 1; i < k; i++) {
        x = 4 * x - 3 * x * x;
        tab[i] = x;
    }
}

void checking(int k, int prec){
    ofstream file("C:\\Semestr 4\\Mownit\\Zestaw 0\\check.csv");
    float tabF[k+1];
    double tabD[k+1];
    float tabFC[k+1];
    long double tabDL[k+1];
    ffloat(k, 0.1f, tabF);
    fdouble(k, 0.1, tabD);
    ffloatC(k, 0.1f, tabFC);
    flongdouble(k,0.1,tabDL);
    for (int j = 0; j < k; j++) {
        file << setprecision(prec) << (tabF[j]-tabD[j]);
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;
    for (int j = 0; j < k; j++) {
        file << setprecision(prec) << (tabF[j]-tabFC[j]);
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;
    for (int j = 0; j < k; j++) {
        file << setprecision(prec) << (tabFC[j]-tabD[j]);
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;
    for (int j = 0; j < k; j++) {
        file << setprecision(prec) << (tabD[j]-tabDL[j]);
        if (j != k - 1) {
            file << ", ";
        }
    }
}


void makingdata(int k, int prec) {
    ofstream file("C:\\Semestr 4\\Mownit\\Zestaw 0\\dat.csv");
    long double tabDL[k+1];
    float tabF[k+1];
    double tabD[k+1];
    long double tabDLC[k+1];
    float tabFC[k+1];
    double tabDC[k+1];
    ffloat(k, 0.1f, tabF);
    fdouble(k, 0.1, tabD);
    flongdouble(k, 0.1l, tabDL);
    ffloatC(k, 0.1f, tabFC);
    fdoubleC(k, 0.1, tabDC);
    flongdoubleC(k, 0.1l, tabDLC);
    for (int j = 0; j < k; j++) {
        file << setprecision(prec) << tabF[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;

    for (int j = 0; j < k; j++) {
        file << tabD[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;

    for (int j = 0; j < k; j++) {
        file << tabDL[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;

    for (int j = 0; j < k; j++) {
        file << tabFC[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;

    for (int j = 0; j < k; j++) {
        file << tabDC[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl << endl;

    for (int j = 0; j < k; j++) {
        file << tabDLC[j];
        if (j != k - 1) {
            file << ", ";
        }
    }
    file << endl;
}



int main() {
    int k;
    int prec;
    cout<<"Podaj liczbe wywolan: "<<endl;
    cin>>k;
    cout<<"Podaj precyzje obliczen"<<endl;
    cin>>prec;
    clock_t start =clock();
    clock_t time;
    start = clock();
    makingdata(k, prec);
    time = clock()-start;
    cout << "Time to execute: " << time/((double)CLOCKS_PER_SEC/1000) << endl;
    checking(k, prec);
    return 0;
}