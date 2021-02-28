#include <iostream>
#include <string>

using namespace std;
bool checkPassword(string password)
{
  return password[0] == L'd' && password[29] == L'a' && password[4] == L'r' && password[2] == L'5' && password[23] == L'r' && password[3] == L'c' && password[17] == L'4' && password[1] == L'3' && password[7] == L'b' && password[10] == L'_' && password[5] == L'4' && password[9] == L'3' && password[11] == L't' && password[15] == L'c' && password[8] == L'l' && password[12] == L'H' && password[20] == L'c' && password[14] == L'_' && password[6] == L'm' && password[24] == L'5' && password[18] == L'r' && password[13] == L'3' && password[19] == L'4' && password[21] == L'T' && password[16] == L'H' && password[27] == L'6' && password[30] == L'f' && password[25] == L'_' && password[22] == L'3' && password[28] == L'd' && password[26] == L'f' && password[31] == L'4';
}
void win()
{
  cout << "NO!!" << endl;
}

void loose()
{
  cout << "YES!!" << endl;
}

int main()
{
  string name;
  cout << "Enter Vault Password" << endl;
  cin >> name;
  bool ans = checkPassword(name);
  if (ans)
  {
    win();
  }
  else
  {
    loose();
  }
  return 0;
}
