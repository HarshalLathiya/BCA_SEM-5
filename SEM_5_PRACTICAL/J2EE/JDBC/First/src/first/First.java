package first;

import java.sql.*;
import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        System.out.println("Hello from J2EE.!");
        
        //CREATE TABLE emp (empno INT PRIMARY KEY,empnm VARCHAR(50),designation VARCHAR(50),city VARCHAR(50),salary DOUBLE,department VARCHAR(50));

        try {
            Scanner sc = new Scanner(System.in);
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            System.out.println("Database is connected successfully!");
            int choice;
            do {
                System.out.println("\n");
                System.out.println("\n");
                System.out.println("1. Insert Employee (p1)");
                System.out.println("2. View All Employees (p2)");
                System.out.println("3. View Employees with Salary > 50000 (p3)");
                System.out.println("4. View Employees from Rajkot (p4)");
                System.out.println("5. View Names Starting with 'A' (p5)");
                System.out.println("6. View Managers (p6)");
                System.out.println("7. Count Employees (p7)");
                System.out.println("8. Show Highest Paid Employee (p8)");
                System.out.println("9. Sort Employees by Name (p9)");
                System.out.println("10. Search by Emp No (p10)");
                System.out.println("11. List by Department (p11)");
                System.out.println("0. Exit");
                System.out.print("Enter your choice: ");
                choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {
                    case 1 : p1_AddEmployee(con, sc);break;
                    case 2 : p2_ViewAll(con);break;
                    case 3 : p3_ViewHighSalary(con);break;
                    case 4 : p4_ViewFromCity(con);break;
                    case 5 : p5_ViewStartsWithA(con);break;
                    case 6 : p6_ViewManagers(con);break;
                    case 7 : p7_CountEmployees(con);break;
                    case 8 : p8_HighestSalary(con);break;
                    case 9 : p9_SortByName(con);break;
                    case 10 : p10_SearchByEmpNo(con, sc);break;
                    case 11 : p11_ListByDepartment(con, sc);break;
                    case 0 : System.out.println("Exiting... Goodbye!");break;
                    default : System.out.println("Invalid choice! Try again.");
                }

            } while (choice != 0);

        } catch (Exception e) {
            System.out.println("Database is not connected!");
            System.out.println("Error: " + e.getMessage());
        }
    }

        // (p1) Insert employee
        static void p1_AddEmployee(Connection con, Scanner sc) throws SQLException {
        
        //INSERT INTO emp(empno, empnm, designation, city, salary, department)VALUES (1, 'Harshal', 'Developer', 'Amreli', 65000, 'IT');
        
        System.out.print("Enter Emp no : ");
        int empno = sc.nextInt();
        sc.nextLine();
        
        System.out.print("Enter Emp name : ");
        String empnm = sc.nextLine();
        
        System.out.print("Enter Emp designation : ");
        String designation = sc.nextLine();
        
        System.out.print("Enter Emp city : ");
        String city = sc.nextLine();
        
        System.out.print("Enter Emp salary : ");
        double salary = sc.nextDouble();
        sc.nextLine();
        
        System.out.print("Enter Emp department : ");
        String department = sc.nextLine();

        String query = "INSERT INTO emp VALUES (?, ?, ?, ?, ?, ?)";
        PreparedStatement pst = con.prepareStatement(query);
        pst.setInt(1, empno);
        pst.setString(2, empnm);
        pst.setString(3, designation);
        pst.setString(4, city);
        pst.setDouble(5, salary);
        pst.setString(6, department);
        pst.executeUpdate();
        System.out.println("Employee inserted successfully!\n");
    }

    // (p2) View all employees
    static void p2_ViewAll(Connection con) throws SQLException
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp");
        while (rs.next()) 
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " +
                    rs.getString("designation") + ", " + rs.getString("city") + ", " +
                    rs.getDouble("salary") + ", " + rs.getString("department"));
        }
    }

    // (p3) Employees with salary > 50000
    static void p3_ViewHighSalary(Connection con) throws SQLException 
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp WHERE salary > 50000");
        while (rs.next())
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getDouble("salary"));
        }
    }

    // (p4) Employees from Rajkot
    static void p4_ViewFromCity(Connection con) throws SQLException
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp WHERE city = 'Rajkot'");
        while (rs.next()) 
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("city"));
        }
    }

    // (p5) Names starting with 'A'
    static void p5_ViewStartsWithA(Connection con) throws SQLException
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp WHERE empnm LIKE 'A%'");
        while (rs.next())
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm"));
        }
    }

    // (p6) Designation = Manager
    static void p6_ViewManagers(Connection con) throws SQLException 
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp WHERE designation = 'Manager'");
        while (rs.next()) 
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("designation"));
        }
    }

    // (p7) Count employees
    static void p7_CountEmployees(Connection con) throws SQLException 
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT COUNT(*) FROM emp");
        if (rs.next()) 
        {
            System.out.println("Total Employees: " + rs.getInt(1));
        }
    }

    // (p8) Highest salary
    static void p8_HighestSalary(Connection con) throws SQLException
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp ORDER BY salary DESC LIMIT 1");
        if (rs.next())
        {
            System.out.println("Highest Paid Employee: " + rs.getString("empnm") + " - ₹" + rs.getDouble("salary"));
        }
    }

    // (p9) Sort by name
    static void p9_SortByName(Connection con) throws SQLException
    {
        ResultSet rs = con.createStatement().executeQuery("SELECT * FROM emp ORDER BY empnm ASC");
        while (rs.next())
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm"));
        }
    }

    // (p10) Search by empno
    static void p10_SearchByEmpNo(Connection con, Scanner sc) throws SQLException 
    {
        System.out.print("Enter Employee Number: ");
        int empno = sc.nextInt();
        PreparedStatement pst = con.prepareStatement("SELECT * FROM emp WHERE empno = ?");
        pst.setInt(1, empno);
        ResultSet rs = pst.executeQuery();
        while (rs.next()) 
        {
            System.out.println(rs.getInt("empno") + ", " + rs.getString("empnm") + ", " + rs.getString("designation"));
        }
    }

    // (p11) List by department
    static void p11_ListByDepartment(Connection con, Scanner sc) throws SQLException 
    {
        System.out.print("Enter Department: ");
        String dept = sc.nextLine();
        PreparedStatement pst = con.prepareStatement("SELECT empnm, designation FROM emp WHERE department = ?");
        pst.setString(1, dept);
        ResultSet rs = pst.executeQuery();
        while (rs.next())
        {
            System.out.println(rs.getString("empnm") + " - " + rs.getString("designation"));
        }
    }
}