import numpy as np

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
    path=[start]
    visited={start: None}
    
    node = start
    startIndex = 0
    
    while True:
        isExistNextNode = False

        for nextNode in range(startIndex, len(matrix[node])):
            # Nếu node có đỉnh kề
            if matrix[node][nextNode] != 0:
                # Kiểm tra xem đỉnh mới có trong path chưa?
                isVisited = False
                for i in path:
                    if i == nextNode:
                        isVisited = True
                        break
                if isVisited:
                    continue
                    
                # Thêm vào trong visited và path
                visited[nextNode] = node
                path.append(nextNode)
                startIndex = 0
                
                # Nếu nextNode là đỉnh kết thúc thì kết thúc
                if nextNode == end:
                    return visited, path
                
                # Nếu chưa phải là đỉnh kết thúc
                node = nextNode
                isExistNextNode = True
                
                break
        
        # Nếu đỉnh node không có các đỉnh kề ta quay lui
        if isExistNextNode == False:
            temp = visited[node]
            del visited[node]
            
            startIndex = node + 1
            node = temp
            path.pop()
            
        if node == None:
            break
            
    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    
    openNode = [(start, None)]
    close = {}
    
    # Lưu các đỉnh đã duyệt qua
    visitedNode = [start]
    
    while True:
        # Nếu hàng đợi openNode không rỗng thì lấy phần tử đầu tiên trong hàng đợi đưa vào trong close
        if openNode != []:
            node, preNode = openNode.pop(0)
            close[node] = preNode
        else:
            return {}, []
        
        for nextNode in range(len(matrix[node])):
            # Khi đỉnh node kề với đỉnh nextNode
            if matrix[node][nextNode] != 0:
                # Kiểm tra có phải là đỉnh kết thúc hay không?
                if nextNode == end:
                    path.append(nextNode)
                    path.append(node)
                    
                    temp = node
                    
                    # Quy lui để xác định path
                    while True:
                        temp = close[temp]
                        if temp:
                            path.append(temp)
                        else:
                            path.reverse()
                            break
                            
                    # Xây dựng visited
                    for i in path:
                        if i == end:
                            visited[i] = node
                        else:
                            visited[i] = close[i]
                    return visited, path
                
                # Kiểm tra đỉnh này có duyệt qua hay chưa. 
                # Nếu đã duyệt qua rồi thì bỏ qua
                # Nếu chưa thì thêm vào trong openNode
                try:
                    visitedNode.index(nextNode)
                except:
                    openNode.append((nextNode, node))
                    visitedNode.append(nextNode)

   
    return visited, path

#Lấy thuộc tính chi phí từ start đến node (Sử dụng trong hàm sort)
def takeDistance(item):
    return item[2]

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    
    openNode = [(start, None, 0)]
    closeNode = {}
    
    while True:
        if openNode != []:
            # w: chi phí đi từ start đến node
            node, preNode, w = openNode.pop(0)
            closeNode[node] = preNode
            
            # Nếu node là đỉnh kết thúc
            if node == end:
                temp = node
                while temp is not None:
                    path.append(temp)
                    
                    visited[temp] = closeNode[temp]
                    temp = visited[temp]
                return visited, path

            
            for nextNode in range(len(matrix[node])):
                if matrix[node][nextNode] != 0:
                    # Kiểm tra đỉnh nextNode đã xét hay chưa. Nếu rồi thì bỏ qua
                    if nextNode in closeNode:
                        continue
                    
                    # Kiểm tra đỉnh nextNode đã mở hay chưa.
                    # Nếu đã mở rồi thì cập nhật lạ chi phí w (Nếu nhỏ hơn)
                    opened = False
                    
                    for temp in openNode:
                        if temp[0] == nextNode:
                            if temp[2] > w + matrix[node][nextNode]:
                                openNode.remove(temp)
                                openNode.append((nextNode, node, w + matrix[node][nextNode]))
                            
                            opened = True
                            break
                    if opened:
                        continue
                            
                    # Nếu chưa có trong openNode và closeNode thì thêm vòa openNode
                    openNode.append((nextNode, node, w + matrix[node][nextNode]))
                    
            # Sắp xếp lại openNode theo thứ tự chi phí tăng dần
            openNode.sort(key = takeDistance)

        else:
            return {}, []

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[start]
    visited={start: None}
    node = start
    minWeight = 1
    
    while True:
        nextMinNode = None
        h = 0
        
        for nextNode in range(len(matrix[node])):
            if matrix[node][nextNode] >= minWeight:
                # Nếu đỉnh nextNode đã đi qua thì bỏ qua.
                if nextNode in visited:
                    continue
                    
                if nextMinNode is None:
                    h = matrix[node][nextNode]
                    nextMinNode = nextNode
                else:
                    if h > matrix[node][nextNode]:
                        h = matrix[node][nextNode]
                        nextMinNode = nextNode
                        
        if nextMinNode is not None:
            path.append(nextMinNode)
            visited[nextMinNode] = node
            
            if nextMinNode == end:
                return visited, path
            else:
                node = nextMinNode
                minWeight = 1
                
        else:
            temp = visited[node]
            
            if temp is None:
                return {}, []
            
            path.remove(node)
            del visited[node]
            
            minWeight = matrix[temp][node] + 1 
            node = temp
    return visited, path

