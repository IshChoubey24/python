int getMin(string s) {
    int res = 0, left = 0;
    for (char &c: s) {
        if (c == '(') {
            left++;
        } else {
            if (left > 0) {
                left--;
            } else {
                res++;
            }
        }
    }
    return res + left;
}