import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;

import java.util.Arrays;


public class ExampleTest {

    private Add add;
    private Subtract subtract;
    private Multiply multiply;

    @Test
    public void AddPositive() {
        add = new Add();
        int result = add.add(2, 2);
        Assert.assertEquals(4,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void AddFail() {
        add = new Add();
        int result = add.add(2, 2);
        Assert.assertEquals(0,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void AddPositiveArray() {
        add = new Add();
        int[] results = {add.add(2, 2),add.add(3, 3)};
        Assert.assertArrayEquals(results,new int[] {4,6});
        System.out.println("APA :" + Arrays.toString(results));
    }

    @Test
    public void AddNegative(){
        add = new Add();
        int result = add.add(2, 2);
        Assert.assertNotEquals(5,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void SubPositive(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        Assert.assertEquals(2,result);
        System.out.println("SP :" + result);
    }

    @Test
    public void SubFail(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        Assert.assertEquals(0,result);
        System.out.println("SP :" + result);
    }

    @Test
    public void SubPositiveArray(){
        subtract = new Subtract();
        int[] results = {subtract.subtract(4, 2), subtract.subtract(6, 3)};
        Assert.assertArrayEquals(results,new int[] {2,3});
        System.out.println("SPA :" + Arrays.toString(results));
    }

    @Test
    public void SubNegative(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        Assert.assertNotEquals(4,result);
        System.out.println("SN :" + result);
    }

    @Test
    public void MulPositive(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        Assert.assertEquals(8,result);
        System.out.println("MP :" + result);
    }

    @Test
    public void MulFail(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        Assert.assertEquals(0,result);
        System.out.println("MP :" + result);
    }

    @Test
    public void MulPositiveArray(){
        multiply = new Multiply();
        int[] results = {multiply.multiply(4, 2), multiply.multiply(6, 3)};
        Assert.assertArrayEquals(results,new int[] {8,18});
        System.out.println("MPA :" + Arrays.toString(results));
    }

    @Test
    public void MulNegative(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        Assert.assertNotEquals(9,result);
        System.out.println("MN :" + result);
    }
}
