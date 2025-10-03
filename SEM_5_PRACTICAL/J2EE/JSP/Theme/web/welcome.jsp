<%@ page import="javax.servlet.http.Cookie" %>
<%
    String userTheme = "light"; // default theme

    Cookie[] cookies = request.getCookies();
    if (cookies != null) {
        for (Cookie c : cookies) {
            if (c.getName().equals("userTheme")) {
                userTheme = c.getValue();
                break;
            }
        }
    }
%>
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: <%= userTheme.equals("dark") ? "#333" : "#fff" %>;
            color: <%= userTheme.equals("dark") ? "#fff" : "#000" %>;
        }
    </style>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Your selected theme is: <strong><%= userTheme %></strong></p>
    <p><a href="index.html">Change Theme</a></p>
</body>
</html>
