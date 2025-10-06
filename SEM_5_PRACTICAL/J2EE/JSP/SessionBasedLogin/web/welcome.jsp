<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String username = request.getParameter("username");

    if(username != null && !username.trim().isEmpty()) {
        session.setAttribute("username", username);
    }

    String sessionUsername = (String)session.getAttribute("username");

    if(sessionUsername == null) {
        response.sendRedirect("login.jsp");
        return;
    }
%>

<html>
<head>
    <title>Welcome Page</title>
</head>
<body>
<h2>Welcome, <%= sessionUsername %>!</h2>
<p>You are now logged in.</p>
<p><a href="logout.jsp">Logout</a></p>
</body>
</html>
