class Box {
    double length, breadth;
    Box(double l, double b) { this.length = l; this.breadth = b; }
    double getArea() { return length * breadth; }
}

class Box3D extends Box {
    double height;
    Box3D(double l, double b, double h) { super(l, b); this.height = h; }
    double getVolume() { return length * breadth * height; }
}

public class MainBox {
    public static void main(String[] args) {
        Box3D myBox = new Box3D(10, 5, 2);
        System.out.println("Area: " + myBox.getArea());
        System.out.println("Volume: " + myBox.getVolume());
    }
}
