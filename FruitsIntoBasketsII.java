class FruitsIntoBasketsII {
    public static int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int count=baskets.length;
        for(int i=0;i<fruits.length;i++){
            int f=fruits[i];
            for(int j=0;j<baskets.length;j++){
                if(baskets[j]>=0 && baskets[j]>=f){
                    baskets[j]=-1*f;
                    count--;
                    break;
                }
            }
        }
        return count;
    }
    public static void main(String[] args){
        int[] fruits={4,2,5};
        int[] baskets={3,5,4};
        System.out.println("Number of fruit types that remain unplaced : "+numOfUnplacedFruits(fruits,baskets));
    }
}