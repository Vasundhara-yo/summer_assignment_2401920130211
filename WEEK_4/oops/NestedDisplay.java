class Outer {
    void display() {
        System.out.println("Inside Outer display");
    }

    class Inner {
        void display() {
            System.out.println("Inside Inner display");
        }
    }
}

public class NestedDisplay {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.display();
        
        Outer.Inner inner = outer.new Inner();
        inner.display();
    }
}
