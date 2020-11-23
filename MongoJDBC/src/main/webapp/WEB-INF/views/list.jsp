<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메인</title>
</head>
<body>
	<a href="register"><h2>글쓰기</h2></a>
	
	<table border="1">
		<tr>
			<td>TITLE</td>
			<td>CONTENT</td>
			<td>WRITER</td>
		</tr>
		<c:forEach var="board" items="${boards }">
		<tr>
			<td><a href="detail/${board.bno }" >${board.title }</a></td>
			<td>${board.content }</td>
			<td>${board.writer }</td>
		</tr>
		</c:forEach>
	</table>
	
	
</body>
</html>