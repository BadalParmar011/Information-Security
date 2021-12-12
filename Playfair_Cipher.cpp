#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

// Hansal Shah - 19BCP043 (6x6 Playfair Cipher)

string encrypt_message(char** matrix, map<char, vector<int>>& positions, string s){
    string final_str = "";
    for(int i=0; i<s.length(); i+=2){
        if(s[i]==' '){
            final_str += s[i];
            i--;
        }
        else{
            char a=s[i], b, final_a, final_b;
            if(i==s.length()-1){
                b = 'x';
            }
            else{
                b=s[i+1];
                if(b==' '){
                    b=s[i+2];
                    i++;
                }
            }

            if(a==b){
                // using x for character stuffing
                b = 'x';
                i--;
            }

            int x1 = positions[a][0], y1 = positions[a][1], x2 = positions[b][0], y2 = positions[b][1];

            if(x1==x2){
                y1=(y1+1)%6; y2=(y2+1)%6;
                final_a = matrix[x1][y1]; final_b = matrix[x1][y2];
            }
            else if(y1==y2){
                x1=(x1+1)%6; x2=(x2+1)%6;
                final_a = matrix[x1][y1]; final_b = matrix[x2][y1];
            }
            else{
                final_a = matrix[x1][y2]; final_b = matrix[x2][y1];
            }
            final_str= final_str + final_a + final_b;
        }
    }
    return final_str;
}

string decrypt_message(char** matrix, map<char, vector<int>>& positions, string s){
    string final_str = "";
    for(int i=0; i<s.length(); i+=2){
        if(s[i]==' '){
            final_str += s[i];
            i--;
        }
        else{
            char a=s[i], b, final_a, final_b;
            if(i==s.length()-1){
                b = 'x';
            }
            else{
                b=s[i+1];
                if(b==' '){
                    b=s[i+2];
                    i++;
                }
            }

            if(a==b){
                // using x for character stuffing
                b = 'x';
                i--;
            }

            int x1 = positions[a][0], y1 = positions[a][1], x2 = positions[b][0], y2 = positions[b][1];

            if(x1==x2){
                y1=y1-1; y2=y2-1; 
                if(y1<0)
                    y1+=6;
                if(y2<0)
                    y2+=6;
                final_a = matrix[x1][y1]; final_b = matrix[x1][y2];
            }
            else if(y1==y2){
                x1-=1; x2-=1; 
                if(x1<0)
                    x1+=6;
                if(x2<0)
                    x2+=6;
                final_a = matrix[x1][y1]; final_b = matrix[x2][y1];
            }
            else{
                final_a = matrix[x1][y2]; final_b = matrix[x2][y1];
            }
            final_str= final_str + final_a + final_b;
        }
    }
    return final_str;
}

int main(){
    // initializing the variables to be used for the en/deciphering algorithm
    map <char, bool> alphanumerics;
    map <char, vector<int>> positions;
    vector <char> character_ordering;

    for(int i=97; i<=122; i++){
        char temp = i;
        alphanumerics[temp]=false;
        positions[temp];
    }

    for(int i=48; i<=57; i++){
        char temp = i;
        alphanumerics[temp] = false;
        positions[temp];
    }

    // inintializing the 6x6 playfair cipher matrix
    char** matrix = (char**)malloc(6*sizeof(char*));
    for(int i=0; i<6; i++){
        matrix[i] = (char*)malloc(6*sizeof(char));
    }

    cout << "\nEncryption & Decryption using 6x6 Playfair Cipher\n";
    int choice;
    while(true){
        bool encrypt = true; 
        cout << "\nWhat do you want to do?\n";
        cout << "1. Encrypt a message\n";
        cout << "2. Decrypt a message\n";
        cout << "3. Exit\n";
        cout << "Enter your choice number: "; cin >> choice;

        if(choice==3){
            break;
        }
        else if(choice==2){
            encrypt=false;
        }

        if(choice!=1 && choice!=2 && choice!=3){
            cout << "\nSelect valid option only!\n"; 
            continue;
        }
        else{

            string message; 
            cout << "\nEnter the message: "; 
            getline(cin>>ws,message);

            // Receiving the key to be used for conversion and extracting the unique characters from the key
            string key;
            cout << "Enter the key: "; cin >> key;

            for(int i=0; i<key.length(); i++){
                int temp = key[i];
                if(temp>=48 && temp<-57){
                    if(!alphanumerics[key[i]]){
                        alphanumerics[key[i]] = true;
                        character_ordering.push_back(key[i]);
                    } 
                }
                else if (temp>65 && temp<=90){
                    char c = temp+32;
                    if(!alphanumerics[c]){
                        alphanumerics[c] = true;
                        character_ordering.push_back(c);
                    } 
                }
                else{
                    if(!alphanumerics[key[i]]){
                        alphanumerics[key[i]] = true;
                        character_ordering.push_back(key[i]);
                    }
                }
            }

            // filling the matrix
            for(int i=97; i<=122; i++){
                char temp = i;
                if(!alphanumerics[temp]){
                    character_ordering.push_back(temp);
                }
            }

            for(int i=48; i<=57; i++){
                char temp = i;
                if(!alphanumerics[temp]){
                    character_ordering.push_back(temp);
                }
            }

            int index = 0;
            for(int i=0; i<6; i++){
                for(int j=0; j<6; j++){
                    matrix[i][j] = character_ordering[index];
                    positions[character_ordering[index]].push_back(i);
                    positions[character_ordering[index++]].push_back(j);
                }
            }

            // converting the string into lower case
            for(int i=0; i<message.length(); i++){
                int temp = message[i];
                if(temp>=65 && temp<=90){
                    char c = temp+32;
                    message[i] = c;
                }
            }

            if(encrypt){
                cout << "Encrypted message: " << encrypt_message(matrix, positions, message) << endl;
            }
            else{
                cout << "Decrypted message: " << decrypt_message(matrix, positions, message) << endl;
            }
        }
    }
}