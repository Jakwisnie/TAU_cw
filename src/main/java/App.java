public class App {
    public int a,b;
    public int NWD(int a , int b){
        a = Math.abs(a);
        b = Math.abs(b);

        if(a==0 && b ==0)
            throw new IllegalArgumentException();

        if(a==0)
            return b;

        if(b==0)
            return a;

        while(a !=b){
            if(a >b)
                a -=b;
            else
                b -=a;
        }
        return a;
    }
    public String c;
    public int d;
    public String echo(String c, int d){
        if(d == 0)
        {
            return null;
        }
         String e = c;
            for(int i =2 ;i <=d;i++ ){
                c = c+e;
            }

        return c;
    }
    private zmienna1 zmienna1;
    private zmienna2 zmienna2;

    public void setZmienna1(zmienna1 zmienna1){
        this.zmienna1 = zmienna1;
    }
    public void setZmienna2(zmienna2 zmienna2){
        this.zmienna2 = zmienna2;
    }

}
