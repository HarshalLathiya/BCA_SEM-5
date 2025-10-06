
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h2 align='center'>
        <%--Declaration Tag --%>
        <%!
            int fun() {
                return 10 + 10;
            }%>
        <%--Scriptlet Tag --%>
        <% out.println("Sum is:"+fun());%>
        <br>
        <%--Expression Tag --%>
        <%="Using Expression tag:"+fun()%>
        </h2>
    </body>
</html>
