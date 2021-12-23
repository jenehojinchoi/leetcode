// 98. Validate Binary Search Tree

var isValidBST = function(root, left=Number.NEGATIVE_INFINITY, right=Number.POSITIVE_INFINITY) {
    if (!root) {
        return true;
    } 
    if (root.val <= left || root.val >= right) {
        return false;
    }
    return isValidBST(root.left, left, Math.min(right, root.val)) && isValidBST(root.right, Math.max(left, root.val), right)
};

/*
Runtime: 68 ms, faster than 99.52% of JavaScript online submissions for Validate Binary Search Tree.
Memory Usage: 43.4 MB, less than 30.77% of JavaScript online submissions for Validate Binary Search Tree.
*/