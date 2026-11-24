class Solution {
public:
    bool isPalindrome(string s) {
        string str = "";
        for(const char& c : s){
            if(isalnum(c)){
                str += tolower(c);
            }
        }
        return str == string(str.rbegin(), str.rend()); 
    }
};
