<%@ page isErrorPage="true" %>
<html>
<head>
    <title>Error Page</title>
</head>
<body>
    <h2>Error occurred during division</h2>
    <p style="color:red;">
        Exception Type: <b><%= exception.getClass().getName() %></b><br/>
        Message: <b><%= exception.getMessage() %></b><br/><br/>
    </p>
    <a href="divide.jsp">Try Again</a>
</body>
</html>
