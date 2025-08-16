package metedata;
import java.sql.*;
public class Metedata {
    
    public static void main(String[] args) {
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            System.out.println("Database is connected successfully!");
            DatabaseMetaData md = con.getMetaData();
            System.out.println("Connection name:"+md.getC
                    onnection());
             System.out.println("Driver name:"+md.getDriverName());
              System.out.println("Driver Version :"+md.getDriverVersion());
        }
       catch (Exception e) {
            System.out.println("Database is not connected!");
            System.out.println("Error: " + e.getMessage());
        }
    } 
}
