#include <string>

using namespace std;

string DNAStrand(const std::string& dna)
{
  string s;
  //your code here
  for (int i = 0 ; i < dna.length() ; i++){
    if (dna[i] == 'A') {
      s += 'T';
    }
    if (dna[i] == 'T') {
      s += 'A';
    }
    if (dna[i] == 'G') {
      s += 'C';
    }
    if (dna[i] == 'C') {
      s += 'G';
    }
    else
      continue;
  }
  return s;
}