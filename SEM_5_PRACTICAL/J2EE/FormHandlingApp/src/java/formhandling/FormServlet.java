package formhandling;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;

public class FormServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        out.println("<html><head><title>Form</title></head><body>");
        out.println("<h2>Fill out the form</h2>");
        out.println("<form action='SubmitServlet' method='post'>");
        out.println("Name: <input type='text' name='name'><br><br>");
        out.println("Email: <input type='text' name='email'><br><br>");
        out.println("<input type='submit' value='Submit'>");
        out.println("</form>");
        out.println("</body></html>");
    }
}
