<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%String rollno = request.getParameter("Student_Rollno"); 
        String name = request.getParameter("Student_Name"); 
        String course = request.getParameter("Student_Course");
        String sem = request.getParameter("Student_Semester");%>
        <table border='1' cellpadding='10'>
            <tr>
                <th>Student Roll Number</th>
                <td>
                    <%= rollno%>
                </td>
            </tr>
            <tr>
                <th>Student Name</th>
                <td>
                    <%= name%>
                </td>
            </tr>
            <tr>
                <th>Student Course</th>
                <td>
                    <%= course%>
                </td>
            </tr>
            <tr>
                <th>Student Semester</th>
                <td>
                    <%= sem%>
                </td>
            </tr>
        </table>
    </body>
</html>
