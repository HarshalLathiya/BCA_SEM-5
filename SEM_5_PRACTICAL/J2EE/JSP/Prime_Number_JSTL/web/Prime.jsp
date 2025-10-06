<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Prime Numbers from 1 to 100</title>
</head>
<body>
    <h2>Prime Numbers from 1 to 100</h2>
    <c:forEach var="i" begin="2" end="100"> 
        <c:set var="isPrime" value="true" />

        <c:forEach var="j" begin="2" end="${i - 1}">
            <c:if test="${i % j == 0}">
                <c:set var="isPrime" value="false" />
            </c:if>
        </c:forEach>

        <c:if test="${isPrime}">
            ${i} &nbsp;
        </c:if>
    </c:forEach>
</body>
</html>
