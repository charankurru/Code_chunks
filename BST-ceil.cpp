int floorInBST(TreeNode<int> *root, int key)
{
    int floor = -1;
    while (root)
    {

        if (root->val == key)
        {
            floor = root->val;
            return floor;
        }

        if (key > root->val)
        {
            root = root->right;
        }
        else
        {
            floor = root->val;
            root = root->left;
        }
    }
    return floor;
}
