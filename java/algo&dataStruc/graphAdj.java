import java.util.*;

public class graphAdj {
    private int[][] adjMatrix;
    private int n;

    public graphAdj(int n) {
        this.n = n;
        adjMatrix = new int[n][n];
        for (int i = 0; i < adjMatrix.length; i++) {
            for (int j = 0; j < adjMatrix.length; j++) {
                adjMatrix[i][j] = 0;
            }
        }
    }

    public void addEdge(int u, int v, int w) {
        adjMatrix[u][v] = w;
    }

    public void bfs(int start) {
        System.out.println("BFS: ");
        boolean[] visited = new boolean[this.n];
        visited[start] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        int step = 0;
        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            for (int i = 0; i < this.n; i++) {
                if (adjMatrix[currentNode][i] != 0 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
            System.out.println(++step + ": " + currentNode);
        }

        System.out.println();
    }

    public void dfs(int start) {
        System.out.println("DFS: ");
        boolean[] visited = new boolean[this.n];
        visited[start] = true;
        Stack<Integer> stack = new Stack<>();
        stack.add(start);
        int step = 0;
        while (!stack.isEmpty()) {
            int currentNode = stack.pop();
            for (int i = 0; i < this.n; i++) {
                if (adjMatrix[currentNode][i] != 0 && !visited[i]) {
                    stack.add(i);
                    visited[i] = true;
                }
            }
            System.out.println(++step + ": " + currentNode);
        }
    }

    private Stack<Integer> dijkstraHelper(int start, int finish) {
        Stack<Integer> result = new Stack<>();
        boolean[] M = new boolean[this.n];
        Integer[] L = new Integer[this.n];
        int[] parent = new int[this.n];
        for (int i = 0; i < this.n; i++) {
            M[i] = false;
            L[i] = Integer.MAX_VALUE;
            parent[i] = -1;
        }
        L[start] = 0;
        for (int i = 0; i < this.n - 1; i++) {
            int u = -1;
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < this.n; j++) {
                if (!M[j] && L[j] < min) {
                    min = L[j];
                    u = j;
                }
            }
            if (u == -1)
                break;
            M[u] = true;
            for (int v = 0; v < this.n; v++) {
                if (!M[v]
                        && adjMatrix[u][v] != 0
                        && L[u] != Integer.MAX_VALUE
                        && L[u] + adjMatrix[u][v] < L[v]) {

                    L[v] = L[u] + adjMatrix[u][v];
                    parent[v] = u;
                }
            }
        }
        if (L[finish] == Integer.MAX_VALUE) {
            return result;
        }
        for (int at = finish; at != -1; at = parent[at]) {
            result.add(at);
        }
        result.add(L[finish]);
        return result;
    }

    public String dijkstra(int start, int finish) {
        String path = "";
        Stack<Integer> pathPlusWeight = dijkstraHelper(start, finish);
        int weight = pathPlusWeight.pop();
        while (!pathPlusWeight.isEmpty()) {
            Integer currentNode = pathPlusWeight.pop();
            path += String.valueOf(currentNode);
            if (pathPlusWeight.size() != 0) {
                path += " -> ";
            }
        }
        return path + "\nВес пути: " + weight;
    }

}
