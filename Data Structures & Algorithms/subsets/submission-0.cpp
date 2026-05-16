class Solution {
public:
    void backtrack(vector<int>& nums, int start, vector<int> arr, vector<vector<int>>& res){
        if(start>=nums.size()){
            res.push_back(arr);
            return;
        }
        arr.push_back(nums[start]);
        backtrack(nums, start+1, arr, res);

        arr.pop_back();
        backtrack(nums, start+1, arr, res);
}

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res={};
        vector<int> arr={};
        int start=0;

        backtrack(nums, 0, arr, res);

        return res;



    }
};
