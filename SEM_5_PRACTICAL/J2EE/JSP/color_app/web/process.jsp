<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    String color = request.getParameter("color");
    if ("blue".equalsIgnoreCase(color)) {
%>
        <jsp:forward page="blue.jsp" />
<%
    } else {
%>
        <jsp:forward page="default.jsp" />
<%
    }
%>
