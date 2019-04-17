class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int len = A.size();
        int res[len];
        int left = 0;
        int right = len-1;
        for(int i = 0; i < len ; i++){
            if(A[i] % 2 == 0){
                res[left] = A[i];
                left++;
            }else{
                res[right] = A[i];
                right--;
            }
        }
    vector<int> v_res = vector<int>(res, res+len);
    return v_res;
    }

};