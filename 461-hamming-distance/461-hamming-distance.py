class Solution {
public:
    int hammingDistance(int x, int y) {
        int res = x^y;
        int count = 0;
        while(res != 0){
            if(res&0x01){
                count += 1;
            }
            res = res >> 1;
        }
        return count;
    }
};