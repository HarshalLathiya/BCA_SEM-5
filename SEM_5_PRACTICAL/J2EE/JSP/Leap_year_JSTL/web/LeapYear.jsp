<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Leap Year Checker</title>
</head>
<body>
    <form method="post">
        Enter Any Year: <input type="text" name="year" required />
        <input type="submit" value="Check" />
    </form>

    <c:if test="${not empty param.year}">
        <c:set var="year" value="${param.year}" />

        <c:choose>
            <c:when test="${(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)}">
                <p>${year} is a <b>Leap Year</b>.</p>
            </c:when>
            <c:otherwise>
                <p>${year} is <b>Not a Leap Year</b>.</p>
            </c:otherwise>
        </c:choose>
    </c:if>
</body>
</html>
