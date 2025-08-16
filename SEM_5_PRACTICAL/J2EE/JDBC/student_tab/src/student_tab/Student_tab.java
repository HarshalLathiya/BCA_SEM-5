package student_tab;

import java.sql.*;
import java.util.Scanner;

public class Student_tab {

    public static void main(String[] args) {
        System.out.println("Hello From Student table:");
        Scanner sc = new Scanner(System.in);
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            System.out.println("Database is connected successfully!");

            //Statement st = con.createStatement();
            //String query = "CREATE TABLE stud (rollno INT PRIMARY KEY, firstname VARCHAR(50), lastname VARCHAR(50), course VARCHAR(50), semester VARCHAR(20))";
            //st.execute(query);

            /*String query = "INSERT INTO stud VALUES (?, ?, ?, ?, ?)";
            PreparedStatement pst = con.prepareStatement(query);
            
            System.out.print("Enter Roll No: ");
            int roll = sc.nextInt(); 
            sc.nextLine();
            
            System.out.print("Enter First Name: ");
            String fname = sc.nextLine();
            
            System.out.print("Enter Last Name: ");
            String lname = sc.nextLine();
            
            System.out.print("Enter Course: ");
            String course = sc.nextLine();
            
            System.out.print("Enter Semester: ");
            int sem = sc.nextInt();
            sc.nextLine();

            pst.setInt(1, roll);
            pst.setString(2, fname);
            pst.setString(3, lname);
            pst.setString(4, course);
            pst.setInt(5, sem);

            pst.executeUpdate();*/
            
            /*String query ="UPDATE stud SET Firstname = ?,lastname = ? where rollno = ?";
            
            PreparedStatement pst = con.prepareStatement(query);
            
            System.out.print("Enter Roll_number to update :");
            int roll = sc.nextInt();
            sc.nextLine();
            
            System.out.print("Enter new First Name :");
            String fname = sc.nextLine();
            
            System.out.print("Enter New Last name :");
            String lname = sc.nextLine();
            
            pst.setString(1,fname);
            pst.setString(2,lname);
            pst.setInt(3,roll);
            int rows = pst.executeUpdate();
             if (rows > 0)
             {
                System.out.println("Record updated successfully.");
             }
             else
             {
                System.out.println("No record found.");
             }*/
            
            String query = "DELETE FROM stud WHERE rollno = ?";
            PreparedStatement pst = con.prepareStatement(query);
            
            System.out.print("Enter Roll_Number to Delete :");
            int roll = sc.nextInt();
            
            pst.setInt(1,roll);
            int rows = pst.executeUpdate();
            if(rows>0)
            {
                System.out.print("Record Deleted succsessfully.");
            }
            else
            {
                System.out.println("No Record found.!");
            }
            
            System.out.println("successfully.");

        } catch (Exception e) {
            System.out.println("Database is not connected!");
            System.out.println("Error: " + e.getMessage());
        }
    }

}