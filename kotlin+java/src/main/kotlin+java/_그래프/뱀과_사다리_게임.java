package _그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 뱀과_사다리_게임 {

    static int n;
    static int m;
    static Map<Integer, Integer> map = new HashMap<>();
    static boolean[] visited = new boolean[101];

    static class Info {
        int cnt;
        int idx;

        public Info(int cnt, int idx) {
            this.cnt = cnt;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n + m; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        System.out.println(bfs());
    }

    public static int bfs() {
        Queue<Info> queue = new LinkedList<>();
        queue.offer(new Info(0, 1));

        while (!queue.isEmpty()) {
            Info info = queue.poll();

            for (int i = 1; i <= 6; i++) {
                int cur = info.idx + i;

                if (cur == 100) {
                    return info.cnt + 1;
                }

                if (cur > 100) {
                    continue;
                }

                if (visited[cur]) {
                    continue;
                }
                Integer num = map.getOrDefault(cur, 0);

                if (num == 0) {
                    queue.offer(new Info(info.cnt + 1, cur));
                    visited[cur] = true;
                } else {
                    queue.offer(new Info(info.cnt + 1, num));
                    visited[num] = true;
                }
            }
        }
        return -1;
    }
}
