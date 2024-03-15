    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]
        if old_color == color:
            return image
        
        stack = [(sr, sc)]
        
        while stack:
            row, col = stack.pop()
            image[row][col] = color
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]) and image[new_row][new_col] == old_color:
                    stack.append((new_row, new_col))
        
        return image
