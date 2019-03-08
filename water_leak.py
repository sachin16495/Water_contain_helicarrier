import heapq
import numpy as np
def WaterStoredInPlatform(platform):
    print("Input")
    print(platform)
    m,n = platform.shape
    if m == 0:
        return 0
    if n == 0:
        return 0

    visited = [[0] * n for _ in range(m)]
    water = 0
    # It responsible for heap storage
    min_height_lookup = []

    # Traverse the input arry from corners
    for row in range(m):
        for column in range(n):

            if (row == 0 or column == 0 or row == m - 1 or column == n - 1):
                # Mark the entry as having been visited
               
                visited[row][column] = 1
                heapq.heappush(min_height_lookup, (platform[row,column], row, column))
                # Push the height along with the row, column indices on to the heap
                
    # Traverse over the heap and  check the neighbors of the minimum height elements 
    # Thus, we start at the boundary of the matrix and keep going into the inner layers
    waters=[]
    while min_height_lookup:
        min_height, min_row, min_column = heapq.heappop(min_height_lookup)
        # Check the neighbors of each element

        for r, c in ((min_row + 1, min_column), (min_row - 1, min_column), (min_row, min_column + 1), (min_row, min_column - 1)):
            if 0 <= r <= m - 1 and 0 <= c <= n - 1 and not visited[r][c]:
            
                # If the neighbor is of lesser height than that of the current element,
                # water will collect there. Else it will flow away.
                # For each neighbor, the water level will be equal to the difference between the heights
                # Check if neighbour is zero then pop the waters from list
                if r>=0 and c>=0:
                    if platform[r,c]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        # Store the taller of the heights betwen the current element and the neighbor on the heap
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                
                        # Mark the neighbor as having been visited
                        visited[r][c] = 1

                elif r+1<m and c<n and c>=0:
                    if platform[r+1,c]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1
                elif r-1<m and c<n and c>=0 and r>=0:
                    if platform[r-1,c]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1

                elif r<m and c+1<n and  r>0:
                    if platform[r,c+1]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1
                elif r<m and c-1<n and  c>=0 and r>=0:
                    if platform[r,c+1]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1
                elif r-1<m and c-1<n and  c>=0 and r>=0:
                    if platform[r-1,c-1]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1
               elif r+1<m and c+1<n and  c>=0 and r>=0:
                    if platform[r+1,c+1]==0:
                        waters.pop()
                        continue
                    else:
                        water += max(0, min_height - platform[r,c])
                        waters.append(water)
                        new_height = max(min_height, platform[r,c])
                        heapq.heappush(min_height_lookup, (new_height, r, c))
                        visited[r][c] = 1
                
                
    #print(waters)            
    return waters.pop()

platform1=np.array([[2,2,2],[2,2,2],[2,2,2]])
print("Water Hold by Platform 1")
print("Storage")
print(WaterStoredInPlatform(platform1))
print("Water Hold by Platform 2")
print("Storage")
platform2=np.array([[2,2,2,2],[2,1,2,1],[2,2,2,1]])
print(WaterStoredInPlatform(platform2))
print("Water Hold by Platform 3")
platform3=np.array([[3,3,3,3,3,3],[3,1,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])
print("Storage")
print(WaterStoredInPlatform(platform3))
print("Water Hold by Platform 4")
platform4=np.array([[3,3,3,3,5,3],[3,0,2,3,1,3],[3,1,2,3,1,3],[3,3,3,1,3,3]])
print("Storage")
print(WaterStoredInPlatform(platform4))
print("Water Hold by Platform 5")
platform5=np.array([[ 5 , 5 , 5 , 5 , 5],[ 9 , 1 , 1 , 1 , 5],[ 5 , 1 , 5 , 1 , 5],[ 5 , 1 , 1 , 1 , 5],[ 5 , 5 , 5 , 5 , 5]])
print("Storage")
print(WaterStoredInPlatform(platform5))

