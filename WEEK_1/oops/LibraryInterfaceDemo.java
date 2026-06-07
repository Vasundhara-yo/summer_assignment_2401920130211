public class LibraryInterfaceDemo {
    public static void main(String[] args) {

        System.out.println("--- KidUser Tests ---");
        KidUsers kid1 = new KidUsers(10, "Kids");
        kid1.registerAccount();
        kid1.requestBook();

        KidUsers kid2 = new KidUsers(18, "Fiction");
        kid2.registerAccount();
        kid2.requestBook();

        System.out.println("\n--- AdultUser Tests ---");
        AdultUser adult1 = new AdultUser(25, "Fiction");
        adult1.registerAccount();
        adult1.requestBook();

        AdultUser adult2 = new AdultUser(10, "Kids");
        adult2.registerAccount();
        adult2.requestBook();
    }
}
