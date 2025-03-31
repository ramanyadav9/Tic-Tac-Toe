#include<iostream>
using namespace std;
int x='x',o='O';

void printBoard(int xstate[9], int ystate[9]){
    char zero = (xstate[0] ? x : (ystate[0] ? o :'0' ));
    char one = (xstate[1] ? x : (ystate[1] ? o : '1'));
    char two = (xstate[2] ? x : (ystate[2] ? o : '2'));
    char three = (xstate[3] ? x : (ystate[3] ? o : '3'));
    char four = (xstate[4] ? x : (ystate[4] ? o : '4'));
    char five = (xstate[5] ? x : (ystate[5] ? o : '5'));
    char six = (xstate[6] ? x : (ystate[6] ? o : '6'));
    char seven = (xstate[7] ? x : (ystate[7] ? o : '7'));
    char eight= (xstate[8] ? x : (ystate[8] ? o : '8'));

    cout<<"************"<<endl;
    cout<< zero<<" | "<<one<<" | "<<two<<endl;
    cout<<"--"<<"| "<<"--"<<"| "<<"--"<<endl;
    cout<< three<<" | "<<four<<" | "<<five<<endl;
    cout<<"--"<<"| "<<"--"<<"| "<<"--"<<endl;
    cout<< six<<" | "<<seven<<" | "<<eight<<endl;
    cout<<"************";

}
int sum(int a, int b, int c){
    return a+b+c;
}   
int checkWin(const int xstate[9], const int zstate[9]) {
    const int winning_combos[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // Rows
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // Columns
        {0, 4, 8}, {2, 4, 6}              // Diagonals
    };

    for (const auto& win : winning_combos) {
        if (sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3) {
            return 1;
        }
        if (sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3) {
            return 0;
        }
    }

    return -1;
}


int main(){
    int xstate[9]={0,0,0,0,0,0,0,0,0};
    int ystate[9]={0,0,0,0,0,0,0,0,0};
    int turn = 1;
    cout<<"WELCOME TO TIC TAC TOE GAME !\n";
    while(true){
        printBoard(xstate, ystate);
        cout<<"\nENTER THE NUMBER FROM THE BOARD ON YOUR CHANCE !\n"<<endl;
        if(turn == 1){
            cout<<"X CHANCE"<<endl;
            int val;
            cout<<"Enter the value: ";
            cin>>val;
            xstate[val] = 1;
        }
        else{
            cout<<"O CHANCE"<<endl;
            int val;
            cout<<"Enter the value: ";
            cin>>val;
            ystate[val] = 1;
        }
        int result = checkWin(xstate, ystate);
        if (result == 1) {
            printBoard(xstate, ystate);
            cout << "\n X won the match!" << endl;
            break;
        } else if (result == 0) {
            printBoard(xstate, ystate);
            cout << "\n O won the match!" << endl;
            break;
        } else if (result == -1) {
            
            turn = !turn;
        }
    }

    return 0;
}