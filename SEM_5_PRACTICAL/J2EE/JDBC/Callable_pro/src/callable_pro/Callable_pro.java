package callable_pro;
import java.sql.*;

//public class Callable_pro {
//
//    public static void main(String[] args) {
//       System.out.println("Hello from J2EE.!");
//        try {
//            Class.forName("com.mysql.cj.jdbc.Driver");
//            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
//            System.out.println("Database is connected successfully!");
//            String query ="{call default_insert()}";
//            CallableStatement cst = con.prepareCall(query);
//            cst.executeUpdate();
//            System.out.println("Data Inserted Successfully using  Procedures!");
//        } catch (Exception e) {
//            System.out.println("Database is not connected!");
//            System.out.println("Error: " + e.getMessage());
//        }
//    }
//}
            //program 16
            import java.util.Scanner;

            public class Callable_pro {
            public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            try 
            {
            System.out.print("Enter Employee No: ");
            int empno = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter Employee Name: ");
            String empnm = sc.nextLine();

            System.out.print("Enter Designation: ");
            String designation = sc.nextLine();

            System.out.print("Enter City: ");
            String city = sc.nextLine();

            System.out.print("Enter Salary: ");
            double salary = sc.nextDouble();
            sc.nextLine();

            System.out.print("Enter Department: ");
            String department = sc.nextLine();

            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            String query ="{call dynamic_insert(?, ?, ?, ?, ?, ?)}";
            CallableStatement cs = con.prepareCall(query);

            cs.setInt(1, empno);
            cs.setString(2, empnm);
            cs.setString(3, designation);
            cs.setString(4, city);
            cs.setDouble(5, salary);
            cs.setString(6, department);

            cs.executeUpdate();
            System.out.println("Dynamic Data inserted successfully!");

        } catch (Exception e) {
           System.out.println("Database is not connected!");
            System.out.println("Error: " + e.getMessage());
        }
    }
}
    //Program 17
//    public class Callable_pro {
//    public static void main(String[] args) {
//        try
//        {
//            Class.forName("com.mysql.cj.jdbc.Driver");
//            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
//            System.out.println("Database is connected!");
//            CallableStatement cs = con.prepareCall("{call get_designation(?, ?)}");
//            cs.setInt(1, 1); 
//            cs.registerOutParameter(2, Types.VARCHAR);
//            cs.executeQuery();
//            System.out.println("Designation: " + cs.getString(2));
//         }catch (Exception e) {
//           System.out.println("Database is not connected!");
//           System.out.println("Error: " + e.getMessage());
//        }
//    }
//}

//import java.util.Scanner;
//
//public class Callable_pro {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        
//        try {
//            Class.forName("com.mysql.cj.jdbc.Driver");
//
//            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
//            System.out.println("Database is connected!");
//
//            System.out.print("Enter designation: ");
//            String desig = sc.nextLine();
//
//            CallableStatement cs = con.prepareCall("{call get_emps_by_designation(?)}");
//            cs.setString(1, desig);
//
//            ResultSet rs = cs.executeQuery();
//            while (rs.next()) {
//                System.out.println(
//                    "EmpNo: " + rs.getInt("empno") +
//                    ", Name: " + rs.getString("empnm") +
//                    ", Designation: " + rs.getString("designation") +
//                    ", City: " + rs.getString("city") +
//                    ", Salary: " + rs.getDouble("salary") +
//                    ", Department: " + rs.getString("department")
//                );
//            }
//        } catch (Exception e) {
//            System.out.println("Database is not connected!");
//            System.out.println("Error: " + e.getMessage());
//        }
//    }
//}
