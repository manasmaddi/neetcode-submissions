class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> countMap = new HashMap<Integer, Integer>();

        for (int n : nums) {
            countMap.put(n, countMap.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (n1, n2) -> countMap.get(n1) - countMap.get(n2)
        );

        for(int i: countMap.keySet()){
            heap.add(i);
            if(heap.size() > k){
                heap.poll();
            }
        }

        int[] finallist = new int[k];
        for (int i = k - 1; i >= 0; --i) {
            finallist[i] = heap.poll();
        }

        return finallist;


    }
}
