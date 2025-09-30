<%@ page errorPage="errorPage.jsp" %>
<html>
<head>
    <title>Division Operation</title>
</head>
<body>
    <h2>Division Operation</h2>
    <form method="post">
        Dividend: <input type="text" name="dividend" required /><br/><br/>
        Divisor: <input type="text" name="divisor" required /><br/><br/>
        <input type="submit" value="Divide" />
    </form>

    <%
        if ("POST".equalsIgnoreCase(request.getMethod())) {
            try {
                int dividend = Integer.parseInt(request.getParameter("dividend"));
                int divisor = Integer.parseInt(request.getParameter("divisor"));

                int result = dividend / divisor;
                out.println("<h3>Result: " + dividend + " / " + divisor + " = " + result + "</h3>");
            } catch (NumberFormatException e) {
                out.println("<p style='color:red;'>Please enter valid integers.</p>");
            }
        }
    %>
</body>
</html>
