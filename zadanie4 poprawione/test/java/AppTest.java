
import static org.junit.Assert.*;
import static org.mockito.Mockito.when;
import static org.mockito.BDDMockito.*;


import org.junit.*;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class AppTest {
    @Mock
    private App app;
    @InjectMocks
    private int kolejnosc = 0;

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
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(2,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test2(){
        int result = app.NWD(40,20);
        given(result).willReturn(20);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(20,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    @Disabled("nie ma")
    public void test3(){
        int result = app.NWD(4,2);
        given(result).willReturn(2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(2,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test4(){
        int result = app.NWD(4,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(5,result);
        fail("a failing test");
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test5(){
        int result = app.NWD(12,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(2,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test6(){
        int result = app.NWD(20,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    } @Test
    public void test7(){
        int result = app.NWD(400000,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(2,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test8(){
        int result = app.NWD(22,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(1,result);
        fail("a failing test");
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    @Disabled("nie ma")
    public void test9(){
        int result = app.NWD(4,2);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals(2,result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test10(){
        int result = app.NWD(14,7);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test11(){
        String result = app.echo("siemka ",5);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka siemka siemka siemka siemka siemka ",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test12(){
        String result = app.echo("siemka ",12);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test13(){
        String result = app.echo("siemka ",6);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka siemka siemka siemka siemka siemka siemka ",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test14(){
        String result = app.echo("siemka ",1);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka siemka ",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test15(){
        String result = app.echo("siemka ",3);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka siemka siemka siemka ",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test16(){
        String result = app.echo("siemka ",5);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test17(){
        String result = app.echo("siemka ",4);
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka siemka siemka siemka siemka ",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test18(){
        String result = app.nazwa("siemka ","szkanka");
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka szklanka",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test19(){
        String result = app.nazwa("siemka ","lanka");
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertEquals("siemka lanka",result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test20(){
        String result = app.nazwa("jola","warka");
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test21(){
        String result = app.nazwa("jola","warka");
        when(kolejnosc == 0).thenThrow(app.blad());
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test22(){
        String result = app.nazwa("jola","warka");
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }
    @Test
    public void test23(){
        String result = app.nazwa("jola","warka");
        when(kolejnosc == 0).thenReturn(Boolean.valueOf("something wrong"));
        when(kolejnosc == 0).thenThrow(app.blad());
        assertNotNull(result);
        kolejnosc = kolejnosc +1;
        System.out.println("Test "+kolejnosc);
    }

}
