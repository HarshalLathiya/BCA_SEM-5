package product_tab;

import java.sql.*;
import java.util.Scanner;

public class Product_tab {

    public static void main(String[] args) {
        System.out.println("Hello From Product Table:");
        Scanner sc = new Scanner(System.in);
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");

//            Statement st = con.createStatement();
//            String query ="CREATE TABLE product_tab (pid int PRIMARY KEY, productname varchar(100), price double, quantity int)";
//            st.executeUpdate(query);
            
                while (true) {
                System.out.println("\n1.insert\n2.update\n3.delete\n4.select\n5.exit");
                System.out.print("Choose option: ");
                int ch = sc.nextInt();
                sc.nextLine();

                switch (ch) {
                    case 1:
                        String insert = "insert into product_tab values (?,?,?,?)";
                        PreparedStatement pst1 = con.prepareStatement(insert);
                        System.out.print("Enter PID:");
                        int pid = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter product name: ");
                        String pname = sc.nextLine();

                        System.out.print("Enter price: ");
                        double price = sc.nextDouble();

                        System.out.print("Enter quantity: ");
                        int qty = sc.nextInt();

                        pst1.setInt(1, pid);
                        pst1.setString(2, pname);
                        pst1.setDouble(3, price);
                        pst1.setInt(4, qty);
                        pst1.executeUpdate();
                        
                        System.out.println("Product inserted.");
                        break;
                        
                    case 2:
                        String update = "update product_tab set price = ?, quantity = ? where pid = ?";
                        PreparedStatement pst2 = con.prepareStatement(update);
                        
                        System.out.print("Enter pid to update: "); 
                        int upid = sc.nextInt();
                        
                        System.out.print("New price: ");
                        double newPrice = sc.nextDouble();
                        System.out.print("New Quantity: ");
                        int newQty = sc.nextInt();

                        pst2.setDouble(1, newPrice);
                        pst2.setInt(2, newQty);
                        pst2.setInt(3, upid);
                        pst2.executeUpdate();
                        
                        System.out.println("Product updated.");
                        break;
                        
                    case 3:
                        String delete = "delete from product_tab where pid = ?";
                        PreparedStatement pst3 = con.prepareStatement(delete);
                        System.out.print("Enter pid to delete: "); 
                        int delid = sc.nextInt();
                        pst3.setInt(1, delid);
                        pst3.executeUpdate();
                        
                        System.out.println("Product deleted.");
                        break;
                    
                    case 4:
                        Statement st = con.createStatement();
                        ResultSet rs = st.executeQuery("select * from product_tab");
                        while (rs.next()) {
                            System.out.println(rs.getInt("pid") + " : " + rs.getString("productname") + " : ₹" + rs.getDouble("price") + " : " + rs.getInt("quantity"));
                        }
                        break;

                    case 5:
                        System.out.println("exit");
                        return;
                    default:
                        System.out.println("Invalid choice.");
                }
            } 
            
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}