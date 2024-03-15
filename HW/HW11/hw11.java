    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        if (oldColor == newColor) {
            return image;
        }
        
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{sr, sc});
        
        while (!stack.isEmpty()) {
            int[] coordinates = stack.pop();
            int row = coordinates[0];
            int col = coordinates[1];
            image[row][col] = newColor;
            
            int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                if (newRow >= 0 && newRow < image.length && newCol >= 0 && newCol < image[0].length && image[newRow][newCol] == oldColor) {
                    stack.push(new int[]{newRow, newCol});
                }
            }
        }
        
        return image;
    }
