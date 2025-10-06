<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html>
<head>
    <title>Visitor Counter using Application Object</title>
</head>
<body>
<%
    Integer counter = (Integer)application.getAttribute("counter");

    if (counter == null) {
        counter = 1;
    } else {
        counter = counter + 1; 
    }

    application.setAttribute("counter", counter);
%>

<h2>Welcome to My Website</h2>
<p>Total visit since server started: 
   <b><%= counter %></b>
</p>

</body>
</html>
