package logic;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;

@WebServlet(name = "logic", urlPatterns = {"/logic"})
public class logic extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String srollno = request.getParameter("Student_Rollno");
            String sfname = request.getParameter("Student_FName");
            String slname = request.getParameter("Student_LName");
            String scourse = request.getParameter("Student_Course");
            String ssem = request.getParameter("Student_Semester");

            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/harshal_jee", "root", "");
                System.out.println("Database is connected successfully!");

                String query = "INSERT INTO stud (rollno, firstname, lastname, course, semester) VALUES (?, ?, ?, ?, ?)";
                PreparedStatement pstmt = con.prepareStatement(query);
                pstmt.setString(1, srollno);
                pstmt.setString(2, sfname);
                pstmt.setString(3, slname);
                pstmt.setString(4, scourse);
                pstmt.setString(5, ssem);

                int rowsInserted = pstmt.executeUpdate();

                out.println("<!DOCTYPE html>");
                out.println("<html>");
                out.println("<head>");
                out.println("<title>Insert Result</title>");
                out.println("</head>");
                out.println("<body>");
                if (rowsInserted > 0) {
                    out.println("<h2>Record inserted successfully!</h2>");
                    Statement st = con.createStatement();
                    String selectQuery = "SELECT * FROM stud";
                    ResultSet rs = st.executeQuery(selectQuery);

                out.println("<h3>Student Records:</h3>");
                out.println("<table border='1'><tr><th>Roll No</th><th>First Name</th><th>Last Name</th><th>Course</th><th>Semester</th></tr>");
                while (rs.next()) {
                    out.println("<tr>");
                    out.println("<td>" + rs.getString("rollno") + "</td>");
                    out.println("<td>" + rs.getString("firstname") + "</td>");
                    out.println("<td>" + rs.getString("lastname") + "</td>");
                    out.println("<td>" + rs.getString("course") + "</td>");
                    out.println("<td>" + rs.getString("semester") + "</td>");
                    out.println("</tr>");
                }
                    
                } else {
                    out.println("<h2>Failed to insert record.</h2>");
                }
                out.println("</body>");
                out.println("</html>");
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>
}
