import ApacheCollections.Customer;
import MockClasses.Class1;
import MockClasses.Class2;
import org.apache.commons.collections4.CollectionUtils;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static org.junit.Assert.*;
import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;


public class ExampleTest {

    private Add add;
    private Subtract subtract;
    private Multiply multiply;
    private Divide divide;
    private Time time;

    private int getNumber;
    private boolean isFalse;

    @Test
    public void MockTest() {

        Class1 class1 = new Class1();
        getNumber = class1.getNumber();
        assertEquals(42,getNumber);

    }

    @Test
    public void MockTest2() {

        Class1 class1 = mock(Class1.class);
        isFalse = class1.isFalse();
        assertEquals(false, isFalse);

    }


    @Test
    public void MockWhen() {

        Class1 class1 = mock(Class1.class);

        when(class1.getNumber()).thenReturn(52);

        getNumber = class1.getNumber();
        assertEquals(52, getNumber);

    }

    @Test
    public void MockWhen2(){

        Class1 class1 = mock(Class1.class);

        when(class1.isFalse()).thenReturn(true);

        Class2 class2 = new Class2(class1);

        assertEquals(class2.toString2(),"Bool : true");

    }

    @Test
    public void MockWhen3(){

        Class1 class1 = mock(Class1.class);

        when(class1.getNumber()).thenReturn(52);

        Class2 class2 = new Class2(class1);

        assertEquals(class2.toString(),"Number : 52");

    }


    @Test
    public void MockGiven() {

        Class1 class1 = mock(Class1.class);

        given(class1.getNumber()).willReturn(52);

        getNumber = class1.getNumber();
        assertEquals(52, getNumber);

    }

    @Test
    public void MockGiven2(){

        Class1 class1 = mock(Class1.class);

        given(class1.getNumber()).willReturn(52);

        Class2 class2 = new Class2(class1);

        assertEquals(class2.toString(),"Number : 52");

    }

    @Test
    public void MockGiven3() {

        Class1 class1 = mock(Class1.class);

        given(class1.isFalse()).willReturn(true);

        isFalse = class1.isFalse();
        assertEquals(true, isFalse);

    }


    @Test
    public void AddPositive() {
        add = new Add();
        int result = add.add(2, 2);
        assertEquals(4,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void AddFail() {
        add = new Add();
        int result = add.add(2, 2);
        assertEquals(0,result);
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
        assertEquals(2,result);
        System.out.println("SP :" + result);
    }

    @Test
    public void SubFail(){
        subtract = new Subtract();
        int result = subtract.subtract(4,2);
        assertEquals(0,result);
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
        assertEquals(8,result);
        System.out.println("MP :" + result);
    }

    @Test
    public void MulFail(){
        multiply = new Multiply();
        int result = multiply.multiply(2,4);
        assertEquals(0,result);
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

    @Test
    public void DivPositive() {
        divide = new Divide();
        int result = divide.divide(2, 2);
        assertEquals(1,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void DivFail() {
        divide = new Divide();
        int result = divide.divide(2, 2);
        assertEquals(0,result);
        System.out.println("AP :" + result);
    }

    @Test
    public void DivPositiveArray() {
        divide = new Divide();
        int[] results = {divide.divide(2, 2),divide.divide(4, 2)};
        Assert.assertArrayEquals(results,new int[] {1,2});
        System.out.println("APA :" + Arrays.toString(results));
    }

    @Test
    public void DivNegative(){
        divide = new Divide();
        int result = divide.divide(2, 2);
        Assert.assertNotEquals(5,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void DivZero(){
        divide = new Divide();
        int result = divide.divide(2, 0);
        assertEquals(-1,result);
        System.out.println("AN :" + result);
    }

    @Test
    public void ActualDate(){
        // funkcja korzysta z Joda-Time porownuje wynik z wbudowanym java.time

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        LocalDateTime now = LocalDateTime.now();

        time = new Time();
        String result = time.ActualDate();

        assertEquals(dtf.format(now),result);
        System.out.println("T :" + result);
    }

    Customer customer1 = new Customer(1, "Daniel", "locality1", "city1");
    Customer customer2 = new Customer(2, "Fredrik", "locality2", "city2");
    Customer customer3 = new Customer(3, "Kyle", "locality3", "city3");
    Customer customer4 = new Customer(4, "Bob", "locality4", "city4");
    Customer customer5 = new Customer(5, "Cat", "locality5", "city5");
    Customer customer6 = new Customer(6, "John", "locality6", "city6");

    List<Customer> list1 = Arrays.asList(customer1, customer2, customer3);
    List<Customer> list2 = Arrays.asList(customer4, customer5, customer6);
    List<Customer> list3 = Arrays.asList(customer1, customer2);

    @Test
    public void NoNullAdded() {
        CollectionUtils.addIgnoreNull(list1, null);

        assertFalse(list1.contains(null));
    }

    @Test
    public void IsNotEmpty() {
        assertTrue(CollectionUtils.isNotEmpty(list2));
    }

    @Test
    public void ElementNotPresent() {
        Collection<Customer> result = CollectionUtils.subtract(list1, list3);
        assertFalse(result.contains(customer1));
    }

}
