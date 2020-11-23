<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>글쓰기</title>
</head>
<body>
	<form action="register" method="POST">
		제목 : <input type="text" name="title"/><br/>
		내용 : <input type="text" name= "content"/><br/>
		글쓴이 : <input type="text" name="writer"/><br/>
		<button>글쓰기</button>
	</form>
</body>
</html>