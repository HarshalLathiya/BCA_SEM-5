<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<meta http-equiv="refresh" content="5; url=login.jsp">
<%
    out.print("This site will logout in 5 sec");
    session.invalidate();
//    response.sendRedirect("login.jsp");
%>
