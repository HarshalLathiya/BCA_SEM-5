import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class SessionServlet extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        HttpSession session = request.getSession();
        String name = request.getParameter("username");

        if (name != null && !name.isEmpty())
        {
            session.setAttribute("username", name);
        }
        String sessionName = (String) session.getAttribute("username");

        out.println("<html><body>");
        if (sessionName != null) 
        {
            out.println("<h2>Welcome, " + sessionName + "!</h2>");
        } 
        else 
        {
            out.println("<h2>Hello, Guest! Please enter your name.</h2>");
            out.println("<a href='index.html'>Go to Form</a>");
        }
        out.println("</body></html>");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    @Override
    public String getServletInfo() {
        return "Servlet that stores username in session and greets user on subsequent visits.";
    }
}
