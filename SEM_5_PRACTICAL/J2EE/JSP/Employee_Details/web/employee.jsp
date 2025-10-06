<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html>
<head>
    <title>Employee Bean Example</title>
</head>
<body>
    <jsp:useBean id="employee" class="My_pack.EmployeeBean" scope="session" />

    <jsp:setProperty name="employee" property="name" value="Harshal Lathiya" />
    <jsp:setProperty name="employee" property="designation" value="Software Developer" />
    <jsp:setProperty name="employee" property="salary" value="45000" />

    <!-- Display properties using EL -->
    <h2>Employee Details</h2>
    <p><b>Name:</b> ${employee.name}</p>
    <p><b>Designation:</b> ${employee.designation}</p>
    <p><b>Salary:</b> ${employee.salary}</p>
</body>
</html>