# Hàm ước tính chi phí
def eclidean_distance(currentVertex, Goal):
    return (currentVertex[0] - Goal[0])**2 + (currentVertex[1] - Goal[1])**2

# Hàm lấy f trong các phần tử của openNode (dùng trong hàm sort)
def takeF(item):
    return item[3]  

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    
    # Mỗi phần tử trong openNode có cấu trúc: node, preNode, g, f
    # node: đỉnh đang xét
    # preNode: đỉnh cha của node
    # g: chi phí từ đỉnh start đến node
    # f: giá trị đánh giá: f = g + h (h là hàm dự đoán chi phí từ node đến đỉnh end)
    
    openNode = [(start, None, 0, eclidean_distance(pos[start], pos[end]))]
    closeNode = {}
    
    while openNode != []:
        node, preNode, g, f_node = openNode.pop(0)
        closeNode[node] = (preNode, g)
        
        print("\t open: ", openNode)
        print("\t close: ", closeNode)
        
        if node == end:
            path.append(end)
            visited[end] = preNode
            
            temp = preNode
            
            while temp is not None:
                path.append(temp)
                visited[temp] = closeNode[temp][0]
                temp = closeNode[temp][0]
            path.reverse()
            
            
            return visited, path
        
        for nextNode in range(len(matrix[node])):
            if matrix[node][nextNode] != 0:
                cost = g + matrix[node][nextNode]
                f = cost + eclidean_distance(pos[nextNode], pos[end])
                # Kiểm tra đỉnh nextNode đã xét chưa (có trong closeNode chưa)
                # Nếu nextNode đã có trong closeNode và: g(nextNode) > g(node) + matrix[node][nextNode]
                # thì loại đỉnh nextNode ra khỏi closeNode và đưa vào openNode
                if nextNode in closeNode:
                    
                    if closeNode[nextNode][1] > cost:
                        del closeNode[nextNode]
                        openNode.append((nextNode, node, cost, f))
                else:
                    # Kiểm tra đỉnh nextNode đã duyệt chưa (có trong openNode chưa)
                    # Nếu nextNode đã có trong openNode và: g(nextNode) > g(node) + matrix[node][nextNode]
                    # thì cập nhật lại đỉnh nextNode
                    for i in openNode:
                        if i[0] == nextNode:
                            if i[2] > cost:
                                openNode.remove(i)
                                openNode.append((nextNode, node, cost, f))

                            break
                    # Khi nextNode không có trong closeNode và openNode
                    # Thêm nextNod3 vào openNode
                    else:
                        openNode.append((nextNode, node, cost, f))
                
        # Sắp xếp openNode theo thứ tự tăng dần của f        
        openNode.sort(key = takeF)  
        print("Sau khi sắp xếp: ", openNode)
                
    return visited, path
