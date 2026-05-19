class Solution {
public:

    void backtrack(vector<vector<int>>& ans, vector<int>& nums,vector<int>& u2 , int u2trash, int i){
        if(i>=nums.size()){
            return;
        }
        if(u2trash==0){
        ans.push_back(u2);
        return;}
        else if(u2trash<0){
        return;
        }
        u2.push_back(nums[i]);
        backtrack(ans,nums, u2, u2trash-nums[i], i);
        u2.pop_back();

        backtrack(ans, nums, u2, u2trash, i+1);

        return;

}

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        
        vector<vector<int>> ans={};
        vector<int> u2;

        backtrack(ans, nums,u2, target, 0);
        return ans;
    }
};
