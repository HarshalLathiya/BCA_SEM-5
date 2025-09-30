<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            String num1Str = request.getParameter("num1");
            String num2Str = request.getParameter("num2");
            String operation = request.getParameter("operation");

            if (num1Str != null && num2Str != null && operation != null) {
                try {
                    int num1 = Integer.parseInt(num1Str);
                    int num2 = Integer.parseInt(num2Str);
                    int result = 0;

                    if (operation.equals("Addition")) {
                        result = num1 + num2;
        %>
        <h1>Sum of <%=num1%> + <%=num2%> is: <%=result%></h1>
        <%
        } else if (operation.equals("Subtraction")) {
            result = num1 - num2;
        %>
        <h1>Subtraction of <%=num1%> - <%=num2%> is: <%=result%></h1>
        <%
        } else if (operation.equals("Multiplication")) {
            result = num1 * num2;
        %>
        <h1>Multiplication of <%=num1%> * <%=num2%> is: <%=result%></h1>
        <%
        } else if (operation.equals("Division")) {
            if (num2 == 0) {
        %>
        <h1 style="color:red;">Error: Division by zero is not allowed!</h1>
        <%
        } else {
            result = num1 / num2;
        %>
        <h1>Division of <%=num1%> / <%=num2%> is: <%=result%></h1>
        <%
            }
        } else {
        %>
        <h1 style="color:red;">Invalid operation selected!</h1>
        <%
            }
        } catch (NumberFormatException e) {
        %>
        <h1 style="color:red;">Invalid number format! Please enter integers only.</h1>
        <%
            }
        } else {
        %>
        <h1 style="color:blue;">Please enter numbers and select an operation.</h1>
        <%
            }
        %>
    </body>
</html>
