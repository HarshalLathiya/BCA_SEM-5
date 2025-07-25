package metadata;
import java.sql.*;
public class Metadata {

    public static void main(String[] args) {
        try {
        Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
            System.out.println("Database is connected successfully!");
            DatabaseMetaData md = con.getMetaData();
            System.out.println("User Name: " + md.getUserName());
            System.out.println("Database Driver Name: " + md.getDriverName());
            System.out.println("Database Driver Version: " + md.getDriverVersion());
            System.out.println("Connection file: " + md.getConnection());   
        }
        catch(Exception e)
        {
            System.out.println("Error:"+ e.getMessage());
        }
    }
    
}
