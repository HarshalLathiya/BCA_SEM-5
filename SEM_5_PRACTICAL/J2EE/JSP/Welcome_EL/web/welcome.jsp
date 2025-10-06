<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String username = request.getParameter("username");
    request.setAttribute("username", username);
%>
<!DOCTYPE html>
<html>
<head>
    <title>Welcome Page</title>
</head>
<body>
    <h2>Welcome Page</h2>
    <p>Hello, <b>${username}</b>! Welcome to our website. (Printed using Variable)</p>
    <p>Hello, <b>${param.username}</b>! Welcome to our website. (Printed using Param)</p>
</body>
</html>
