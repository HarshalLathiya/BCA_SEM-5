<%@ page isErrorPage="true" %>
<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #e74c3c; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for doesn't exist.</p>
    <p><a href="<%= request.getContextPath() %>/index.html">Return to Home Page</a></p>
</body>
</html>
