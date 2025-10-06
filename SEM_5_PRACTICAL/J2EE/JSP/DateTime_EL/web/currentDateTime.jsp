<%@ page import="java.util.Date, java.text.SimpleDateFormat" %>
<%
    Date now = new Date();

    SimpleDateFormat DF = new SimpleDateFormat("dd-MM-yyyy hh:mm:ss a");

    String formattedDate = DF.format(now);

    request.setAttribute("currentDate", formattedDate);
%>

<!DOCTYPE html>
<html>
<head>
    <title>Current Date and Time</title>
</head>
<body>
    <h2>Current Date and Time</h2>
    <p>${currentDate}</p>
</body>
</html>
