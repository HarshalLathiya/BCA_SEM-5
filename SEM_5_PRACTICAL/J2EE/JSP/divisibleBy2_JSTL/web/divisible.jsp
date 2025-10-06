<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Divisible by 2 Checker</title>
</head>
<body>
    <h2>Check if a Number is Divisible by 2</h2>
    
    <form method="post">
        Enter a Number: <input type="number" name="number" required />
        <input type="submit" value="Check" />
    </form>

    <c:if test="${not empty param.number}">
        <c:set var="num" value="${param.number}" />
        
        <c:choose>
            <c:when test="${num % 2 == 0}">
                <p>${num} is <b>divisible by 2</b>.</p>
            </c:when>
            <c:otherwise>
                <p>${num} is <b>not divisible by 2</b>.</p>
            </c:otherwise>
        </c:choose>
    </c:if>
</body>
</html>
