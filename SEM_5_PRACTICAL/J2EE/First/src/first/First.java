package first;

import java.sql.*;
import java.util.Scanner;

public class First {

    public static void main(String[] args) {
        System.out.println("Hello from J2EE.!");
        try {
            Scanner sc = new Scanner(System.in);
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            System.out.println("Database is connected successfully!");

            //Statement st = con.createStatement();

            /*create table
            String query ="CREATE TABLE emp (em pno INT PRIMARY KEY, empnm VARCHAR(50), designation VARCHAR(50),
            city VARCHAR(50), salary DOUBLE, department VARCHAR(50))";*/
            
 /*static insert data
            String query="Insert into emp(empno,empnm,designation,city,salary,department)values(2,'Mihir','FullStack_Developer','Ahemdabad',750000,'CE')";*/
 
           //(1)  Write a program to insert a record of an employee into the emp table. (Dynamic Insert Data)
          /* System.out.print("Enter Emp no :");
           int empno = sc.nextInt();
           sc.nextLine();
           
           System.out.print("Enter Emp name :");
           String empnm = sc.nextLine();
           
           System.out.print("Enter Emp designation :");
           String designation = sc.nextLine();
           
           System.out.print("Enter Emp city :");
           String city = sc.nextLine();
           
           System.out.print("Enter Emp salary :");
           int salary = sc.nextInt();
           sc.nextLine();
           
           System.out.print("Enter Emp department :");
           String department = sc.nextLine();
           
           String query="Insert into emp values("+empno+",'"+empnm+"','"+designation+"','"+city+"','"+salary+"','"+department+"')";*/
 
            //(2)  Write a program to display all the records of employees. (select data)
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp");
            
            while (rs.next()) {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("designation") + ", " + rs.getString("city") + ", " + rs.getDouble("salary") + ", " + rs.getString("department"));
             }*/
            
            
            //(3)  Write a program to display employees whose salary is greater than 50000.
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp WHERE salary > 50000");
            while (rs.next()) {
                System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getDouble("salary"));
            }*/
            
            //(4)  Write a JDBC program to display employees who are from the city 'Rajkot'. 
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp WHERE city = 'Rajkot'");
            while (rs.next()) {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("city"));
            }*/
            
            //(5)  Write a program to display employees whose name starts with 'A'.
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp WHERE empnm LIKE 'A%'");
            while (rs.next()) {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm"));
            }*/
            
            //(6)  Write a program to display employees whose designation is manager. 
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp WHERE designation = 'Manager'");
            while (rs.next()) {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("designation"));
            }*/
            
            //(7)  Write a program to count the number of employees in the table. 
            /*ResultSet rs = st.executeQuery("SELECT COUNT(*) FROM emp");
            if (rs.next()) {
            System.out.println("Total Employees: " + rs.getInt(1));
            }*/
            
            //(8)  Write a program to display the employee with the highest salary.
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp ORDER BY salary DESC LIMIT 1");
            if (rs.next()) {
            System.out.println("Highest Paid Employee: " + rs.getString("empnm") + " : " + rs.getDouble("salary"));
            }*/
            
            //(9)  Write a program to sort employee records by empnm. 
            /*ResultSet rs = st.executeQuery("SELECT * FROM emp ORDER BY empnm ASC");
            while (rs.next()) {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm"));
            }*/
            
            /*10th program
            String query = "SELECT * FROM emp WHERE empno = ?";
            PreparedStatement pst = con.prepareStatement(query);
            System.out.print("Enter Employee Number: ");
            int empno = sc.nextInt();
            pst.setInt(1, empno);
            ResultSet rs = pst.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("designation"));
            }*/
            
            /*11th program
            String query = "SELECT empnm, designation FROM emp WHERE department = ?";
            PreparedStatement pst = con.prepareStatement(query);
            System.out.print("Enter Department: ");
            String dept = sc.nextLine();
            pst.setString(1, dept);
            ResultSet rs = pst.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getString("empnm") + " : " + rs.getString("designation"));
            }*/
            
            //st.executeUpdate(query);
            System.out.println("successfully");
        } catch (Exception e) {
            System.out.println("Database is not connected!");
            System.out.println("Error: " + e.getMessage());
        }
    }
}
