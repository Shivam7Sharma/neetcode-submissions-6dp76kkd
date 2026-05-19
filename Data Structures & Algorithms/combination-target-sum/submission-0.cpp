class Solution {
public:

    void backtrack(vector<vector<int>>& ans, vector<int>& nums,vector<int> u2 , int &target, int i){
        if(i>=nums.size()){
            return;
        }
        int sum=0;
        for(int j=0; j<u2.size(); j++){
            sum+=u2[j];
        }
        if(sum==target){
        ans.push_back(u2);
        return;}
        else if(sum>target){
        return;
        }
        u2.push_back(nums[i]);
        backtrack(ans,nums, u2, target, i);
        u2.pop_back();

        backtrack(ans, nums, u2, target, i+1);

        return;

}

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        
        vector<vector<int>> ans={};
        vector<int> u2={};

        backtrack(ans, nums, u2, target, 0);
        return ans;
    }
};
