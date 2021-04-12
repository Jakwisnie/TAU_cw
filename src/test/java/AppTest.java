
import static org.junit.Assert.*;
import org.junit.*;
import org.junit.jupiter.api.Disabled;

public class AppTest {
    private App app;

    @Before
    public void setUP(){
        app = new App();
        System.out.println("before");

    }

    @After
    public void tearDown(){
        app = null;
        System.out.println("after");
    }

    @Test
    public void test1(){
        int result = app.NWD(4,2);
        assertEquals(2,result);
        System.out.println("Test1");
    }
    @Test
    public void test2(){
        int result = app.NWD(40,20);
        assertEquals(20,result);
        System.out.println("Test2");
    }
    @Test
    @Disabled("nie ma")
    public void test3(){
        int result = app.NWD(4,2);
        assertEquals(2,result);
        System.out.println("Test3");
    }
    @Test
    public void test4(){
        int result = app.NWD(4,2);
        assertEquals(5,result);
        fail("a failing test");
        System.out.println("Test4");
    }
    @Test
    public void test5(){
        int result = app.NWD(12,2);
        assertEquals(2,result);
        System.out.println("Test5");
    }
    @Test
    public void test6(){
        int result = app.NWD(20,2);
        assertEquals(2,result);
        System.out.println("Test6");
    } @Test
    public void test7(){
        int result = app.NWD(400000,2);
        assertEquals(2,result);
        System.out.println("Test7");
    }
    @Test
    public void test8(){
        int result = app.NWD(22,2);
        assertEquals(1,result);
        fail("a failing test");
        System.out.println("Test8");
    }
    @Test
    @Disabled("nie ma")
    public void test9(){
        int result = app.NWD(4,2);
        assertEquals(2,result);
        System.out.println("Test9");
    }
    @Test
    public void test10(){
        int result = app.NWD(14,7);
        assertEquals(7,result);
        System.out.println("Test10");
    }
    @Test
    public void test11(){
        String result = app.echo("luzik",3);
        assertEquals("luzikluzikluzik",result);
        System.out.println("Test11");
    }
    @Test
    public void test12(){
        String result = app.echo("luzik",5);
        assertEquals("luzikluzikluzikluzikluzik",result);
        System.out.println("Test12");
    }
    @Test
    public void test13(){
        String result = app.echo("luzik",4);
        assertEquals("luzikluzikluzikluzik",result);
        System.out.println("Test13");
    }
    @Test
    public void test14(){
        String result = app.echo("luzik",0);
        assertEquals(null,result);
        System.out.println("Test14");
    }
    @Test
    public void test15(){
        String result = app.setZmienna2( );
        assertEquals(null,result);
        System.out.println("Test14");
    }
    @Test
    public void test16(){
        String result = app.setZmienna1("luzik");
        assertEquals(null,result);
        System.out.println("Test14");
    }



}
