height = int(input("Enter the number of height in tree: "))
branch = int(input("Enter the number of branch in node: "))

def total_nodes(height, branch):
    height = height+ 1
    total_nodes = 0
    for i in range(height):
        total_nodes += branch ** i
    return total_nodes
total_node = total_nodes(height, branch)


nodes = [i for i in range(1, total_node+1)]
def tree(nodes, branch):
    tree = {}
    pointer = 1
    for i in nodes:
        # for j in range(1,branch+1):
        if pointer < total_node:
            tree[i] = [pointer+j+1 for j in range(branch)]
        else:
            tree[i] = []
        for j in range(1, branch+1):
            pointer += 1
    return tree

tree_ = tree(nodes, branch)
print(tree_)

def dfs(tree, start, end):
    stack = []
    stack.append(start)
    visited = []
    path = []
    path.append(start)
    pointer = start
    while pointer != end:
        print(stack)
        if tree[pointer]:  
            pointer = tree[pointer][0]
            stack.append(pointer)
            path.append(pointer)
        else:
            stack.pop()
            tree[stack[-1]].pop(0) 
            pointer = stack[-1]
            path.append(pointer)
    return path


print(dfs(tree_, 1, 5))
    
    








        

        

    
        
        




            
        





    






            

        




        
    



        
    

    
        



    
