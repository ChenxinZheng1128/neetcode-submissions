class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        for (const string& s : strs) {
            encodedString  += to_string(s.length()) + "#" + s;
        }
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> decodedString;
        int i = 0;

        while (i < s.length()) {
            int j = s.find('#', i);
            int length = stoi(s.substr(i, j - i));

            decodedString.push_back(s.substr(j + 1, length));

            i = j + 1 + length;
        }
        
        return decodedString;
    }
};
