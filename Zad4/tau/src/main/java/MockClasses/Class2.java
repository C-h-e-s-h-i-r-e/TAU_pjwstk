package MockClasses;

public class Class2 {

    private Class1 class1;

    public Class2(Class1 class1) {
        this.class1 = class1;
    }

    @Override
    public String toString() {
        return "Number : " + String.valueOf(class1.getNumber());
    }

    public String toString2() {
        return "Bool : " + String.valueOf(class1.isFalse());
    }

}
