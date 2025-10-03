<%@ page import="javax.servlet.http.Cookie" %>
<%
    String theme = request.getParameter("theme");
    if (theme != null) {
        Cookie themeCookie = new Cookie("userTheme", theme);
        themeCookie.setMaxAge(60*60*24*30);
        response.addCookie(themeCookie);
    }
    response.sendRedirect("welcome.jsp");
%>
