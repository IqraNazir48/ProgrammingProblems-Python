class PowerOfThree{
    public static boolean isPowerOfThree(int n) {
        if(n==0){
            return false;
        }
        int power=1;
        for(int i=0;i<=31;i++){
            if(power==n){
                return true;
            }
            power*=3;
        }
        return false;
    }
    public static void main(String[] args){
        int n=27;
        System.out.println(n + " power of Three ? : "+isPowerOfThree(n));
        int n1=-1;
        System.out.println(n1 + " power of Three ? : "+isPowerOfThree(n1));
    }
}