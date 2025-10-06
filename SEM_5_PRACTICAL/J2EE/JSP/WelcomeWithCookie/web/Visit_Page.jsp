<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="javax.servlet.http.Cookie" %>
<%
    boolean isNewUser = true; 

    Cookie[] cookies = request.getCookies();

    if(cookies != null) {
        for(Cookie cookie : cookies) {
            if(cookie.getName().equals("visited")) {
                isNewUser = false;
                break;
            }
        }
    }

    if(isNewUser) {
        Cookie visitCookie = new Cookie("visited", "yes");
        visitCookie.setMaxAge(30);
        response.addCookie(visitCookie);
    }
%>

<html>
<head>
    <title>Welcome Page</title>
</head>
<body>
<h2>
<%= isNewUser ? "Welcome!" : "Welcome back!" %>
</h2>
</body>
</html>
