<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Leap Year Result</title>
</head>
<body>
    <%
    String yearStr = request.getParameter("year");
    if (yearStr != null) {
        try {
            int year = Integer.parseInt(yearStr);

            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                out.println(year + " is a Leap Year");
            } else {
                out.println(year + " is Not a Leap Year");
            }
        } catch (NumberFormatException e) {
            out.println("Invalid input. Please enter a valid year.");
        }
    } else {
        out.println("No year provided.");
    }
%>
</body>
</html>
