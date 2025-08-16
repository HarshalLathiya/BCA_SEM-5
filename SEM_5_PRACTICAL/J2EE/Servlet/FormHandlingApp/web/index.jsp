<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <title>Form Page</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h2>Click the button to open the Submit form</h2>
        <form action="NewServlet" >
            Name: <input type='text' name='name'><br><br>
            <input type="submit" value="Open Form">
        </form>
    </body>
</html>
