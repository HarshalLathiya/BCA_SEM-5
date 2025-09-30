<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
    String pStr = request.getParameter("principal");
    String rStr = request.getParameter("rate");
    String tStr = request.getParameter("time");

    if(pStr != null && rStr != null && tStr != null){
        try {
            double principal = Double.parseDouble(pStr);
            double rate = Double.parseDouble(rStr);
            double time = Double.parseDouble(tStr);

            double simpleInterest = (principal * rate * time) / 100;

            out.println("<h3>Simple Interest: " + simpleInterest + "</h3>");
        } catch (NumberFormatException e) {
            out.println("<p style='color:red;'>Please enter valid numeric values.</p>");
        }
    }
%>

    </body>
</html>
