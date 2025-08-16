
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class calculator_logic extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            int num1 = Integer.parseInt(request.getParameter("num1"));
            int num2 = Integer.parseInt(request.getParameter("num2"));
            String operation = request.getParameter("operation");
            int result = 0;
            if (operation.equals("Addition")) 
            {
                result = num1 + num2;
                out.println("<h1>Sum of " + num1 + " + " + num2 + " is: "+result+"</h1>");
            } 
            else if(operation.equals("Subtraction"))
            {
                result = num1 - num2;
                out.println("<h1>Subtraction of " + num1 + " - " + num2 + " is: "+result+"</h1>");
            }
            else if(operation.equals("Multiplication"))
            {
                result = num1 * num2;
                out.println("<h1>Multiplication of " + num1 + " * " + num2 + " is: "+result+"</h1>");
            }
            else if(operation.equals("Division"))
            {
                if(num2 == 0) {
                    out.println("<h1 style='color:red;'>Error: Division by zero is not allowed!</h1>");
                } else {
                    result = (int) num1 / num2;
                    out.println("<h1>Division of " + num1 + " / " + num2 + " is: "+result+"</h1>");
                }
            }
            else
            {
                out.println("<h1 style='color:red;'>Invalid operation selected !</h1>");
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
